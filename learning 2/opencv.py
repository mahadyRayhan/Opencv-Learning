# import the necessary packages
import imutils
import cv2
 
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("opencv_tutorial_load_image.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
 
# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
# =============================================================================
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# =============================================================================
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# =============================================================================
# roi = image[60:160, 320:420]
# cv2.imshow("ROI", roi)
# cv2.waitKey(0)
# =============================================================================
# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
# =============================================================================
# r = 300.0 / w
# dim = (300, int(h * r))
# resized = cv2.resize(image, dim)
# cv2.imshow("Aspect Ratio Resize", resized)
# cv2.waitKey(0)
# =============================================================================

# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
# =============================================================================
# resized = imutils.resize(image, width=300)
# cv2.imshow("Imutils Resize", resized)
# cv2.waitKey(0)
# =============================================================================
# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)