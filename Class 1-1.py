
import cv2
import random
import time
import dropbox

starttime=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videocap=cv2.videoCapture(0)
    result=True
    while(result):
     ret,frame=videocap.read()
     print(ret)
     imgname="img"+str(number)+".png"
     cv2.imwrite(imgname,frame)
     result=False
    return imgname
    print("Snapshot Taken.")

    videocap.release()
    cv2.destroyAllWindows()
    
def upload_file(imgname):
    access_token='sl.BKr4VtEPGhnJ4upLuQE_rlyZIT_vNI_mrACUSVyvo-Csda0h3RZEMdWkFVEUNHQ8A4DN4k9Z83UJb6hSXq3MexwmxnmkKO9bBbXsQkiEQbsD8bTTSrTWnd-yXJL6_aSuM2MR6DoohgXe'   
    file=imgname
    file_from=file
    file_to="/python/"+(imgname)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)

def main():
    while(True):
        if ((time.time()- starttime) >= 300):
         name = take_snapshot()
         upload_file(name)
main()
