"""
app.py
-------
Fast interactive inference script for English → Bengali translation.
Loads the base Helsinki-NLP/opus-mt-en-bn model with the saved LoRA adapter
and translates user-supplied English sentences to Bengali.

Usage (single sentence):
    python demo.py --text "The weather is beautiful today."

Usage (interactive REPL mode):
    python demo.py --interactive

Usage (translate a text file, one sentence per line):
    python demo.py --file input.txt --output output.txt
"""

import argparse
import logging
import sys
import time
from pathlib import Path

import torch
from peft import PeftModel
from transformers import MarianMTModel, MarianTokenizer

# ──────────────────────────────────────────────────────────────────────────────
# Logging (minimal for demo)
# ──────────────────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

# ──────────────────────────────────────────────────────────────────────────────
# Defaults
# ──────────────────────────────────────────────────────────────────────────────
BASE_MODEL_NAME: str = "Helsinki-NLP/opus-mt-en-bn"
DEFAULT_ADAPTER_PATH: str = "./final_bengali_adapter"


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="English → Bengali translation demo using LoRA-adapted MarianMT."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--text",
        type=str,
        default=None,
        help="Single English sentence to translate.",
    )
    group.add_argument(
        "--interactive",
        action="store_true",
        help="Launch interactive REPL for repeated translations.",
    )
    group.add_argument(
        "--file",
        type=str,
        default=None,
        help="Path to a text file with one English sentence per line.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="(Optional) Path to write translations when using --file.",
    )
    parser.add_argument(
        "--adapter_path",
        type=str,
        default=DEFAULT_ADAPTER_PATH,
        help="Path to the LoRA adapter directory.",
    )
    parser.add_argument(
        "--base_model",
        type=str,
        default=BASE_MODEL_NAME,
        help="Base MarianMT model identifier.",
    )
    parser.add_argument(
        "--num_beams",
        type=int,
        default=4,
        help="Beam width for generation (higher = better quality, slower).",
    )
    parser.add_argument(
        "--max_length",
        type=int,
        default=128,
        help="Maximum number of generated tokens.",
    )
    parser.add_argument(
        "--device",
        type=str,
        default=None,
        help="Device override ('cpu', 'cuda', 'mps'). Auto-detected if not set.",
    )
    return parser.parse_args()


# ──────────────────────────────────────────────────────────────────────────────
# Model loading (cached at module level for interactive mode)
# ──────────────────────────────────────────────────────────────────────────────
def _select_device(device_override: str | None) -> torch.device:
    if device_override:
        return torch.device(device_override)
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def load_pipeline(
    base_model_name: str,
    adapter_path: str,
    device: torch.device,
) -> tuple[PeftModel, MarianTokenizer]:
    """
    Load the base model + LoRA adapter and move to device.

    Returns a (model, tokenizer) tuple ready for inference.
    Prints a friendly loading message to stderr so stdout stays clean.
    """
    print("⏳  Loading model …", file=sys.stderr)
    t0 = time.perf_counter()

    base_model = MarianMTModel.from_pretrained(base_model_name)
    model = PeftModel.from_pretrained(base_model, adapter_path)
    model = model.to(device)
    model.eval()

    tokenizer = MarianTokenizer.from_pretrained(adapter_path)

    elapsed = time.perf_counter() - t0
    print(f"✅  Model ready ({elapsed:.1f}s) | device: {device}", file=sys.stderr)
    return model, tokenizer


# ──────────────────────────────────────────────────────────────────────────────
# Core translation function
# ──────────────────────────────────────────────────────────────────────────────
def translate(
    text: str,
    model: PeftModel,
    tokenizer: MarianTokenizer,
    device: torch.device,
    num_beams: int = 4,
    max_length: int = 128,
) -> str:
    """
    Translate a single English sentence to Bengali.

    Args:
        text:       Source English string.
        model:      LoRA-adapted MarianMT model.
        tokenizer:  Matching tokenizer.
        device:     Inference device.
        num_beams:  Beam search width.
        max_length: Token length cap for generation.

    Returns:
        Decoded Bengali translation string.
    """
    inputs = tokenizer(
        [text.strip()],
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=max_length,
    ).to(device)

    with torch.no_grad():
        generated_ids = model.generate(
            **inputs,
            max_length=max_length,
            num_beams=num_beams,
            early_stopping=True,
        )

    output = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return output


# ──────────────────────────────────────────────────────────────────────────────
# Execution modes
# ──────────────────────────────────────────────────────────────────────────────
def run_single(args: argparse.Namespace, model, tokenizer, device) -> None:
    """Translate a single sentence and print result."""
    result = translate(args.text, model, tokenizer, device,
                       num_beams=args.num_beams, max_length=args.max_length)
    print(f"\n🇬🇧  English  : {args.text}")
    print(f"🇧🇩  Bengali  : {result}\n")


def run_interactive(args: argparse.Namespace, model, tokenizer, device) -> None:
    """Interactive REPL loop for repeated translations."""
    print("\n" + "═" * 60)
    print("  English → Bengali Translation (REPL)")
    print("  Type 'quit' or press Ctrl+C to exit.")
    print("═" * 60 + "\n")
    while True:
        try:
            text = input("🇬🇧  English  : ").strip()
            if not text:
                continue
            if text.lower() in {"quit", "exit", "q"}:
                print("Goodbye! / বিদায়!")
                break
            t0 = time.perf_counter()
            result = translate(text, model, tokenizer, device,
                               num_beams=args.num_beams, max_length=args.max_length)
            elapsed_ms = (time.perf_counter() - t0) * 1000
            print(f"🇧🇩  Bengali  : {result}  ({elapsed_ms:.0f} ms)\n")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye! / বিদায়!")
            break


def run_file(args: argparse.Namespace, model, tokenizer, device) -> None:
    """Translate all sentences in a text file."""
    input_path = Path(args.file)
    if not input_path.exists():
        print(f"❌  File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    sentences = [line.strip() for line in input_path.read_text(encoding="utf-8").splitlines()
                 if line.strip()]

    print(f"📄  Translating {len(sentences)} sentence(s) from '{args.file}' …\n")
    results = []
    for i, sentence in enumerate(sentences, 1):
        translation = translate(sentence, model, tokenizer, device,
                                num_beams=args.num_beams, max_length=args.max_length)
        results.append(translation)
        print(f"[{i:>3}] EN: {sentence}")
        print(f"       BN: {translation}\n")

    if args.output:
        output_path = Path(args.output)
        output_path.write_text("\n".join(results), encoding="utf-8")
        print(f"✅  Translations saved to '{args.output}'")


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────
def main() -> None:
    args = parse_args()
    device = _select_device(args.device)

    # Default to interactive if no mode specified
    if args.text is None and not args.interactive and args.file is None:
        args.interactive = True

    model, tokenizer = load_pipeline(args.base_model, args.adapter_path, device)

    if args.text:
        run_single(args, model, tokenizer, device)
    elif args.file:
        run_file(args, model, tokenizer, device)
    else:
        run_interactive(args, model, tokenizer, device)


if __name__ == "__main__":
    main()
