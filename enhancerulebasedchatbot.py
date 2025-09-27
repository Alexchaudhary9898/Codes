import re, random
from colorama import Fore, init
init(autoreset=True)
destinations = {
    "beaches": ["Bali", "Maldives", "Phucket"],
    "mountains" : ["Swiss alps", "Rocky, Mountains", "Himalayas"],
    "cities" : ["Tokyo", "Paris", "New york"]
}
jokes = [
    "Why don't you programmers like nature? Too many bugs",
    "Why did the computer go to the doctor? It had a virus",
    "Why do travelers always feel warm? Because of all their hot spots"
]
def normalize(text): return re.sub(r"\s+"," ", text.strip().lower())
def recommend():
    pref = normalize(input(f"{Fore.CYAN}TravelBot: Beaches, mountains, or cities?in{Fore.YELLOW}You: "))
    if pref in destinations:
       while True:
        suggestion = random.choice(destinations[pref])
        print(f"{Fore.GREEN}TravelBot: How about {suggestion}?")
        ans = input(f"{Fore.YELLOW}You (yes/no): ").lower()
        if ans == "yes": return print(f"{Fore.GREEN}TravelBot: Awesome Enjoy {suggestion}")
        if ans == "no" : continue
        return
    else:
       print(f"{Fore.RED}TravelBot: Sorry, i dont have that type of destination.")
def packing():
   loc = normalize(input(f"{Fore.CYAN}TravelBot: were 2\n{Fore.YELLOW}you:"))
   days = input(f"{Fore.CYAN}TravelBot: how many days\n{Fore.YELLOW}you:")
   print(f"{Fore.GREEN}TravelBot: packing tips for {days} days in {loc}")
   print(f"- pack versatile clothes\n- bring chargers/adapters\n check the forecasts")
def tell_jokes(): print(f"{Fore.GREEN}TravelBot: {random.choice(jokes)}")
def show_help():
   print(f""{Fore.MAGENTA}\n can:
{Fore.GREEN}- suggest travel spots ('recommendation')
- offer packing tips ('packing'))