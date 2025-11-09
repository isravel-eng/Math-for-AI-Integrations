# pca_streamlit_app.py
import streamlit as st
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

st.title("PCA Visualizer — Day 1")

uploaded = st.file_uploader("Upload CSV (numeric columns only)", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.write("Preview:", df.head())
    X = df.select_dtypes(include=['number']).dropna(axis=1)
    n_components = st.slider("n_components", min_value=1, max_value=min(5, X.shape[1]), value=2)
    pca = PCA(n_components=n_components)
    Xp = pca.fit_transform(X)
    st.write("Explained variance ratio:", pca.explained_variance_ratio_)
    fig, ax = plt.subplots()
    ax.scatter(Xp[:, 0], Xp[:, 1])
    ax.set_xlabel("PC1"); ax.set_ylabel("PC2")
    st.pyplot(fig)
else:
    st.info("Upload a small numeric CSV (e.g., iris.csv) to test.")
