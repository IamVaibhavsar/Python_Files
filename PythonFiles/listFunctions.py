numbers=[4,8,92,16,23,42,5]

friends =["suyash","krishna","vivek","Devashish","vinay","chalse","Aditya","suyash"]

print(friends)

friends.extend(numbers)
print(friends)

friends.append("harshal")
print(friends)

#friends.clear()
#print(friends)         empty list

friends.pop()
print(friends)      #last element removed

print(friends.index("suyash"))
print(friends.count("suyash"))

array=[23,86,65,2,65,23,48]
array.sort()
print(array)

array.reverse()
print(array)

array2=array.copy()
print(array2)


