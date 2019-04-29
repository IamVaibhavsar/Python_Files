import re

email_add= "please contact me at vaibhavbhavsar007@gmail.com"
new_email_add=re.sub(r'([\w\.-]+)@([\w\.-]+)',r'vaibhavbhavsar007@gmail.com',email_add)

print(new_email_add)

#please contact me at vaibhavbhavsar007@gmail.com

