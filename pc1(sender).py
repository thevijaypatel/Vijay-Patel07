import ftplib
import os
def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
print("done")
ftp = ftplib.FTP("113.10.0.12")
print("enter username and password")
ftp.login("user1", "pass2")
upload(ftp, "uploading.txt")
