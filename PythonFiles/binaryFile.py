'''
binary is format of file where format is not made of readable characters.
in mode section, we have to specify the "+b" to open file binary mode
writes the array byte_arr to file "binary"
'''
f=open("binary.txt","w+b")
byte_arr=[120,3,255,0,100]
binary_format=bytearray(byte_arr)       #bytearray is used for convert string to bytes and returns new array of bytes.
f.write(binary_format)

f.close()


'''
Modes:
r:read only
rb:read in binary
r+:read and write
w:write
wb:write in binary
wb+:wb and reading
a:append
ab: append in binary
a+: append and reading
ab+:ab and reading
t: text mode
+:updating read and writing'''