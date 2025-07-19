import streamlit as st

def main():
    st.set_page_config(page_title="Test Score Average Calculator", layout="centered")

    st.title("🎓 Test Score Average Calculator")

    st.write("Enter the scores for 5 tests below:")

    # Input fields for 5 test scores
    score1 = st.number_input("Test 1 Score", min_value=0, max_value=100, value=0)
    score2 = st.number_input("Test 2 Score", min_value=0, max_value=100, value=0)
    score3 = st.number_input("Test 3 Score", min_value=0, max_value=100, value=0)
    score4 = st.number_input("Test 4 Score", min_value=0, max_value=100, value=0)
    score5 = st.number_input("Test 5 Score", min_value=0, max_value=100, value=0)

    if st.button("Calculate Average"):
        scores = [score1, score2, score3, score4, score5]
        average = sum(scores) / len(scores)
        st.success(f"✅ Average Score: {average:.2f}")

        # Set the pass threshold
        pass_mark = 40.0

        if average >= pass_mark:
            st.markdown(f"### 🟢 Status: **Pass** 🎉")
        else:
            st.markdown(f"### 🔴 Status: **Fail** ❌")

if __name__ == "__main__":
    main()
