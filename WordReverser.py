import streamlit as st

def reverse_each_word(sentence):
    words = sentence.split()
    reversed_words = [f"<span style='color:green; font-weight:bold;'>{word[::-1]}</span>" for word in words]
    return " ".join(reversed_words)

def reverse_word_order(sentence):
    words = sentence.split()[::-1]
    reversed_words = [f"<span style='color:blue; font-weight:bold;'>{word}</span>" for word in words]
    return " ".join(reversed_words)

def reverse_both(sentence):
    words = sentence.split()[::-1]
    reversed_words = [f"<span style='color:purple; font-weight:bold;'>{word[::-1]}</span>" for word in words]
    return " ".join(reversed_words)

# Streamlit UI
st.set_page_config(page_title="Reverse & Highlight", layout="centered")
st.title("🔁 Sentence Reverser with Highlights")

# Input
input_text = st.text_input("Enter a sentence (e.g., Sunrad makes solar simple):")

# Option
option = st.radio(
    "Choose how to reverse:",
    ["Reverse each word", "Reverse word order", "Reverse both"]
)

# Output
if input_text:
    st.markdown("### 🔍 Result with Visual Highlights:")
    if option == "Reverse each word":
        result = reverse_each_word(input_text)
    elif option == "Reverse word order":
        result = reverse_word_order(input_text)
    elif option == "Reverse both":
        result = reverse_both(input_text)

    st.markdown(f"<p style='font-size:1.3rem'>{result}</p>", unsafe_allow_html=True)
