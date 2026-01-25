import time
import cohere
import config

co = cohere.Client(config.COHERE_API_KEY)

vvv
def generate_response(prompt, temperature=0.5):
    """
    Generate a response from Cohere Chat API with temperature control
    """
    try:
        response = co.chat(
            model="c4ai-aya-expanse-8b",   # ✅ verified working model
            message=prompt,
            temperature=temperature,
            max_tokens=300
        )
        return response.text.strip()

    except Exception as e:
        return f"Error generating response: {e}"


def temperature_prompt_activity():
    """
    Interactive activity to explore temperature & instruction-based prompts
    """
    print("=" * 80)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")
    print("=" * 80)

    print("\nIn this activity, we'll explore:")
    print("1. How temperature affects AI creativity and randomness")
    print("2. How instruction-based prompts control AI output")

    # ---------------- PART 1 ----------------
    print("\n" + "-" * 40)
    print("PART 1: TEMPERATURE EXPLORATION")
    print("-" * 40)

    base_prompt = input(
        "\nEnter a creative prompt "
        "(e.g., 'Write a short story about a robot learning to paint'): "
    )

    print("\n--- LOW TEMPERATURE (0.1) – Deterministic ---")
    print(generate_response(base_prompt, temperature=0.1))
    time.sleep(1)

    print("\n--- MEDIUM TEMPERATURE (0.5) – Balanced ---")
    print(generate_response(base_prompt, temperature=0.5))
    time.sleep(1)

    print("\n--- HIGH TEMPERATURE (0.9) – Creative ---")
    print(generate_response(base_prompt, temperature=0.9))

    print("\n" + "-" * 40)
    print("PART 2: INSTRUCTION-BASED PROMPTS")
    print("-" * 40)

    topic = input("\nChoose a topic (e.g., climate change, space exploration): ")

    instructions = [
        f"Summarize the key facts about {topic} in 3–4 sentences.",
        f"Explain {topic} as if I am a 10-year-old child.",
        f"Write a pros and cons list about {topic}.",
        f"Create a fictional news headline from the year 2050 about {topic}."
    ]

    for i, instruction in enumerate(instructions, start=1):
        print(f"\n--- INSTRUCTION {i} ---")
        print(instruction)
        print(generate_response(instruction, temperature=0.7))
        time.sleep(1)

    print("\n" + "-" * 40)
    print("PART 3: CUSTOM INSTRUCTION + TEMPERATURE")
    print("-" * 40)

    custom_instruction = input("\nEnter your own instruction-based prompt: ")

    try:
        custom_temp = float(input("Set a temperature (0.1 – 1.0): "))
        if not 0.1 <= custom_temp <= 1.0:
            raise ValueError
    except ValueError:
        print("Invalid input. Using default temperature 0.7.")
        custom_temp = 0.7

    print(f"\n--- RESPONSE (Temperature = {custom_temp}) ---")
    print(generate_response(custom_instruction, temperature=custom_temp))

    # ---------------- REFLECTION ----------------
    print("\n" + "-" * 40)
    print("REFLECTION QUESTIONS")
    print("-" * 40)
    print("1. How did temperature change creativity?")
    print("2. Which instruction gave the most useful output?")
    print("3. How would you apply temperature control in real applications?")
    print("4. Why are instruction-based prompts important?")


# ---------------- RUN ----------------
if __name__ == "__main__":
    temperature_prompt_activity()
