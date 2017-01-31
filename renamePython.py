"""
Ten program:
     Ung dung doi ten file_thu muc so luong lon:
     - Cac tinh nang:
         + doi ten file_folder theo y
         + doi ten hang loat theo number
         + doi duoi file (*.*)
         + phan loai file theo ext
     Tham so dau vao: Duong dan thu muc
     E:\MON HOC\TAI LIEU\TOPIC PRACTICE\PYTHON\BAI TAP
     Huong phat trien: Tu dong sap xep cac file vao thu muc
     dua vao ten.
     """

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
#tao thu vien class readDir
class readDir():
     pathDir=''
     nameFile=''
     def __init__(self,pathDir='',nameFile=''):
          self.pathDir=pathDir
          self.nameFile=nameFile
     def readListFile(self):
          listFile=os.listdir(self.pathDir)
          countFile=len(listFile)
          print ('Contanst:',countFile)
          print ('  ')
          i=0
          for i in range(countFile):
               print (listFile[i])

     def checkFile(self):
          listFile=os.listdir(self.pathDir+'\\')
          pathLink=self.pathDir + '\\'
          countFile=len(listFile)
          print ('File: ')
          for i in range(countFile):
               if os.path.isfile(pathLink + listFile[i]) == True:
                    print (listFile[i])
          print (' ')
          print ('Folder: ')
          for i in range(countFile):
               if os.path.isdir(pathLink + listFile[i]) == True:
                    print (listFile[i])

     def renameFile(self):
          listFile=os.listdir(self.pathDir)
          countFile=len(listFile)
          print ('Contanst:',countFile)
          print ('  ')
          i=0
          for i in range(countFile):
               if listFile[i].endswith('.pdf'):
                    os.rename(os.path.join(self.pathDir,listFile[i]),os.path.join(self.pathDir,self.nameFile+listFile[i]))

# su dung thu vien vua tao viet ham truyen thong so
class readMyDir(readDir):
     def readMyNameFile(self):
          print ('File name is ')
# ham lay duong path
def path_folder():
     duongdan=input('Hay Nhap Duong Dan:')
     return duongdan.strip()

# ham lay thong tin ve thu muc, file
def readListFile(pathDir):
          listFile=os.listdir(pathDir) # tra ve gia tri mang
          countFile=len(listFile) #dem so item trong thu muc
          print ('Total: ',countFile , 'Items')
          print ('  ')
          i=0
          for i in range(countFile):
               print (listFile[i])
          print ('\n')
# ham phan loai file _ folder
def checkFile(pathDir):
          listFile=os.listdir(pathDir)
          pathLink=pathDir + '\\'
          countFile=len(listFile)
          print ('File: ')
          for i in range(countFile):
               if os.path.isfile(pathLink + listFile[i]) == True:
                    print (listFile[i])
          print (' ')
          print ('Folder: ')
          for i in range(countFile):
               if os.path.isdir(pathLink + listFile[i]) == True:
                    print (listFile[i])
# ham nhap ten file can doi tên + nhap tên moi
def old_name():
     oldname=input('Tên File cu là: ')
     return oldname
def new_name():
     newname=input('Tên File moi là: ')
     return newname

#hàm nhập lựa chọn chức năng
def option():
    tinhnang=input('Hãy chọn tính năng tương ứng: '
          '\n'
          '1 - Show File/Folder Information'
          '2 - Rename one file/folder''\n'
          '3 - Rename multifile base on number''\n'
          '4 - Replace EXT'
          '\n')
    return tinhnang
# ham doi ten file
def rename(path,oldname,newname):
     os.rename(os.path.join(path,oldname),os.path.join(path,newname))
     if os.path.isfile(path + '//' + newname) == True:
         print('Success !!!')
     else:
         print('Unsuccess !!!')
# hàm truyền increase hay decrease
def typeRename():
    return input('Increase or Decrease ? 1/0 ')

# ham doi ten file
def renameMultiFileNumber(path,newname,startNumber,type):
    listFile=os.listdir(path) # tra ve gia tri mang
    countFile=len(listFile) #dem so item trong thu muc
    if type == '1':
        for i in range(countFile):
            count=i+ int(startNumber)
            os.rename(os.path.join(path,listFile[i]),os.path.join(path,newname + str(count)))
    if type == '0':
         for i in range(countFile):
            count=i+int(startNumber)
            os.rename(os.path.join(path,listFile[i]),os.path.join(path,newname + str(count)))

#hàm xác định EXT
def defineEXT(path):
     if os.path.isfile(path) == True:
         for i in range(len(path)):
             if path[i] == '.':
                 return path[i+1:len(path)]
def xulyOption(option):
    #Trường hợp show thông tin
    if option == '1':
        duongdan=path_folder()
        print ('Folder/File in ',duongdan,)
        readListFile(duongdan)
    #Trường hợp đổi tên file/folder
    if option == '2' :
        duongdan=path_folder()
        oldname=old_name()
        newname=new_name()
        rename(duongdan,oldname,newname)
    #Trường hợp đổi tên file/folder theo  number
    if option == '3':
         duongdan=path_folder()
         newname=new_name()
         type=typeRename()
         startNumber=input('Start = ')
         renameMultiFileNumber(duongdan,newname,startNumber,type)
    if option == '4' :
        duongdan=path_folder()
        listFile=os.listdir(duongdan) # tra ve gia tri mang
        countFile=len(listFile) #dem so item trong thu muc
        path = duongdan + "\\"
        arrayEXT=[]
        kt=0
        for i in range(countFile):
                kt=0
                if os.path.isfile(path +listFile[i] ) == True:
                    if len(arrayEXT) == 0:
                        arrayEXT.append(defineEXT(path + listFile[i]))
                    else:
                        for j in range(len(arrayEXT)):
                            if arrayEXT[j] == defineEXT(path + listFile[i]):
                                kt=1
                                break
                        if kt==0 :
                            arrayEXT.append(defineEXT(path + listFile[i]))
        print (arrayEXT)
        for j in range(len(arrayEXT)):
            print ('File with EXT ',arrayEXT[j],':')
            for i in range(countFile):
                if os.path.isfile(path +listFile[i] ) == True:
                    if defineEXT(path + listFile[i]) == arrayEXT[j] :
                        print (listFile[i])


def checkContinue():
        check=input('Go on action other? Y/N ')
        return check
#thuc thi
#my=readMyDir(duongdan)
#my.checkFile()
#my.renameFile()
#void main
def main():
    while True:
        print('Ứng dụng đổi tên file hoặc folder theo ý')
        opt=option()
        xulyOption(opt)
        check=checkContinue()
        if check == 'N' :
            break

main()

















