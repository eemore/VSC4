# importing "array" for array creations
import array 
a=[1,'a string2',False] #list
b=('String',1,2.5,3)    #tuple
c={1,2,3,"Freedom"}               #set
d={"width":1, "length":2, "height":3}   #dict
e = array.array('i', [1, 2, 3]) #array.array

print('a[]',type(a))
print('b()',type(b))
print(r'c{}',type(c))
print(r'd{}',type(d))
print('e.array()',type(e))
print(a[1])
print(b[1])
#print(c[1]) set object not subscriptable
print(d)
print(d["width"])
print(e[0])
print(e[2])
for i in c:
    print(i)



