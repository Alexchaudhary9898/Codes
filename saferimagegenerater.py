import re
import requests
from urllib.parse import quote
from PIL import Image
from io import BytesIO

# -----------------------------
# Classroom Safety Filter
# -----------------------------

RESTRICTED_PATTERNS = [
    r"\b(adult|mature)\b",
    r"\b(violent|harm|attack)\b",
    r"\b(self[-\s]?harm)\b",
    r"\b(weapon|explosive)\b",
    r"\b(hate|extremism)\b",
    r"\b(illegal|drugs)\b"
]

def is_safe(prompt):
    for pattern in RESTRICTED_PATTERNS:
        if re.search(pattern, prompt, flags=re.IGNORECASE):
            return False
    return True


# -----------------------------
# Image Generator Function
# -----------------------------

def generate_image(prompt):
    encoded_prompt = quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=60)
    except requests.exceptions.RequestException:
        print("Network error. Check internet connection.")
        return

    if response.status_code != 200:
        print(f"Server Error: {response.status_code}")
        return

    content_type = response.headers.get("Content-Type", "")
    if "image" not in content_type:
        print("API did not return a valid image. Try again.")
        return

    try:
        img = Image.open(BytesIO(response.content))
        img.save("generated_image.png")
        print("✅ Image saved as generated_image.png")
    except Exception:
        print("Failed to process image.")


# -----------------------------
# Main Program
# -----------------------------

if __name__ == "__main__":
    user_prompt = input("Enter image description: ")

    if not user_prompt.strip():
        print("Please enter a valid description.")
    elif not is_safe(user_prompt):
        print("Prompt not allowed in classroom mode.")
    else:
        final_prompt = user_prompt + ", high quality, detailed"
        print("Generating image...")
        generate_image(final_prompt)