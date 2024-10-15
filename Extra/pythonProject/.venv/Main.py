import cv2
from PIL import Image

#image_path = 'cat.jpg'
#cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
#image = cv2.imread(image_path)
#cat_face = cat_face_cascade.detectMultiScale(image)
#print(cat_face)
#
#
#cat = Image.open(image_path)
#glasses = Image.open("glasses.png")
#
#cat = cat.convert("RGBA")
#glasses = glasses.convert("RGBA")
#
#for(x, y, w, h) in cat_face:
#    glasses = glasses.resize((w, int(h / 3)))
#    #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)
#    cat.paste(glasses, (x, int(y + h / 4)), glasses)
#    cat.save("cat_with_glasses.png")
#    cat_with_glasses = cv2.imread("cat_with_glasses.png")
#    cv2.imshow("cat_with_glasses.png", cat_with_glasses)
#cv2.imshow("cat", image)
#cv2.waitKey()

image_path = 'Blonde.png'
Eye_right_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')
Eye_left_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
image = cv2.imread(image_path)
RightEye = Eye_right_cascade.detectMultiScale(image)
LeftEye = Eye_left_cascade.detectMultiScale(image)

print(RightEye)


Blonde = Image.open(image_path)
Heart = Image.open("Heart.png")



Blonde = Blonde.convert("RGBA")
Heart = Heart.convert("RGBA")


for(x, y, w, h) in RightEye:
    Heart = Heart.resize((w + 70, int(h + 70)))
    Blonde.paste(Heart, (x - 40, int(y + h - 120)), Heart)
    Blonde.save("Blonde_with_heart_eyes.png")
    Blonde_with_heart_eyes = cv2.imread("Blonde_with_heart_eyes.png")
    cv2.imshow("Blonde_with_heart_eyes.png", Blonde_with_heart_eyes)
for(x, y, w, h) in LeftEye:
    Heart = Heart.resize((w * 2, int(h * 2)))
    Blonde.paste(Heart, (x - 230, int(y + h - 100)), Heart)
    Blonde.save("Blonde_with_heart_eyes.png")
    Blonde_with_heart_eyes = cv2.imread("Blonde_with_heart_eyes.png")
    cv2.imshow("Blonde_with_heart_eyes.png", Blonde_with_heart_eyes)



cv2.imshow("Blonde", image)
cv2.waitKey()