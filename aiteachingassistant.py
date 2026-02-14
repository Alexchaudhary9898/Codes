import streamlit as st
import cohere
import config
import re   
co = cohere.Client(config.COHERE_API_KEY)
def ai(prompt, tokens = 800):
    try:
        r = co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            temperature= 0.3,
            max_tokens=tokens
        )
        return r.text.strip()
    except Exception as e:
        return f"Error: {e}"
def incomplete(text):
    return not text.strip().endswith((".","!","?"))
def complete_answer(q):
    prompt = f"Answer clearly in numbered points.\n\nQuestion: {q}"
    ans = ai(prompt)
    if incomplete(ans):
        cont = ai(f"Continue the answer without repeating.\n\n{ans}")
        ans = ans + "\n" + cont
    return ans
st.title("AI Teaching assistant (Cohere)")
st.write("Ask any question and get a complete structured answer")
question = st.text_input("Enter your question:")
if question:
    st.markdown(f"**Question:**{question}")
    answer = complete_answer(question)
    st.markdown("**Answer:**")
    st.markdown(answer)
else:
    st.info("Please enter a question")