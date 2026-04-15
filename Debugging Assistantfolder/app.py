import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

# -------------------------------
# Sample "error database"
# (You can expand this later)
# -------------------------------
error_data = [
    {
        "error": "NullPointerException in Java",
        "solution": "Check if the object is initialized before using it. Use null checks."
    },
    {
        "error": "IndexOutOfBoundsException",
        "solution": "Ensure index is within array/list size."
    },
    {
        "error": "ModuleNotFoundError in Python",
        "solution": "Install the missing module using pip install <module-name>."
    },
    {
        "error": "Segmentation fault",
        "solution": "Occurs due to invalid memory access. Check pointers and array bounds."
    }
]

# -------------------------------
# Load embedding model
# -------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')

# -------------------------------
# Convert errors to embeddings
# -------------------------------
error_texts = [item["error"] for item in error_data]
error_embeddings = model.encode(error_texts)

# -------------------------------
# Function: Find similar error
# -------------------------------
def find_solution(user_error):
    user_embedding = model.encode([user_error])

    similarities = np.dot(error_embeddings, user_embedding.T).flatten()
    best_match_index = np.argmax(similarities)

    return error_data[best_match_index]

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🧠 AI Debugging Assistant")
st.write("Paste your error and get a solution instantly!")

user_input = st.text_area("Enter your error message:")

if st.button("Find Solution"):
    if user_input.strip() == "":
        st.warning("Please enter an error message.")
    else:
        result = find_solution(user_input)

        st.success("✅ Similar Error Found:")
        st.code(result["error"])

        st.info("💡 Suggested Solution:")
        st.write(result["solution"])
