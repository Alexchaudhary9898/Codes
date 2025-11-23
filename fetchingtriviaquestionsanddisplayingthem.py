import requests
import random
import html
EDUCATION_CATEGORY_ID = 9
API_URL = f'https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple'
def get_education_questions():
    repsonse = requests.get(API_URL)
    if repsonse.status_code == 200:
        data = repsonse.json()
        if data['response_code'] == 0 and data['results']:
            return data['results']
        return None
def run_quiz():
    questions = get_education_questions()
    if not questions:
        print("failed to fetch educational questions")
        return
    score = 0
    print("WElcome to the education quiz")
    for i, q in enumerate(questions, 1):
       questions = html.unescape(q['question'])
       correct = html.unescape(q['correct_answer'])
       incorrects = [html.unescape(a) for a in q ['incorrect_answers']]
       options = incorrects + [correct]
       random.shuffle(options)
       print(f"question [i] {questions}")
       for idx, option in enumerate(options, 1):
           print(f"{idx}. {option}")
       while True:
          try:
           choice = int(input("\nYour answer (1-4):"))
           if 1 <= choice <= 4:
              break
          except ValueError:
           pass
          print("invalid input please enter 1-4")
       if options[choice-1] ==correct:
          print("✔️ correct")
          score +=1
       else:
          print(f"❌ wrong correct answer {correct}")
if __name__ == "__main__":
   run_quiz()