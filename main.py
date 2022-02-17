import cv2
#reading image
img = cv2.imread("Assets/babies.jpg")
# img = cv2.imread("Assets/christmasSam.jpg")
# img = cv2.imread("Assets/nub.jpg")

# converting BGR image to grayscale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#image inversion
invertedImg = 255 - grayImg

# cv2.imshow("original", grayImg)
# cv2.imshow("invertegd", invertedImg)

# get the blurred image and its inverse
blurredImg = cv2.GaussianBlur(invertedImg, (21, 21), 0)
inverted_blurred = 255 - blurredImg

# vars for scales for different images
babiesScale = 200
christmasScale = 125
nubScale = 150

# divide the two images
pencil_sketch = cv2.divide(grayImg, inverted_blurred, scale=babiesScale)



cv2.imshow("Original Image", img)
cv2.imshow("Pencil Sketch of Dog", pencil_sketch)
cv2.waitKey(0)

cv2.destroyAllWindows()

# save the resulting image
cv2.imwrite("Result/result.jpg", pencil_sketch)
