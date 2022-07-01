import cv2
import numpy


img = cv2.imread("Question2/sample.png")
imgs = cv2.resize(img, (960, 540)) 

hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lower = numpy.array([0, 50, 50])
upper = numpy.array([10, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

cv2.imwrite('Question2/result.png', mask)



# Tested here
# hsv_sml is to use csv imshow for mask
hsv_sml  = cv2.cvtColor(imgs, cv2.COLOR_BGR2HSV)

# mask_sml is to use csv imshow for mask
mask_sml = cv2.inRange(hsv_sml, lower, upper)


# Tested before creating result.png
cv2.imshow("Image", imgs)
cv2.imshow("Mask", mask_sml)


cv2.waitKey(0)
cv2.destroyAllWindows()
