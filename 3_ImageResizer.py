import cv2


image = cv2.imread('yellow-smokes-iron-man-superhero-vlt40bbefkyi9cw5.webp')  # Replace with your image path

# Resize the image - specify width and height
new_width = 1920
new_height = 1080
resized_image = cv2.resize(image, (new_width, new_height))

# Display the original and resized images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

# Saving the resized image 
cv2.imwrite('resized_output.webp', resized_image)
print("Resized image saved as 'resized_output.webp'")
# Note: Ensure you have the necessary permissions to read/write files in the directory.