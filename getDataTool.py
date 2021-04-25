import cv2
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 2)
    frame = cv2.rectangle(frame, (319, 49), (621, 351), (0, 255, 0), 1)
    cv2.imshow("test", frame)
    img = frame[50:351, 320:621]
    k = cv2.waitKey()
    keyname = chr(k%256)
    path = "D:/UIT/HKII_2020_2021/Nhan dang/getDataTool/Data/{}".format(keyname)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    else:
        if os.path.isdir(path):
            img_name = "{}/{}{}.png".format(path, keyname, img_counter)
            cv2.imwrite(img_name, img)
            print("{} written!".format(img_name))
            img_counter += 1
        else:
            os.mkdir(path)

cam.release()

cv2.destroyAllWindows()