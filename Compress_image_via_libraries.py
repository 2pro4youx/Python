from skimage import io
import numpy as np
import matplotlib.pyplot as plt
# Load grayscale image into 2D matrix
image = io.imread('sample.jpg', as_gray=True)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')
plt.show()
# Perform SVD factorization
U, S, VT = np.linalg.svd(image, full_matrices=False)
# Keep top K=50 singular values for low-rank reconstruction
K = 50
compressed_image = np.dot(U[:, :K], np.dot(np.diag(S[:K]), VT[:K, :]))
plt.imshow(compressed_image)
plt.title(f'Compressed Image with K={K} Singular Values')
plt.axis('off')
plt.show()