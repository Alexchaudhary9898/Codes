import streamlit as st
import cohere, config, io
co = cohere.Client(config.COHERE_API_KEY)
SYSTEM = """YOU ARE A MASTERMIND.
SHOW STEP BY STEP SOLUTION, REASONING, VERIFY ANSWER
FORMAT: PROBLEM >STEPS >FINAL ANSWER >CONCEPTS"""
def solve(problem, level):
    prompt = f"{SYSTEM}\n\nLevel: {level}\nProblem:{problem}"
    try:
        r = co.chat(
            model = "c4ai-aya-expanse-8b",
            message=prompt,
            temperature=0.1,
            max_tokens= 1000
        )
        return r.text.strip()
    except Exception as e:
        return f"Error :{e}"
def export(history):
    text = "\n\n".join(
        [f"Q{i}: {h['q']}\nA{i:} {h['a']}" for i, h in enumerate(history, 1)]
    )
    return io.BytesIO(text.encode())
st.set_page_config(page_title="Math mastermind", layout="centered")
st.title("math mastermind cohere")
st.session_state.setdefault("history",[])
c1, c2 = st.columns(2)
if c1.button("Clear"):
    st.session_state.history = []
    st.rerun()
if st.session_state.history:
    c2.download_button("Export", export(st.session_state.history),
                       "solutions.txt", "text/plain")
problem = st.text_area("Enter your math problem:")
level = st.selectbox("Level", ["Basic","Intermediate", "Advanced"])
if st.button ("Solve"):
    if problem.strip():
        with st.spinner("Solving"):
            ans = solve(problem, level)
        st.session_state.history.insert(0, {"q": problem, "a": ans})
        st.rerun()
    else:
        st.warning("Enter a problem first")
if st.session_state.history:
    st.markdown("### Solutions")
    for i, h in enumerate(st.session_state.history, 1):
        st.markdown(f"**Q{i}: {h['q']} ({level})**")
        st.markdown(h["a"])