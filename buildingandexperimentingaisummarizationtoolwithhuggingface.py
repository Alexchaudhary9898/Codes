import re
from colorama import Fore, Style, init
init(autoreset=True)
def clean_text(text):
    return re.sub(r'\+', '',text).strip()
def score_sentences(text):
    words = text.lower().split()
    freq = {w: words.count(w) for w in words}
    sentences = re.split(r'(?<=[.!?])+',text)
    scores = {}
    for s in sentences:
        scores[s] = sum(freq.get(w, 0) for w in s.lower().split())
        return sentences, scores
def summarize(text, n=2):
    text = clean_text(text)
    sentences, scores = score_sentences(text)
    if len(sentences) <= n:
        return text
    best = sorted(scores, key=scores.get, reverse= True)[:n]
    return " ".join(best)
print(Fore.YELLOW + Style.BRIGHT + " Hi there whats your name")
name = input("your name:").strip() or "user"
print(Fore.GREEN + f"\nEnter the text to summarize:\n")
text = input(Fore.YELLOW + "\nEnter the text to summarize:\n").strip()
if not text:
    print("no text provided")
else:
    print("\n choose summarization style:")
    print("1 standard (short)")
    print("2 detailed(longer)")
    choice = input(">").strip()
    num = 4 if choice == "2" else 2
    print(Fore.GREEN + Style.BRIGHT + "\n SUMMARY OUTPUT")
    print(summarize(text, num))