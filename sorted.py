# Learning git so this comment 
list=[4,5,3,89,70,34,56]
print(sorted(list))
print(sorted(list,reverse=True))

list_alphabet=['u','h','a','k','y']
print(sorted(list_alphabet))
print(sorted(list_alphabet,reverse=True))


string='python'
print(sorted(string))
print(sorted(string,reverse=True))

tuple=(5,6,3)
print(sorted(tuple))

dict=x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6}
print(sorted(dict))

set={1,2,4,3,2,8,8}
print(sorted(set))

l=["yrwuey",'jwqhegj','jhd','jhasd']
print("normal sort",sorted(l))
print("Sorted with key",sorted(l,key=len))

# key takes user defined functions as well
def funcc(x):
    return x % 7
l=[15,3,11,7]

print("Normal Sort",sorted(l))
print("sorted with key",sorted(l,key=funcc))

