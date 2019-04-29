employee_file=open("employee.txt","w")      #write mode- erases previous content

employee_file.write("David - Software Developer")

print(employee_file.readable())
#print(employee_file.read())

employee_file.close()

#David - Software Developer
# previous data and content is vanished