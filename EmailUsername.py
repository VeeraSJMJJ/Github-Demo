import streamlit as st

st.set_page_config(page_title="📧 Email Username Extractor", layout="centered")
st.title("📧 Extract Username from Email Address")
st.markdown("Enter email addresses to extract usernames. We'll keep a history of all during this session.")

# Initialize session state list
if "history" not in st.session_state:
    st.session_state.history = []

# Input
email = st.text_input("Enter email address:", "sunrad@example.com")

# Username extraction function
def extract_username(email):
    if "@" in email:
        return email.split("@")[0]
    return None

# Process and store history
if email:
    username = extract_username(email)
    if username:
        st.success(f"🧑‍💻 Username: `{username}`")
        if username not in st.session_state.history:
            st.session_state.history.append(username)
    else:
        st.error("❌ Invalid email format. Please include '@'.")

# Display session history
if st.session_state.history:
    st.markdown("### 📜 Session History")
    for i, user in enumerate(st.session_state.history, 1):
        st.markdown(f"{i}. `{user}`")

# Optional: clear history
if st.button("🧹 Clear History"):
    st.session_state.history.clear()
    st.success("Session history cleared.")
