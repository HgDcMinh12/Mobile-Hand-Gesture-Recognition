import cv2
import os
import glob

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")
cv2.resizeWindow('test',1920,1080)
img_counter = 1

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 2)
    frame = cv2.rectangle(frame, (319, 49), (621, 351), (0, 255, 0), 1)
    cv2.imshow("test", frame)
    img = frame[50:351, 320:621]
    k = cv2.waitKey(1)
    keyname = chr(k%256)
    path = "./Data/{}".format(keyname)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k == -1:
        continue
    else:
        if os.path.isdir(path):
            if os.listdir(path):
                list_of_files = glob.glob(path+'/*')
                latest_file = max(list_of_files, key = os.path.getctime)
                img_counter = int(latest_file.split('.')[1].rsplit('\\')[1][1:])+1
                # print(img_counter)

            img_name = "{}/{}{}.png".format(path, keyname, img_counter)
            cv2.imwrite(img_name, img)
            print("{} written!".format(img_counter))
            img_counter += 1
        else:
            os.mkdir(path)

cam.release()

cv2.destroyAllWindows()
