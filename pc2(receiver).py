import ftplib
import sys
def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print ("Error")
ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("user2", "pass2")
ftp.cwd('/project/')       
getFile(ftp,'uploading.txt')
ftp.quit()
