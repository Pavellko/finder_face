import cv2
import os
import shutil

d=input("Введите каталог, где нужно определить лица: ")
ff=0
x = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
spisok=[]
vl=[]

for dirpath, dirnames, filenames in os.walk(d):
    for filename in filenames:
    	if "jpg" in filename or "jpeg" in filename:
            file_path = os.path.join(dirpath, filename)
            img = cv2.imread(file_path)
            # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            det = x.detectMultiScale(img, 1.1, 19)
            if len(det)==0:
                det_i=False
            else:
                det_i=True
            spisok.append([file_path, img, det, filename, dirpath, det_i])
            ff+=1

copy_path = dirpath+"/faces" 
copy_path_no = dirpath+"/no-faces" 
os.mkdir(copy_path)
os.mkdir(copy_path_no)

for ii in spisok:
    if ii[5]:
        # cv2.imshow('rez', ii[1])
        shutil.copyfile(ii[0] , copy_path+'/'+ii[3] )
    else:
        shutil.copyfile(ii[0] , copy_path_no+'/'+ii[3] )