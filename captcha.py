import cv2
import pytesseract
import numpy as np

# Load image
img = cv2.imread("captcha.png")

# Resize (helps OCR accuracy)
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur to remove salt-and-pepper noise
blur = cv2.medianBlur(gray, 3)

# Threshold using Otsu
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Morphological operations to reduce noise further
kernel = np.ones((2, 2), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Invert back to black text on white background
final = cv2.bitwise_not(morph)

# Save steps for inspection
cv2.imwrite("step1_gray.png", gray)
cv2.imwrite("step2_blur.png", blur)
cv2.imwrite("step3_thresh.png", thresh)
cv2.imwrite("step4_morph.png", morph)
cv2.imwrite("step5_final.png", final)

# OCR using Tesseract
config = "--oem 3 --psm 8"  # Treat as a single word
text = pytesseract.image_to_string(final, config=config)

print("🧠 Detected CAPTCHA:", text.strip())
