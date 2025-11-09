# eigen_demo.py
import numpy as np
import matplotlib.pyplot as plt

# --- Matrix A ---
A = np.array([[2, 1],
              [1, 2]])

# --- Compute Eigenvalues & Eigenvectors ---
eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)

# --- Plot Setup ---
fig, ax = plt.subplots(figsize=(8, 8))
origin = np.zeros(2)

# --- Plot SCALED Eigenvectors (length = eigenvalue) ---
for i in range(eigvecs.shape[1]):
    vec = eigvecs[:, i]                    # normalized eigenvector
    scaled_vec = eigvals[i] * vec          # scale by eigenvalue
    ax.quiver(*origin, *scaled_vec,
              angles='xy', scale_units='xy', scale=1,
              color='black', width=0.005,
              label=f'v{i+1}, λ={eigvals[i]:.1f}')

# --- Plot Unit Circle and Transformed Circle ---
theta = np.linspace(0, 2 * np.pi, 200)
circle = np.vstack((np.cos(theta), np.sin(theta)))        # unit circle
transformed = A @ circle                                  # A(unit circle)

ax.plot(circle[0, :], circle[1, :], 'b--', linewidth=1.5, label='Unit Circle')
ax.plot(transformed[0, :], transformed[1, :], 'orange', linewidth=2, label='A(unit circle)')

# --- Styling ---
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10, loc='upper left')
ax.set_title("Eigenvectors (scaled by λ) and A(unit circle)", fontsize=14, pad=15)
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)
ax.set_xlabel('x')
ax.set_ylabel('y')

# --- Save & Show ---
plt.savefig("outputs/eigen_plot_scaled.png", dpi=200, bbox_inches='tight')
plt.tight_layout()
plt.show()