roll_no, marks, name = 10, 70, "Jessa"
a = b = c = 10

a = 10
b = 10
print(id(a))
print(id(b))

c = 20
d = 20
e = 20
print(id(c))
print(id(d))
print(id(e))
import sys
print(sys.getrefcount(a))
print(sys.getrefcount(c))

#packing
a = 10
b = 20
c = 20
d = 40
tuple1 = a, b, c, d # Packing tuple
print(t) # (10, 20, 20, 40)

#unpacking
tuple1 = (10, 20, 30, 40)  #remember lists use []
a, b, c, d = tuple1
print(a, b, c, d)  # 10 20 30 40