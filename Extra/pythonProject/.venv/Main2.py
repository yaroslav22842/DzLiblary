import cv2
from PIL import Image
image_path = 'Man.png'
Eye_right_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')
Eye_left_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
image = cv2.imread(image_path)
RightEye = Eye_right_cascade.detectMultiScale(image)
LeftEye = Eye_left_cascade.detectMultiScale(image)

print(RightEye)


Man = Image.open(image_path)

Man = Man.convert("RGBA")



for(x, y, w, h) in RightEye:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 128, 0), 3)
for(x, y, w, h) in LeftEye:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 128, 0), 3)


cv2.imshow("Man", image)
cv2.waitKey()