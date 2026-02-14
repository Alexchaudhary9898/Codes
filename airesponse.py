import cohere
import config
import time
co = cohere.Client(config.COHERE_API_KEY)
def generate_response(prompt, temperature =0.3, max_tokens = 400):
    """Generate AI response using Cohere"""
    try:
        response = co.chat(
            model = "c4ai-aya-expanse-8b",
            message=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
        )   
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"
def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===")
    prompt = input("Enter a prompt (e.g., Describe the ideal doctor): ").strip()
    if not prompt:
        print("prompt cannot be empty")
        return
    initial = generate_response(prompt)
    print("\nInitial AI Response:\n", initial)
    neutral = input("\nRewrite prompt in neutral form: ").strip()
    if neutral:
        improved = generate_response(neutral)
        print("\nNeutral AI Response:\n", improved)
    else:
        print("No Neutral prompt entered.")
def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===")
    long_prompt = input("Enter a long prompt: ").strip()
    if long_prompt:
        long_result = generate_response(long_prompt, max_tokens=800)
        preview = long_result[:500] + "...." if len(long_result) > 500 else long_result
        print("\nLong Prompt Response (Preview):\n", preview)
    else:
        print("Skipped long prompt")
    short_prompt = input("\nEnter condensed prompt: ").strip()
    if short_prompt:
        short_result = generate_response(short_prompt, max_tokens=250)
        print("Condensed prompt response", short_result)
    else:
        print("Skipped Condensed Prompt")
def main():
    while True:
        print("\n=== AI  PROMPT ENGINEERING PROJECT (Cohere)===")
        print("1 bias mitigation")
        print("2 token  limit test")
        print("3 Exit")
        choice = input("Choose (1-3):").strip()
        if choice == "1":
            bias_mitigation_activity()
        elif choice == "2":
            token_limit_activity()
        elif choice == "3":
            print("Exiting program")
            break
        else: 
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()