import argparse
from email.mime import image
from PIL import Image


class QuadtreeNode:
    lef


class Tree:
    root = QuadtreeNode()

if __name__ == "__main__":
    "MAIN FUNCTION"
    parser = argparse.ArgumentParser(description="Сжать изображение")
    parser.add_argument("image_path", type=str, help="Путь к изображению")
    parser.add_argument("-d", "--depth", type=int, default=2, help="Глубина дерева")
    parser.add_argument(
        "-l", "--lines", action="store_true", help="Show lines in image"
    )
    parser.add_argument(
        "-m",
        "--max_depth",
        action="store_true",
        help="Показать максимальную глубину изображения",
    )
    parser.add_argument(
        "-glove", "--gif_glove", action="store_true", help="создать гиф"
    )
    args = parser.parse_args()

    img = image.open(args.image_path).convert("RGB")
    box = img.getbbox() 
    node = QuadtreeNode()