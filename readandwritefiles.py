#Create a file
fw=open('sample.txt','w') #prepare a file to be created... w means to write..if file is already there it will replace the file's contents
fw.write('Writing some stuff in my file \n') #\n means go to new line
fw.write('I like momo')
fw.close()

#Read from a file
fr=open('sample.txt','r')
text=fr.read()
print(text)
fr.close()

