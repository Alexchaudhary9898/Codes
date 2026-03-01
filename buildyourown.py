import io
import re
import streamlit as st
import cohere
import config
co = cohere.Client(config.COHERE_API_KEY)
MATH_SYSTEM = """You are a math mastermind.
Solve with clear step by step reasoning. correct, and a final answer.
Verify when possible and mention an alternative method briefly if relevant."""
def generate(prompt, temperature=0.3, tokens=1000):
    try:
        r = co.chat(
            model = "c4ai-aya-expanse-8b",
            message =prompt,
            temperature=temperature,
            max_tokens=tokens
        )
        return r.text.strip()
    except Exception as e:
        return f"Error: {e}"
def looks_incomplete(text):
    return not text.strip().endswith((".","!", "?"))
def generate_complete(prompt, temperature, tokens):
    ans = generate(prompt, temperature, tokens)
    if looks_incomplete(ans):
      cont = generate(
        f"Continue from where you stopped. Do not repeat.\n\n{ans}",
        temperature,
        tokens
      )
      ans = ans + "\n" + cont
    return ans
def export_txt(history):
    txt = ""
    for i, h in enumerate(history, 1):
        txt += f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n"
    return io.BytesIO(txt.encode("utf-8"))
def run_ai_teaching_assistant():
    st.title("Ai teaching assistant")
    st.session_state.setdefault("history_ata",[])
    temp = st.slider("Creativity level", 0.0, 1.0, 0.3)
    tokens = st.slider("Max tokens (Response length)", 200, 2000, 1000)
    memory = st.checkbox("Enable Coversation memory", value=True)
    col1, col2 = st.columns([1, 2])
    if col1.button("Clear"):
        st.session_state.history_ata = []
        col2.download_button(
            "Export",
            export_txt(st.session_state.history_ata),
            "Teaching_assistant_chat.txt",
            "text/plain"
        )
    q = st.text_input("enter your password:")
    if st.button("Ask"):
        if not q.strip():
            st.warning("enter a question")
        else:
            with st.spinner("Thinking"):
                prompt = q
                if memory and st.session_state.history_ata:
                    previous = "\n".join(
                        [f"Q: {h['question']}nA: {h['answer']}"
                         for h in st.session_state.history_ata[:3]]
                    )
                    prompt = previous + "\nCurrent Question:" + q
                ans = generate_complete(prompt, temp, tokens)
            st.session_state.history_ata.insert(
                0, {"question": q.strip(), "answer": ans}
            )
            st.rerun()
    if not  st.session_state.history_ata:
        return
    st.markdown("### Conversation history")
    for i, h in enumerate(st.session_state.history_ata, 1):
        st.markdown(f"**Q{i}: {h['question']}**")
        st.markdown(h["answer"])
        if st.button(f"Regenerate Q{i}", key=f"regen_{i}"):
            new_ans = generate_complete(h["question"], temp, tokens)
            st.session_state.history_ata[i-1]["answer"] = new_ans
            st.rerun()
        st.markdown("---")
def run_math_mastermind():
    st.title("Math Mastermind")