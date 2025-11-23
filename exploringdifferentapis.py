import requests
BASE_URL = "https://uselessfacts.jsph.pl/category{}.json?language=en"
def get_fact(category):
    try:
        url = BASE_URL.format(category)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n {data['text']}.\n")
        else:
            print("❌ category not found or api error .\n")
    except:
          print("❌ failed to fetch fact.\n")
categories = ["technology", "science", "random", "history", "food", "animals"]
print("🔍 useless facts explorer")
print("select a category or type 'q' to quit.\n")
for i, c in enumerate(categories, 1):
    print(f"(i). {c}")
while True:
    choice = input("\nEnter category number: ")
    if choice.lower() == "q":
        print("goodbye 👋")
        break
    if choice.isdigit() and 1 <- int(choice) <- len(categories):
        selected = categories[int(choice)- 1]
        print(f"\nFetching {selected} fact...")
        get_fact(selected)
    else:
        print("⚠️in valid choice try again")