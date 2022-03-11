import cv2
import os
import shutil

d=input("Введите каталог, где нужно определить лица: ")
ff=0
x = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
spisok=[]


for dirpath, dirnames, filenames in os.walk(d):
    for filename in filenames:
    	if "jpg" in filename or "jpeg" in filename:
            file_path = os.path.join(dirpath, filename)
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
        shutil.copyfile(ii[0] , copy_path+'/'+ii[3] )
    else:
        shutil.copyfile(ii[0] , copy_path_no+'/'+ii[3] )