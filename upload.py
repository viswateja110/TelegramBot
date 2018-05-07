from ftplib import FTP
ftp=FTP("qpleaktest123.000webhostapp.com")
ftp.login(user='qpleaktest123',passwd='Teja1995')
ftp.cwd('/uploads')

def fileGrab():
    fileName='finalquestionpaper1.pdf.enc'
    localFile=open(fileName,'wb')
    ftp.retrbinary('RETR'+fileName,localFile.write,1024)
    ftp.quit()
    localFile.close()
def placeFile():
    fileName='finalquestionpaper1.pdf.enc'
    ftp.storbinary('STOR'+fileName,open(fileName,'rb'))
    ftp.quit()

placeFile()