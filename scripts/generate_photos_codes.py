from src.utils.encoder import encode_image_to_base64
from src.constants import MATCH_PHOTOS

def generate_photos_codes(output_file: str) -> None:
    with open(output_file, 'w') as file:
        file.write("[\n")
        for sicariot in MATCH_PHOTOS:
            photo_path = str(sicariot["photo"])
            encoded_photo = encode_image_to_base64(photo_path)
            file.write(f'{{"name": "{sicariot["name"]}", "photo": "{encoded_photo}"}},\n')
        file.write("]\n")

if __name__ == "__main__":
    generate_photos_codes("data/photos_codes.txt")
