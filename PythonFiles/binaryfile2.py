file=open("filename.pdf","wb")          #file to write to
file2=open("filename2.pdf","rb")        #file to read from

bin_cont=file2.read()
file.write(bin_cont)

file.close()
file2.close()