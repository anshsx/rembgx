from rembg import remove
from PIL import Image

def remove_background(input_path: str, output_path: str):
    with Image.open(input_path) as img:
        output = remove(img)
        output.save(output_path)
