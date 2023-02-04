import cv2

img = cv2.imread("PRO-104-Project-Image-main/solar-system.jpg")

cv2.putText(img,'Sun', (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255) )
cv2.putText(img, 'Mercury', (110, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'Venus', (190, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'Earth', (290, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, 'Mars', (375,150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, 'Jupiter', (550, 100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, 'Saturn', (750, 115), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, 'Uranus', (975, 115), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, 'Pluto', (1100, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.imshow('output', img)



cv2.waitKey(0)

