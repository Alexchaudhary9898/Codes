import requests
from requests.auth import HTTPBasicAuth

API_KEY = "acc_8f4a4b063d9191f"
API_SECRET = "0f5c32daac38a0f338273ccf5cf3fa1c"

def caption_single_image(image_path):
    url = "https://api.imagga.com/v2/tags"

    with open(image_path, "rb") as img:
        response = requests.post(
            url,
            auth=HTTPBasicAuth(API_KEY, API_SECRET),
            files={"image": img}
        )

    data = response.json()
    tags = data["result"]["tags"][:5]

    caption = ", ".join(tag["tag"]["en"] for tag in tags)

    print("Image:", image_path)
    print("Caption (generated from tags):", caption)


def main():
    image_path = input("Enter image path: ")
    caption_single_image(image_path)


if __name__ == "__main__":
    main()
