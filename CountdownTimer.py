import streamlit as st
import time

st.set_page_config(page_title="Countdown Timer", layout="centered")
st.title("⏱️ Custom Countdown Timer")

# Input: Let user choose countdown time
countdown_time = st.number_input("Enter countdown time (in seconds):", min_value=1, max_value=3600, value=10, step=1)

# Start button
if st.button("Start Countdown"):
    countdown_placeholder = st.empty()

    for i in range(countdown_time, -1, -1):
        mins, secs = divmod(i, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        countdown_placeholder.markdown(f"## ⏳ Countdown: `{time_str}`")
        time.sleep(1)

    # Display message and play sound
    st.success("⏰ Time's up!")
    st.balloons()

    # Optional: Play a beep sound using HTML (note: some browsers may block it)
    st.markdown(
        """
        <audio autoplay>
            <source src="https://www.soundjay.com/button/beep-07.wav" type="audio/wav">
        </audio>
        """,
        unsafe_allow_html=True
    )
