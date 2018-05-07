from __future__ import print_function
import random
import xlrd
import sys
import json
import pdfkit
from Crypto.Cipher import AES
from Crypto import Random
import os
class Encryption:
    def __init__(self,key):
        self.key=key
    
    def pad(self,s):
        return s + "\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, msg,key,key_size=256):
        msg=self.pad(msg)
        iv=Random.new().read(AES.block_size)
        cipher=AES.new(key,AES.MODE_CBC,iv)
        return iv+cipher.encrypt(msg)
    
    def encrypt_file(self,filename):
        with open(filename,'rb') as fp:
            data=fp.read()
        enc=self.encrypt(data,self.key)
        with open(filename+".enc","wb") as fp:
            fp.write(enc)
    def decrypt(self,cipherText,key):
        iv=cipherText[:AES.block_size]
        cipher=AES.new(key,AES.MODE_CBC,iv)
        data=cipher.decrypt(cipherText[AES.block_size:])
        return data.rstrip(b"\0")
    def decrypt_file(self,filename):
        with  open(filename,"rb") as fp:
            cipherText=fp.read()
        dec=self.decrypt(cipherText,self.key)
        with open(filename[:-4],"wb") as fp:
            fp.write(dec)
    
key=b'\xa4\xe4\xfe\xef7\xfe\xab\xd1\x92\x86\xa7\xfc\x9eM\xbe\xeb'
enc=Encryption(key)


listq=[]
def genPDF(l1,l2,l3):

    htmlstr="""
    <!DOCTYPE html>
    <html>
    <head>
    <title>question paper</title>
    </head>
    <style>
    p.small {
        line-height: 0.7;
    }

    p.big {
        line-height: 1.8;
    }
    </style>
        
    <body>


    <h3><pre>            Code no: R1621054                                               R16                                                    Set no: 1</pre></h3>
    <h4><center> II B. Tech I Semester Regular Examinations, October/November - 2018</h4>
    <h2><center> PYTHON PROGRAMMING</h2>
    <h5><center>(Com to CSE & IT)</h5>
    <h3><pre>            Time : 2 hours                                                                                                      Max marks : 50</pre></h3>
    <hr>
    <h3><pre>        Answer ALL the questions                                                                        Marks</pre> </h3>
            
    <br>
    <br>
    <center>
    <table>"""
    for i in range(len(l1)):
        htmlstr+="""
        <tr>
            <td>"""+str(i+1)+"""</td>
            <td>"""+l1[i]+"""</td>
            <td></td>
        </tr>"""
    
    for i in range(len(l2)):
        htmlstr+="""
        <tr>
            <td>"""+str(i+1)+"""</td>
            <td>"""+l2[i]+"""</td>
            <td></td>
        </tr>"""
    for i in range(len(l3)):
        htmlstr+="""
        <tr>
            <td>"""+str(i+1)+"""</td>
            <td>"""+l3[i]+"""</td>
            <td></td>
        </tr>"""


    htmlstr+="""</table>
        </center>
        </body>
        </html>"""
    with open("qgentemplate.html","w") as f:
        f.write(htmlstr) 
    pdfkit.from_file('qgentemplate.html','finalquestionpaper1.pdf')

def QuestionClassifier(quesList,mark):
    dist={}
    x=0
    for j in mark:
        classifiedList=[]
        for i in range(len(quesList)):        
            if quesList[i].get("marks")==j:
                classifiedList.append(quesList[i])
        x+=1
        listq.append(len(classifiedList))
        dist["sec"+str(x)]=classifiedList
    return (dist)
def getSection(section,no_of_section):
    data=set(section)
    return random.sample(data,no_of_section)
        
#starting point

#reading excel sheets from commandline arguments
xls=[sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]]
setques={}
setno=1
print("*"*20,"generating question paper")
for i in xls:
    wrkbook=xlrd.open_workbook(str(i))
    sheet=wrkbook.sheet_by_index(0)
    #print(sheet.cell_value(0,0))
    #print( sheet.nrows)
    #print (sheet.ncols)
    x=0

    tags=["Qno","question","marks","difficulty"]

    quesDictList=[]
 
    x=0
    for i in range(6,sheet.nrows):
        quesDict={}
        for j in range(0,sheet.ncols):
            quesDict[tags[j]]=(sheet.cell_value(i,j))
        
        quesDictList.append(quesDict)
    section=[]
    for i in range(len(quesDictList)):
        section.append(quesDictList[i].get("marks"))

    no_of_section=sheet.cell_value(4,1)
    
    marksec=getSection(section,int(no_of_section))

    randQuesList=QuestionClassifier(quesDictList,sorted(marksec))
    setques["set "+str(setno)]=randQuesList
    setno+=1

jsonOutput=json.dumps(setques)
print(jsonOutput)
listsam=[]
finalqList=[]

sec1ques=[]
sec2ques=[]
sec3ques=[]
for i in range(1,5):
    for j in range(1,int(no_of_section)+1):
        x=len(setques['set '+str(i)]['sec'+str(j)])
        listsam.append(x)
        #print(x)
        #print(setques['set '+str(i)]['sec'+str(j)][x].get('question').encode("utf-8"),end="\n\n\n")
        for y in range(x):
            if j==1:
                sec1ques.append(setques['set '+str(i)]['sec'+str(j)][y].get('question').encode("utf-8"))
            elif j==2:
                sec2ques.append(setques['set '+str(i)]['sec'+str(j)][y].get('question').encode("utf-8"))
            elif j==3:
                sec3ques.append(setques['set '+str(i)]['sec'+str(j)][y].get('question').encode("utf-8"))
            else:
                pass

        
    
#print(listsam)
for i in range(int(no_of_section)):
    finalqList.append(listsam[i]+listsam[i+3]+listsam[i+6]+listsam[i+9])
#print(sec1ques,end="\n\n\n")
#print(sec2ques,end="\n\n\n")
#print(sec3ques,end="\n\n\n")

list1 = sec1ques
list2 = sec2ques
list5 = sec3ques

newlist1=[]
temp=[]
el=[]
ol=[]

for i in reversed(list1):
    temp.append(i)
for i in range (0, int(len(temp)/2)):
    el.append(temp[2*i])
for i in range (0, int(len(temp)/2)):
    ol.append(temp[2*i+1])
for i in el:
    newlist1.append(i)
for j in ol:
    newlist1.append(j)



newlist2=[]
temp=[]
el=[]
ol=[]

for i in reversed(list2):
    temp.append(i)
for i in range (0, int(len(temp)/2)):
    el.append(temp[2*i])
for i in range (0, int(len(temp)/2)):
    ol.append(temp[2*i+1])
for i in el:
    newlist2.append(i)
for j in ol:
    newlist2.append(j)    



newlist5=[]
temp=[]
el=[]
ol=[]
for i in reversed(list5):
    temp.append(i)
for i in range (0, int(len(temp)/2)):
    el.append(temp[2*i])
for i in range (0, int(len(temp)/2)):
    ol.append(temp[2*i+1])
for i in el:
    newlist5.append(i)
for j in ol:
    newlist5.append(j)  
  



a = int(input("enter a number between 1 to 3: "))

finallist1=[]
finallist2=[]
finallist5=[]

for i in range (0, 5):
    k=(a+i*2)
    finallist1.append(newlist1[k])
    finallist2.append(newlist2[k])
for i in range (0,2):
    finallist5.append(newlist5[i])
genPDF(finallist1,finallist2,finallist5)
print("*"*20,"encrypting...")
enc.encrypt_file('finalquestionpaper1.pdf')
print("*"*20,"deleting original file...")
#os.remove('finalquestionpaper1.pdf')
print("*"*20,"paper generation completed")











           
