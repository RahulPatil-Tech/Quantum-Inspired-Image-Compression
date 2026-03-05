# Quantum-Inspired Image Compression

![Python](https://img.shields.io/badge/Python-3.12-blue)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-orange)
![SciPy](https://img.shields.io/badge/SciPy-Linear%20Algebra-green)
![Domain](https://img.shields.io/badge/Domain-Biomedical%20Imaging-red)
![Research](https://img.shields.io/badge/Field-Quantum%20Information-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

This project explores the application of **Singular Value Decomposition (SVD)** to digital image processing, framing matrix factorization as a **Schmidt Decomposition of a composite quantum system**.

---

## 🏥 Why Biomedical?

Medical imaging techniques such as **MRI** and **CT scans** generate massive volumes of data. Efficient compression is essential for:

- Storage optimization
- Faster transmission
- Maintaining diagnostic image quality

This project demonstrates how **Quantum-Inspired truncation of singular values** can compress images while preserving clinically important structures.

---

## 🚀 Key Features

### Quantum Representation
Treats a **2D image matrix** as a **state vector in a composite Hilbert space**, analogous to quantum systems.

### High Efficiency
Keeping only the **top ~20% of singular values** can preserve **>90% structural accuracy**.

### Noise Reduction
Shows how the **essential structure ("quantum essence")** of an image becomes clearer as low-importance singular values (noise / decoherence) are removed.

---

## 🛠️ Tech Stack

**Language**
- Python 3.12

**Libraries**
- NumPy – High-dimensional matrix operations
- SciPy – Numerical linear algebra and optimization

---

## 📊 Results Summary

Example results using a **512 × 512 image matrix**:

| Components (k) | Compression Ratio | Accuracy | Visual Quality |
|---------------|------------------|---------|---------------|
| Original | 1:1 | 100% | Perfect |
| 100 | 2.5:1 | 96.81% | Very High |
| 50 | 5.1:1 | 94.01% | Good |
| 10 | 25:1 | ~80% | Low |

---

## 💻 How to Run

```python
from scipy import linalg
import numpy as np

# Core compression function
def compress_image(image_matrix, k):
    U, s, Vt = linalg.svd(image_matrix, full_matrices=False)
    s_k = np.diag(s[:k])
    return np.dot(U[:, :k], np.dot(s_k, Vt[:k, :]))
```

### Usage Example

```python
compressed_image = compress_image(image_matrix, k=50)
```

Where:

- `image_matrix` = grayscale image converted to a NumPy array  
- `k` = number of singular values retained  

---

## 🧠 Conceptual Background

Singular Value Decomposition can be interpreted through a **quantum information perspective**:

| Linear Algebra | Quantum Interpretation |
|----------------|-----------------------|
| Image Matrix | Quantum State |
| SVD | Schmidt Decomposition |
| Singular Values | Entanglement Spectrum |
| Truncation | Decoherence / Noise Removal |

This provides an interesting bridge between **quantum information theory** and **classical signal processing**.

---

## 📜 References

1. Nielsen, M. A., & Chuang, I. L. (2010).  
   *Quantum Computation and Quantum Information.*

2. Strang, G. (2022).  
   *Introduction to Linear Algebra.*

---

## 👨‍💻 Author

**Rahul Patil**

Field:
- Quantum Information  
- Data Science
