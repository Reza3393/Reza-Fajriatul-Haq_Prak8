import cv2
import matplotlib.pyplot as plt
from skimage.transform import swirl

# Load gambar
image = cv2.imread("Image/zee.jpeg")

# Konversi gambar ke skema warna RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Terapkan transformasi twirl pada gambar
swirled = swirl(image_rgb, rotation=0, strength=60, radius=500)

# Tampilkan gambar asli dan gambar hasil transformasi twirl
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3), sharex=True, sharey=True)
ax0.imshow(image_rgb)
ax0.axis('off')
ax1.imshow(swirled)
ax1.axis('off')
plt.show()