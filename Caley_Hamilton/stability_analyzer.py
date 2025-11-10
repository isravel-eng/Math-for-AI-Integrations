# stability_analyzer.py
import numpy as np
import streamlit as st

st.title("🧮 RNN Weight Matrix Stability Analyzer")

st.markdown("""
Enter a 2×2 weight matrix.  
The app computes eigenvalues and reports whether the system is **Stable** (|λ| < 1) or **Unstable**.
""")

# --- Matrix input ---
a11 = st.number_input("a11", value=0.5, step=0.1)
a12 = st.number_input("a12", value=0.2, step=0.1)
a21 = st.number_input("a21", value=-0.1, step=0.1)
a22 = st.number_input("a22", value=0.8, step=0.1)

A = np.array([[a11, a12],
              [a21, a22]])

# --- Eigen computation ---
eigvals, eigvecs = np.linalg.eig(A)

st.write("### Eigenvalues:", np.round(eigvals, 3))

# --- Stability check ---
stable = np.all(np.abs(eigvals) < 1)

if stable:
    st.success("✅ Stable: all |λ| < 1")
else:
    st.error("⚠️ Unstable: some |λ| ≥ 1")

# --- Optional visualization ---
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
ax.add_artist(unit_circle)
ax.scatter(np.real(eigvals), np.imag(eigvals), color='blue', label='Eigenvalues')
ax.set_xlabel("Real(λ)"); ax.set_ylabel("Imag(λ)")
ax.set_aspect('equal'); ax.grid(True)
ax.legend(); ax.set_title("Eigenvalues in Complex Plane")
st.pyplot(fig)
