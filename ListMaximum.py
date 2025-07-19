import streamlit as st
import statistics
import pandas as pd
import matplotlib.pyplot as plt

def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

def find_smallest(numbers):
    smallest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
    return smallest

st.set_page_config(page_title="Number Stats & Visualization", layout="centered")
st.title("📊 Number Analyzer: Find Largest + Stats + Chart")

# Input
input_text = st.text_input("🔢 Enter numbers separated by commas (e.g., 10, 5, 20, 8):")

if st.button("Analyze"):
    try:
        # Convert to list of floats
        numbers = [float(num.strip()) for num in input_text.split(",") if num.strip() != '']
        if not numbers:
            st.warning("⚠️ Please enter at least one number.")
        else:
            # Calculations
            largest = find_largest(numbers)
            smallest = find_smallest(numbers)
            mean_val = statistics.mean(numbers)
            median_val = statistics.median(numbers)
            sorted_numbers = sorted(numbers)

            # Display sorted list with highlight
            st.markdown("### 🔢 Sorted Numbers (ascending):")
            highlighted = [
                f"**:green[{num}]**" if num == largest else f"{num}"
                for num in sorted_numbers
            ]
            st.markdown(" | ".join(highlighted))

            # Display stats
            st.markdown("---")
            st.markdown("### 📈 Basic Statistics")
            st.write(f"✅ **Largest**: {largest}")
            st.write(f"🔻 **Smallest**: {smallest}")
            st.write(f"➗ **Mean**: {mean_val:.2f}")
            st.write(f"🧮 **Median**: {median_val}")

            # Bar Chart
            st.markdown("---")
            st.markdown("### 📊 Bar Chart of Entered Numbers")
            df = pd.DataFrame({'Index': list(range(1, len(numbers)+1)), 'Value': numbers})
            fig, ax = plt.subplots()
            bar_colors = ['green' if val == largest else 'blue' for val in numbers]
            ax.bar(df['Index'], df['Value'], color=bar_colors)
            ax.set_xlabel("Index")
            ax.set_ylabel("Value")
            ax.set_title("Bar Chart of Input Numbers")
            st.pyplot(fig)

    except ValueError:
        st.error("❌ Invalid input! Please enter only numbers separated by commas.")
