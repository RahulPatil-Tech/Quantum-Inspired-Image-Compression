import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO


def run_quantum_compression(image_url, k_values):
    # 1. Load and Pre-process Image
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content)).convert(
        'L')  # Convert to Grayscale
    A = np.array(img, dtype=float) / 255.0  # Normalize to [0, 1]

    # 2. Perform SVD (The "Schmidt Decomposition")
    # A = U * S * Vt
    U, S, Vt = np.linalg.svd(A, full_matrices=False)

    # Setup plotting
    plt.figure(figsize=(15, 5))

    # 3. Apply Truncation for different K values
    for i, k in enumerate(k_values):
        # Truncate matrices to rank k
        U_k = U[:, :k]
        S_k = np.diag(S[:k])
        Vt_k = Vt[:k, :]

        # 4. Reconstruction (A_k)
        A_k = U_k @ S_k @ Vt_k

        # 5. Calculate Accuracy (Quantum Fidelity)
        error_norm = np.linalg.norm(A - A_k, ord='fro')
        original_norm = np.linalg.norm(A, ord='fro')
        accuracy = (1 - (error_norm / original_norm)) * 100

        # Plotting the results
        plt.subplot(1, len(k_values), i+1)
        plt.imshow(A_k, cmap='gray')
        plt.title(f"Rank k={k}\nAccuracy: {accuracy:.2f}%")
        plt.axis('off')

    plt.tight_layout()
    plt.show()


# --- EXECUTION ---
# OPTION A: Use a more reliable image URL
sample_url = "https://raw.githubusercontent.com/ieee8023/covid-chestxray-dataset/master/images/000001-1.jpg"

# OPTION B: Use a local file (Uncomment the line below and put an image in your folder)
# sample_url = "my_photo.jpg"

ranks_to_test = [5, 20, 50, 100]
run_quantum_compression(sample_url, ranks_to_test)
