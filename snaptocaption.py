import requests
from requests.auth import HTTPBasicAuth
from PIL import Image
import os
from colorama import init, Fore, Style
init(autoreset = True)
API_KEY = "acc_8f4a4b063d9191f"
API_SECRET = "0f5c32daac38a0f338273ccf5cf3fa1c"
IMAGGA_URL = "https://api.imagga.com/v2/tags"
def truncate_text(text, word_limit):
    words = text.split()
    return " ".join(words[:word_limit])
def get_image_tags(image_path, limit=10):
    with open(image_path, "rb") as img:
        response = requests.post(
            IMAGGA_URL,
            auth=HTTPBasicAuth(API_KEY, API_SECRET),
            files={"image": img}
        )
    data = response.json()
    tags = data.get("result", {}).get("tags",{})
    return [tag["tag"]["en"] for tag in tags[:limit]]
def generate_caption(tags):
    return truncate_text(", ".join(tags), 5)
def generate_description(tags):
    sentence = (
        f"This image shows {tags[0]}, "
        f"it includes elements such as {', '.join(tags[1:6])}, "
        f"the scene appears visually clear and well composed."
    )
    return truncate_text(sentence, 30)
def generate_summary(tags):
    sentence = (
        f"the image primarily features {tags[0]}, "
        f"other visible elements include {', '.join(tags[1:7])}, "
        f"the objects are clearly distinguisable and form a  meaningful scene. "
        f"the image provides a simple yet informative visual representation. "
    )
    return truncate_text(sentence, 50)
def print_menu():
    print(f"""{Style.BRIGHT}{Fore.GREEN}
          IMAGE TO TEXT CONVERSION
          select output type:
          1. Caption (5 words)
          2. description (30 words)
          3. summary (50 words)
          4. exit
          """)
def main():
    image_path = input(f"{Fore.BLUE}Enter Image path: {Style.RESET_ALL}")
    if not os.path.exists(image_path):
        print(f"{Fore.RED}❌ Image file not found.")
        return
    try:
       Image.open(image_path)
    except:
        print(f"{Fore.RED} invalid image file.")
        return
    
    print(f"{Fore.YELLOW}Analyzing image.\n")
    tags = get_image_tags(image_path)
    if not tags:
        print(f"{Fore.RED} failed to generate tags.")
    while True:
        print_menu()
        choice = input("enter choice(1 4):")
        if choice == "1":
          caption = generate_caption(tags)
          print(f"{Fore.YELLOW} caption (5 words): {Style.BRIGHT}{caption}\n")
        elif choice == "2":
          desc  = generate_description(tags)
          print(f"{Fore.CYAN}description (30 words): {Style.BRIGHT} {desc}\n")
        elif choice == "3":
          summary = generate_summary(tags)
          print(f"{Fore.GREEN} summary(50 words): {Style.BRIGHT}{summary}\n")
        elif choice == "4":
          print(f"{Fore.GREEN} goodbye")
          break
        else:
            print(f"{Fore.RED} invalid choice, try again.\n")
if __name__ == "__main__":
    main()