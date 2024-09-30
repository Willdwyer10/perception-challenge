import cv2
import numpy as np

# Load the image
image = cv2.imread('red.png')

# Convert image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define expanded HSV range for red cones
lower_red = np.array([175, 180, 100])  # Lower HSV bound for the red color
upper_red = np.array([180, 255, 255])  # Upper HSV bound for the red color

# Create a mask for the specified red color range
mask = cv2.inRange(hsv_image, lower_red, upper_red)

# Apply Gaussian Blur to reduce noise
blurred_mask = cv2.GaussianBlur(mask, (5, 5), 0)

# Find contours from the masked image
contours, _ = cv2.findContours(blurred_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Store the points of the cone positions
cone_positions = []

# Minimum and maximum contour area for filtering
min_contour_area = 300 # smallest cone is a bit less than 20x20
max_contour_area = 10000 # biggest cone is around 100x100

# Get the center of each cone
for contour in contours:
    if min_contour_area < cv2.contourArea(contour) < max_contour_area:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        # Find the center of the cone and add to positions
        cone_center = (x + w // 2, y + h // 2)
        cone_positions.append(cone_center)

# Sort the cones by y-coordinates to get left and right boundaries
cone_positions.sort(key=lambda point: point[1])

# Grab the two cones on the left side 
lower_left = cone_positions[0]
upper_left = cone_positions[-2]

# Width of the image
_, width, _ = image.shape

# Calculate a direction vector for the left line
dx_left = upper_left[0] - lower_left[0]
dy_left = upper_left[1] - lower_left[1]
slope_left = dy_left / dx_left

# calculate endpoints for line
x1 = 0
y1 = int(slope_left*(x1 - lower_left[0]) + lower_left[1])
x2 = width - 1
y2 = int(slope_left*(x2 - lower_left[0]) + lower_left[1])

cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 6)


# Grab the two cones on the right side 
lower_right = cone_positions[1]
upper_right = cone_positions[-1]

height, width, _ = image.shape

# Calculate a direction vector for the left line
dx_left = upper_right[0] - lower_right[0]
dy_left = upper_right[1] - lower_right[1]
slope_left = dy_left / dx_left

# calculate endpoints for line
x1 = 0
y1 = int(slope_left*(x1 - lower_right[0]) + lower_right[1])
x2 = width - 1
y2 = int(slope_left*(x2 - lower_right[0]) + lower_right[1])

cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 6)

# Save the final image with boundary lines
cv2.imwrite('answer.png', image)

print("Path boundary lines saved as 'answer.png'.")
