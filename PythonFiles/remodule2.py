import re
str='an example word:cat!!'

match=re.search(r'word:\w\w\w',str)     #r:raw string

if match:
    print("found")
else:
    print("Did not match")


#found