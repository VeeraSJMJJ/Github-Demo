import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="🔤 Caesar Shift Visualizer", page_icon="🔄", layout="centered")

# Page heading
st.markdown("""
# 🔠 Caesar Shift Visualizer  
Easily shift letters in your text by any number of positions in the alphabet.  
Highlights changed letters and supports dark mode!
""")

# UI Controls
dark_mode = st.toggle("🌙 Dark Mode")
highlight_color = st.color_picker("🎨 Pick Highlight Color", "#FF4B4B")
shift = st.slider("🔄 Shift Letters By", min_value=1, max_value=25, value=1)
text = st.text_input("✍️ Enter text to shift:", "Sunrad Renewable Energy!")

# CSS Styling
style = f"""
    <style>
    .highlight {{
        background-color: {highlight_color};
        padding: 1px 5px;
        border-radius: 4px;
        font-weight: bold;
        animation: fade 0.5s ease-in-out;
    }}
    @keyframes fade {{
        0% {{opacity: 0.3;}}
        100% {{opacity: 1;}}
    }}
    body {{
        background-color: {'#1e1e1e' if dark_mode else '#ffffff'};
        color: {'#ffffff' if dark_mode else '#000000'};
    }}
    </style>
"""
st.markdown(style, unsafe_allow_html=True)

# Caesar shift logic
def shift_char(c, s):
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base + s) % 26 + base)
    return c

def side_by_side(text, shift):
    rows = []
    for char in text:
        shifted = shift_char(char, shift)
        changed = char != shifted and char.isalpha()
        if changed:
            rows.append((char, f"<span class='highlight'>{shifted}</span>"))
        else:
            rows.append((char, char))
    return rows

# Display results
if text:
    result = side_by_side(text, shift)

    original = ''.join([char for char, _ in result])
    shifted_html = ''.join([shifted for _, shifted in result])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📄 Original Text")
        st.code(original, language='text')
    with col2:
        st.markdown("### ✨ Shifted & Highlighted")
        st.markdown(shifted_html, unsafe_allow_html=True)
