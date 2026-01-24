from openai import OpenAI
import config
import time
client = OpenAI(api_key=config.OPENAI_API_KEY)
def generate_response(prompt):
    """
    Generate AI response safely using OpenAI
    """
    try: 
        response = client.chat.completion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a helpful AI assistant"}
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return (
           "\n OpenAI error occured.\n"
           "please check API key or internet connection.\n"
        )
def silly_prompt():
    print("=" * 60)
    print(" AI PROMPT ENGINEERING TUTORIAL")
    print("Topic: CLarity, Specification & context")
    print("=" * 60)
    vague_prompt = input("\n Enter a VAGUE prompt (e.g., tell me about technology):")
    print("\n your vague prompt:", vague_prompt)
    print("\n AI response:")
    time.sleep(1)
    specific_prompt = input(
        "\n Make it MORE SPECIFIC (e.g., Explain how AI is used in education):"
    )
    print("\n Your specific prompt:", specific_prompt)
    print("\n AI response:")
    print(generate_response(specific_prompt))
    time.sleep(1)
    contextual_prompt = input(
        "\n Add context (role, audience, purpose): "
    )
    print("\n your contextual prompt:", contextual_prompt)
    print("Reflection questions")
    print("1 how did the response improve with specificality")
    print("2 how did context make the answer more useful")
    print("3 which prompt gave the best result and why")
    print("-" * 60)
if __name__ == "__main__":
    silly_prompt()