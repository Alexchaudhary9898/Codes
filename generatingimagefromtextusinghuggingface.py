import requests
from PIL import Image
from io import BytesIo
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
def generate_image_from_text(prompt: str) -> Image.Image:
    """
    Sends a text promt to huggingface API and returns the genrated image
    """
    headers = {"Authorization": f"Bearer {hf_api}"}
    payload = {"inputs": prompt}
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        if "image" in response.headers.get("Content-type", ""):
            image = Image.open(BytesIo(response.content))
            return image
        else:
            raise Exception("the resposne is not an image. API may have returned an error message")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
def main():
    """
    main loop for user interaction
    continuosly prompts the user for texts and gives and option to save them
    """
    print("Welcome to the text-to-image generator")
    print("type 'exit' to quit the program.\n")
    while True:
        prompt = input("enter a description for the image you want to generate.\n").strip()
        if prompt.lower("q") == "exit":
            print("goodbye")
            break
        print("\nGenerating image...\n")
        try:
            image = generate_image_from_text(prompt)