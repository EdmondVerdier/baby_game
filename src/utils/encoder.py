import base64
from io import BytesIO
from PIL import Image

def encode_image_to_base64(image_path : str) -> str:
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string


def decode_image_from_base64(encoded_string :str) -> Image.Image:
    decoded_bytes = base64.b64decode(encoded_string)
    image = Image.open(BytesIO(decoded_bytes))
    return image
