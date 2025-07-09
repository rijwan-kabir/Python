print("Hello world","extra")
name='''Rijwan Kabir'''
age=22
print("My Name is ", name)

print(type(name))
print(type(age))

bl=True
m=None
print(type(bl),type(m))

print(2**5) #a^b

v1=True
v2=False
print(not False," ",v1 and v2," ", v1 or v2)

a=2
b=4.25
s="8"
print(a+b)
print(a+int(b))
print(a+int(s))

s=input("Enter the Number") #always take string
print(s)
n1=int(input("Enter the 1st num: "))
n2=int(input("Enter the 2nd Num: "))
print(n1+n2)

s1="Rijwan"
s2="Kabir"
print(s1+s2)
print(len(s1))
print(s1[1:3]) #[:4],,[2:]
print(s1[-6:-1])

print(s1.endswith("an")) #return true it ends with this char or string
print(s1.capitalize()) #return first word capital
print(s1.replace("wan","oan")) #replace this char or string
print(s1.find('a'))
print(s1.count('i'))

age=int(input("Enput the Age: "))
if(age<18):
    print("you are not eligible")
    print("keep growing")
elif(age>100):
    print("you are extra senior")
else:
    print("Congratulation")  
    print("you are Eligible")

if(age>=18):
    if(age>=80):
        print("Can't Drive")
    else:
        print("Can Drive")
else:
    print("Can't Drive")

list=["Rijwan",840,241,66] #list mutable(changable)---->string immutable
print(list,"->",list[0],"->",type(list),"->",len(list))
list[0]="Kabir"
print(list)
print(list[1:3]) #slicing or list[-3:-1]

lst=[2,1,3]
lst.append(4)  #add one element end
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True) #Descending order
print(lst)
lst.reverse()
print(lst)

lst.insert(0,100) #insert(idx,ele)
print(lst)
lst.remove(1) #remove first occurence of the list
print(lst)
lst.pop(0) #remove elem. at idx
print(lst) 

tuple=(1,2,3,3) #tuple immutable
print(tuple)
print(tuple.index(2)) #tup.index(ele) return indx number
print(tuple.count(3)) #Total occurence 

#Dictionary--->> unorder,mutable
dict={
    "name":"Rijwan",
    "cgpa":"3.92",
    "marks":[86,87,91],
    "is_valid":True,
    100.5:95.5
}
print(dict)
print(dict["name"])
dict["name"]="Kabir"
print(dict)

student={
    "name":"Rijwan",
    "score":{
        "phy":91,
        "cem":95,
        "math":97
    }
}
print(student)
print(student["name"])
print(student["score"]["phy"])
print(student.keys()) #return all dictionary keys
print(list(student.keys()))

print(student.values()) #return all vakues
pair=list(student.items()) #return (key,val) pairs as tuple
print(pair[0])

#print(student["Forcheck"])  #give error
print(student.get("Forcheck")) #give none, so it's use should be fine

student.update({"city":"Dhaka"})
print(student) 

collectionset={1,2,2,5,9,7,"hello","hello"} #set-->unique,sets(mutable),setElement(immutable),unorder
print(collectionset)
print(type(collectionset))
print(len(collectionset))

setcollection=set()

setcollection.add(100)
print(setcollection)
setcollection.remove(100)
print(setcollection)
setcollection.clear() #empties the set
setcollection.add(10)
setcollection.add(20)
print(setcollection)
setcollection.pop()
print(setcollection)

set1={1,2,3}
set2={3,4,5}
print(set1.union(set2)) #union
print(set1.intersection(set2)) #intersection 

sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print(sum)

i=1
while i<=10:
    if(i==2):
        print("Found")
        break
    else:
        print("Not Found")
        i+=1

i=1
while i<=3:
    if(i==2):
        i+=1
        continue
    else:
        print(i)
        i+=1 

str="Rijwan"
for char in str:
    if(char=='j'):
        print("j Found")
    else:
        print(char)

for el in range(5):
    print(el)

for el in range(1,10,2): #range(start,stop,step)
    print(el)

for i in range(5):
    pass
print("END")

