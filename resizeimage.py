import cv2
image_path = 'download.jpg' 
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not load image.")
    exit()
new_width = 800
new_height = 600
resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
