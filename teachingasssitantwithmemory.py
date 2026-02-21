import streamlit as st
import cohere
import config
import re 
import io  
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

def export_chat(history):
    text = ""
    for i, item in enumerate(history, 1):
        text += f"Q{i}: {item['question']}\n"
        text += f"A{i}: {item['answer']}\n\n"
    return io.BytesIO(text.encode("utf-8"))
if "history" not in st.session_state:
    st.session_state["history"] = []
st.set_page_config(page_title="Ai teaching assistant", layout="centered")
st.title("AI teaching Assistant (Cohere)")
st.write("Ask any question and get a complete structured answer")
col1, col2 = st.columns(2)
with col1:
    if st.button("Clear chat"):
            st.session_state.history = []
            st.rerun()
with col2:
    if st.session_state.history:
        st.download_button(
         "Export chat",
            data=export_chat(st.session_state.history),
            file_name="AI_CHAT_HISTORY.txt",
            mine="Text/plain"   
        )
question = st.text_input("Enter your question:", key="question_input")
if st.button("Ask"):
    q = question.strip()
    if q:
        with st.spinner("Generating complete answer"):
            answer = complete_answer(q)
        st.session_state.history.insert(0, {
            "question": q,
            "answer": answer
        })
        st.rerun()
    else:
        st.warning("Please enter a question")
st.markdown("Conversation history")
for i, item in enumerate(st.session_state.history, 1):
    st.markdown (f"**Q{i}: {item['question']}**")
    st.markdown(item['answer'])
    st.markdown("---")