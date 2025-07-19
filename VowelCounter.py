import streamlit as st
import pandas as pd

def count_individual_vowels(text):
    vowels = "aeiou"
    text = text.lower()
    counts = {v: text.count(v) for v in vowels}
    return counts

def count_total_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def highlight_vowels(text):
    vowels = "aeiouAEIOU"
    highlighted = ""
    for char in text:
        if char in vowels:
            highlighted += f"<span style='color: green; font-weight: bold;'>{char}</span>"
        else:
            highlighted += char
    return highlighted

st.set_page_config(page_title="Advanced Vowel Counter", layout="centered")
st.title("🔡 Advanced Vowel Counter")

input_text = st.text_input("Enter a word or sentence:")

if input_text:
    total_vowels = count_total_vowels(input_text)
    vowel_counts = count_individual_vowels(input_text)
    total_chars = len(input_text.replace(" ", ""))  # Exclude spaces
    vowel_percentage = (total_vowels / total_chars) * 100 if total_chars > 0 else 0

    # Highlight vowels in text
    st.markdown("### 🖍️ Text with Highlighted Vowels:")
    st.markdown(
        f"<p style='font-size: 1.2rem;'>{highlight_vowels(input_text)}</p>",
        unsafe_allow_html=True
    )

    # Show counts
    st.markdown("### 🧮 Vowel Statistics")
    st.write(f"✅ Total Vowels: **{total_vowels}**")
    st.write(f"📊 Vowel Percentage: **{vowel_percentage:.2f}%** (excluding spaces)")

    # Show breakdown in table
    st.markdown("### 🔍 Vowel Breakdown Table:")
    df = pd.DataFrame(vowel_counts.items(), columns=["Vowel", "Count"])
    st.dataframe(df.set_index("Vowel"))

    # Show bar chart
    st.markdown("### 📉 Vowel Count Bar Chart:")
    st.bar_chart(df.set_index("Vowel"))
