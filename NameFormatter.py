import streamlit as st

# Common name prefixes
COMMON_TITLES = ["Mr.", "Ms.", "Mrs.", "Dr.", "Prof.", "Miss", "Mx.", "Sir", "Madam", "Rev."]

def parse_full_name(full_name):
    words = full_name.strip().split()

    # Check if the first word is a title
    title = ""
    if words and words[0].rstrip(".").capitalize() in [t.rstrip(".") for t in COMMON_TITLES]:
        title = words.pop(0)

    if len(words) < 2:
        return {"error": "Please enter at least first and last name."}

    first = words[0]
    last = words[-1]
    middle = " ".join(words[1:-1]) if len(words) > 2 else ""

    return {
        "Title": title,
        "First": first,
        "Middle": middle,
        "Last": last,
        "First Last": f"{first} {last}",
        "Last, First": f"{last}, {first}",
        "Initials": "".join([word[0].upper() for word in [first] + words[1:]]),
        "Uppercase": " ".join(words).upper(),
        "Lowercase": " ".join(words).lower(),
        "Abbreviated": f"{first[0].upper()}. {last.title()}",
        "Formal": f"{title} {first} {middle + ' ' if middle else ''}{last}".strip()
    }

# Streamlit UI
st.set_page_config(page_title="Name Formatter with Title", layout="centered")
st.title("🧾 Full Name Formatter with Title Support")

full_name = st.text_input("Enter your full name (e.g., Dr. John Michael Doe):")

if full_name:
    result = parse_full_name(full_name)

    if "error" in result:
        st.warning(result["error"])
    else:
        st.markdown("### ✨ Formatted Versions:")
        st.write(f"**Detected Title**: {result['Title'] or 'None'}")
        st.markdown(f"- **First Last**: {result['First Last']}")
        st.markdown(f"- **Last, First**: {result['Last, First']}")
        st.markdown(f"- **Initials**: {result['Initials']}")
        st.markdown(f"- **Uppercase**: {result['Uppercase']}")
        st.markdown(f"- **Lowercase**: {result['Lowercase']}")
        st.markdown(f"- **Abbreviated**: {result['Abbreviated']}")
        st.markdown(f"- **Formal (with title)**: {result['Formal']}")
