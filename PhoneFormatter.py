import streamlit as st

st.set_page_config(page_title="📞 Phone Formatter", layout="centered")
st.title("📞 Format 10-digit Number")
st.markdown("Enter a 10-digit number and format it as `(XXX) XXX-XXXX`")

# Input
number = st.text_input("Enter a 10-digit number:", "9876543210")

# Format function
def format_phone(number):
    digits = ''.join(filter(str.isdigit, number))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    else:
        return None

# Output
if number:
    formatted = format_phone(number)
    if formatted:
        st.success(f"📞 Formatted: `{formatted}`")
    else:
        st.error("❌ Please enter a valid 10-digit number.")
