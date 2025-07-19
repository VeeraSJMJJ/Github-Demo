import streamlit as st
import re

# --- Page config ---
st.set_page_config(page_title="Initials Highlighter Pro", layout="centered")

# --- Title ---
st.title("🌟 Animated Initial Highlighter Pro")
st.markdown("Customize highlight colors, fonts, animation, and more for names or sentences.")

# --- Input ---
input_text = st.text_input("Enter a full name or sentence:", "dr. a. p. j. abdul kalam is a legend.")

# --- Sidebar customization ---
st.sidebar.header("🎛️ Style Controls")

highlight_color = st.sidebar.color_picker("Highlight Color", "#00FF00")
background_color = st.sidebar.color_picker("Background Color", "#222222")
animate = st.sidebar.toggle("🎞️ Animate Initials", value=True)
capitalize = st.sidebar.toggle("🔤 Capitalize Initials", value=True)

font_size = st.sidebar.slider("Font Size (em)", min_value=0.8, max_value=3.0, step=0.1, value=1.5)
font_style = st.sidebar.selectbox("Font Style", ["normal", "italic", "oblique"])

# --- CSS Animation + Custom Styling ---
css = f"""
    <style>
    .highlight {{
        font-weight: bold;
        color: {highlight_color};
        background-color: {background_color};
        font-style: {font_style};
        font-size: {font_size}em;
        padding: 2px 4px;
        border-radius: 4px;
        {'animation: pulse 1.5s infinite;' if animate else ''}
        display: inline-block;
    }}

    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.25); }}
        100% {{ transform: scale(1); }}
    }}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# --- Highlighting Logic ---
def highlight_initials(text):
    words = text.strip().split()
    result = []

    for word in words:
        if not word:
            continue
        first = word[0].upper() if capitalize else word[0]
        rest = word[1:]
        html_word = f"<span class='highlight'>{first}</span>{rest}"
        result.append(html_word)

    return " ".join(result)

# --- Display Output ---
if input_text:
    highlighted_output = highlight_initials(input_text)
    st.markdown("### ✨ Result")
    st.markdown(f"<div>{highlighted_output}</div>", unsafe_allow_html=True)
