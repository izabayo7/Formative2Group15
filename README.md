# Machine Learning Project: Matrix Operations and PCA on African Dataset

## Overview

This project is structured into **three phases** and demonstrates key linear algebra and machine learning techniques in Python. It includes:

1. A custom Python library for matrix multiplication (`group15multiplyingmatrices`)
2. Implementation of **Principal Component Analysis (PCA)** on an African dataset
3. Manual computation of **eigenvalues** and **eigenvectors**

The goal of this project is to build core ML capabilities from scratch, enhance mathematical intuition, and apply PCA for dimensionality reduction and data interpretation.

---

## Project Structure

```
project-root/
│
├── group15multiplyingmatrices/
│   └── matrix.py         # Custom matrix multiplication logic
│
├── pca/
│   ├── african_dataset.csv  # African dataset used in PCA
│   └── pca_analysis.py      # PCA implementation and visualization
│
├── eigen/
│   └── eigen_calc.pdf     # Manual computation of eigenvalues/vectors
│
└── README.md             # Project documentation
```

---

## Phase 1: Matrix Multiplication Library

### Module: `group15multiplyingmatrices`

This custom library implements basic matrix multiplication without using external libraries like NumPy.

**Features:**

* Input validation
* Multiplication of 2D matrices
* Clean API for reuse

**Usage Example:**

```python
from group15multiplyingmatrices.matrix import multiply_matrices

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = multiply_matrices(A, B)
print(result)
```

---

##  Phase 2: Principal Component Analysis (PCA)

###  Module: `pca/pca_analysis.py`

PCA is implemented to analyze and reduce dimensionality of a real-world African dataset.

**Key Steps:**

* Data normalization
* Covariance matrix calculation
* Eigen decomposition
* Projection to lower dimensions
* Data visualization (2D plot)

**Libraries Used:**

* `pandas`, `numpy`, `matplotlib`, `seaborn`

**Run:**

```bash
python pca/pca_analysis.py
```

> 📌 Dataset: A CSV file containing socio-economic indicators across African countries.

---

## Phase 3: Eigenvalue and Eigenvector Computation

###  Module: `eigen/eigen_calc.py`

Eigenvalues and eigenvectors are computed manually from the covariance matrix to demonstrate understanding beyond library usage.

**Methods Include:**

* Characteristic polynomial generation
* Solving polynomial for eigenvalues
* Finding eigenvectors by solving `(A - λI)v = 0`

**Note:** While `numpy.linalg` is used for verification, all core steps are computed manually.

---

##  Requirements

Install dependencies with:

```bash
pip install alumathvanguard
```


---



## Contributors

* Group 15 – Machine Learning Team
* Edith Githinji
* Cedric Ibitayo
* Eliel Ntwali
* Samuel Wanjohi

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 📌 Acknowledgments

Special thanks to our mentors/coach (Marvin)  who supported this exploration into machine learning fundamentals.
