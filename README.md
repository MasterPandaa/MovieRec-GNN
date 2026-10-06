# 🎬 MovieRec-GNN — Movie Recommendation Engine

> **Graph Neural Network (GNN)** powered movie recommendation web application built with Flask and Python.

---

## 📌 Features
- **Graph-Based Recommendations**: Utilizes graph embeddings and topological relationships between users, genres, and movies.
- **Pre-trained Model**: Integrated with `movie_gnn_model.pkl` for fast, real-time inference.
- **Interactive Web Interface**: Clean web UI to explore movie suggestions and similarity scores.

---

## 🛠️ Tech Stack
- **Backend & ML**: Python, PyTorch Geometric / NetworkX, Scikit-Learn
- **Web Framework**: Flask
- **Deployment**: Procfile-ready for cloud deployment

---

## 🚀 Getting Started

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/MasterPandaa/MovieRec-GNN.git
cd MovieRec-GNN
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your browser.
