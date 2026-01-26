import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    with open('movie_gnn_model.pkl', 'rb') as f:
        data = pickle.load(f)
    return data['df'], data['vectors'], data['map']

df, vectors, movie_map = load_model()

# --- SYSTEM LOGIC (Sama seperti yang kita buat) ---
def recommend(history_titles, top_k=5):
    if not history_titles: return []
    
    # Ambil vector dari history
    indices = [movie_map[t] for t in history_titles if t in movie_map]
    if not indices: return []
    
    user_vec = np.mean(vectors[indices], axis=0).reshape(1, -1)
    sims = cosine_similarity(user_vec, vectors).flatten()
    
    # Hapus yg sudah ditonton
    sims[indices] = -1
    
    recs_idx = sims.argsort()[-top_k:][::-1]
    return df.iloc[recs_idx]

# --- USER INTERFACE ---
st.title("🎬 Movie GNN RecSys")
st.write("Sistem Rekomendasi Film Cerdas berbasis Graph Neural Network")

# Sidebar: Simulasi User
st.sidebar.header("User Activity")
selected_movies = st.sidebar.multiselect(
    "Film yang sudah Anda tonton:",
    options=df['Title'].values
)

if st.sidebar.button("Reset History"):
    selected_movies = []

# Main Area
tab1, tab2 = st.tabs(["🔥 Rekomendasi Untukmu", "🔍 Cari Film"])

with tab1:
    if selected_movies:
        st.subheader(f"Karena kamu menonton: {', '.join(selected_movies[:2])}...")
        recs = recommend(selected_movies)
        
        cols = st.columns(5)
        for idx, row in enumerate(recs.itertuples()):
            with cols[idx]:
                st.info(f"⭐ {row.Rating}")
                st.write(f"**{row.Title}**")
                st.caption(f"{row.Genres}")
    else:
        st.info("Pilih film di sidebar untuk mendapatkan rekomendasi personal!")

with tab2:
    genre = st.selectbox("Pilih Genre", df.explode('Genre_List')['Genre_List'].unique())
    res = df[df['Genres'].str.contains(genre)].sort_values('Popularity', ascending=False).head(10)
    st.dataframe(res[['Title', 'Genres', 'Rating', 'Country']])