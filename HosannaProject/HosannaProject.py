import os


full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
# Python program to
# demonstrate merging
# of two files
  
data = data2 = ""

# Reading data from file1
with open(path+'\\FileChords\\abachuatrencao.txt',encoding="utf8") as fp:
    data = fp.read()
  
# Reading data from file2
with open(path+'\\FileChords\\tonvinhchiencon.txt',encoding="utf8") as fp:
    data2 = fp.read()

# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2

with open (path+'\\FileChords\\finalfiles.txt', 'w',encoding="utf8") as fp:
    fp.write(data)