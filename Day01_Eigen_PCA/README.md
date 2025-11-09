# Math for AI Integrations
# 01 — Eigenvalues, Eigenvectors & PCA

## Concept
Eigenvectors are directions unchanged by a linear transformation; eigenvalues are scalars that scale those directions.
PCA uses eigen-decomposition of the covariance matrix for dimensionality reduction.

## Notes / What I learned
- Understood how matrix transformations reshape vector spaces.
- Explored eigenvectors as directions that remain invariant under transformation.
- Connected basis, span, and null space to the structure of linear systems.
- Visualized eigenvalue properties and their role in dimensionality reduction (PCA).

## where i learned 
- For visualized study -  [3blue1brown - youtube video](https://www.youtube.com/watch?v=PFDu9oVAE-g&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=14) and that overall playlist for better understanding
- For theoretical study - [Prime newtons - youtube video](https://www.youtube.com/watch?v=QFgUHeUc_W0&list=PLql0qQWQbo6m0ltRGuqFGnJ83jYhyOMqm&index=6)
- For ideas , code - Chatgbt
- For doubts , understanomg the code - Grok
- Workout - VSCode 


## Files
- `eigen_demo.py` — visualizes eigenvectors and transformed unit circle.
- `pca_streamlit_app.py` — interactive app: upload CSV → run PCA → view 2D scatter and explained variance.

## How to run
1. `python eigen_demo.py`  (requires numpy, matplotlib)
2. `streamlit run pca_streamlit_app.py`  (requires scikit-learn, pandas, streamlit)


## Output
- `outputs/eigen_plot.png`
<img width="1371" height="1430" alt="image" src="https://github.com/user-attachments/assets/a8ef9abe-2f76-41ff-9c04-fc953932f609" />

- `outputs/getting_input_page.png`
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/094fad27-0573-4b1b-82b8-a33fc5790a09" />

- `outputs/output_page_part_1.png`
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b0cd740e-7ddb-4504-ba1b-7d2f31ec89d8" />

- `outputs/output_page_part_2.png`
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a0a3999c-3392-4491-ba7c-33fee3cfcdb1" />

- `outputs/total_output.png`

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/68f30eea-cbdc-4d93-b100-9e930cb26ddd" />


