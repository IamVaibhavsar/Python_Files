employee_file=open("employee.txt","r")      #read mode
print(employee_file.readable())     #returns 1 if readable

print(employee_file.read())     #Read all data



'''True
Jim- Salesman
Mike- CEO
John - Manager
Kevin - Chairman
Steve - Accountant
'''

print(employee_file.readline())         #read only one line

#Jim- Salesman

print(employee_file.readlines()[1])     #read line whose index no.1

#True
#Mike- CEO

for emp in employee_file.readlines():           #read all data using for loop
    print(emp)

'''True
Jim- Salesman

Mike- CEO

John - Manager

Kevin - Chairman

Steve - Accountant'''

employee_file.close()