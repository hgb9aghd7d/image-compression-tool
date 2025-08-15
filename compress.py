import os
from PIL import Image
from pathlib import Path
import argparse

def compress_image(input_path, output_path, quality):
    img = Image.open(input_path)
    img_format = img.format if img.format in ['JPEG', 'PNG', 'WEBP'] else 'JPEG'
    
    img.save(output_path, format=img_format, optimize=True, quality=quality)

def batch_compress(input_dir, output_dir, quality):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for img_file in input_path.glob("*"):
        if img_file.suffix.lower() not in [".jpg", ".jpeg", ".png", ".webp"]:
            continue

        out_file = output_path / img_file.name
        compress_image(img_file, out_file, quality)
        print(f"Compressed: {img_file.name} -> {out_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Image Compression Tool")
    parser.add_argument('--input', required=True, help='Input folder path')
    parser.add_argument('--output', required=True, help='Output folder path')
    parser.add_argument('--quality', type=int, default=70, help='Compression quality (0-100)')
    
    args = parser.parse_args()
    batch_compress(args.input, args.output, args.quality)
