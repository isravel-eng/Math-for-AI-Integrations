# cayley_hamilton.py
import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Define Matrix ---
A = np.array([[2, 1],
              [1, 3]])

# --- Step 2: Characteristic Polynomial ---
char_poly = np.poly(A)  # Coefficients of λ^2 - 5λ + 5 = 0
print("Characteristic Polynomial Coefficients:", char_poly)

# --- Step 3: Verify Cayley–Hamilton Theorem ---
I = np.eye(A.shape[0])
lhs = np.polyval(char_poly, A)  # substitute A into its characteristic polynomial
print("\nA satisfies its own characteristic equation (should be near zero):")
print(lhs)

# --- Step 4: Diagonalization ---
eigvals, eigvecs = np.linalg.eig(A)
D = np.diag(eigvals)
P = eigvecs
P_inv = np.linalg.inv(P)
reconstructed = P @ D @ P_inv

print("\nReconstructed A (via diagonalization):\n", reconstructed)

# --- Step 5: Visualization ---
fig, ax = plt.subplots()
ax.quiver(0, 0, eigvecs[0, 0], eigvecs[1, 0], color='red', scale=1, angles='xy', scale_units='xy', label='Eigenvector 1')
ax.quiver(0, 0, eigvecs[0, 1], eigvecs[1, 1], color='blue', scale=1, angles='xy', scale_units='xy', label='Eigenvector 2')
ax.set_xlim(-1, 2); ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.legend(); ax.grid(True)
ax.set_title("Eigenvectors of A (Diagonalization)")
plt.savefig("outputs/Day02_eigenvectors.png", dpi=150)
plt.show()
