# 🧠 AI Debugging Assistant (RAG + Vector Search using Endee)

## 📌 Project Overview
The AI Debugging Assistant is a smart tool that helps developers quickly resolve coding errors by leveraging semantic search and Retrieval-Augmented Generation (RAG).

Users can input an error message, and the system retrieves the most relevant similar errors along with suggested solutions.

This project demonstrates the use of modern AI infrastructure including vector databases, embeddings, and semantic similarity.

---

## 🚀 Features
- 🔍 Semantic search for error messages
- 🧠 AI-powered debugging suggestions
- ⚡ Fast and lightweight interface using Streamlit
- 📂 Easily extendable with real-world datasets
- 🔗 Built with vector database concepts using Endee

---

## 🏗️ System Architecture

1. User inputs an error message
2. Error text is converted into embeddings
3. Embeddings are stored/retrieved using vector database (Endee)
4. Similar errors are found using cosine similarity
5. Relevant solution is returned to the user

---

## 🧰 Tech Stack

- Python
- Streamlit (UI)
- Sentence Transformers (Embeddings)
- NumPy (Similarity Calculation)
- Endee (Vector Database)

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
