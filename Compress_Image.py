import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=5 #scalar

#shifting
identity=np.eye(len(A))
print("Shifted Matrix (+): \n", A+B*identity)
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# Load an image and convert to grayscale
image = io.imread('sample.jpg', as_gray=True)

# Perform Singular Value Decomposition (SVD)
U, S, Vt = np. linalg. svd(image, full_matrices=False)

# Compress image by keeping only the first 'k' singular values
k = 50 # Number of singular values to keep
compressed_image = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))

# Show original and compressed images
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image, cmap='gray')
axes [0].set_title("Original Image")
axes [1]. imshow(compressed_image, cmap='gray')
axes[1].set_title(f"Compressed Image (k={k})")
plt.show()