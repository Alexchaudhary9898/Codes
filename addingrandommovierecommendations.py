import pandas as pd, random, time, sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore, Style
init(autoreset=True)

# Load data
def load_data(path='imdb_top_1000.csv'):
    try:
        df = pd.read_csv(path)
        df['combined'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"File {path} not found."); sys.exit()

def load_data(path='Codes/imdb_top_1000.csv'):
    try:
        df = pd.read_csv(path)
        df['combined'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"file {path} not found."); sys.exit()
movies = load_data()
tfidf = TfidfVectorizer(stop_words='english')
cosine_sim =cosine_similarity(tfidf.fit_transform(movies['combined']))
def list_genres(df): return sorted({g.strip() for x in df['Genre'].dropna()
    for g in x.split(',')})
genres = list_genres(movies)
def recommend(genre=None, mood=None, rating=0, top_n=5):
    df = movies
    if genre: df = df[df['Genre'].str.contains(genre, case=False, na=False)]
    if rating: df = df[df['IMDB_Rating'] >= rating]
    df = df.sample(frac=1)
    recs = [(r['Series_Title'], TextBlob(r['Overview']).sentiment.polarity)
            for _, r in df.iterrows() if not mood or TextBlob(mood).sentiment.polarity * TextBlob(r['Overview']).sentiment.polarity >= 0]
    return recs[:top_n] or "No suitable movie recommendations found"
def show(recs, name):
    print(Fore.YELLOW + f"\n AI recommendations for {name}:")
    for t, p in recs: print(f"- {t} ({'Positive' if p>0 else 'Negative' if p<0 else 'Neutral'})")
def main():
    print(Fore.BLUE + "Welcome to ai movie assistant \n")
    name = input(Fore.YELLOW+"your name: ").strip()
    print(Fore.GREEN+f"great to meet you. {name}\n\nAvailable Genres:")
    [print(f"{i+1}. {g}") for i,g in enumerate(genres)]
    while True:
        g = input(Fore.YELLOW+"pick genre (or press enter to skip: ").strip()
        g = g if g in genres else None
        mood = input(Fore.YELLOW+"mood (Describe how you feel): ").strip()
        r = input(Fore.YELLOW+"Minimum rating (0-10, default 0):")
        r = float(r if r.isdigit() else 0 )
        show(recommend(g, mood, r), name)
        if input(Fore.YELLOW+"\nMore recommendations? (yes/no): ").lower()!="yes":
            print(Fore.GREEN+f"Enjoy your movies {name}! "); break
if __name__=="__main__":main()