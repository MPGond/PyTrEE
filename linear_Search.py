'''from pywebio.input import *
from pywebio.output import *
def linear_Search(list,key):
    for i in range(len(list)):
        if(key==list[i]):
            print("element found in the list at index:", i)
            break
    else:
        print("required element not found in the list")
list=[1,2,3,4,5,6]
key=int(input("enter the value of key:\t"))
linear_Search(list,key)'''
#Linear Search without Function
from pywebio.input import input, FLOAT
from pywebio.output import put_text
num=input("enter the desired element :",type=FLOAT)
list=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(list)):
    if num==list[i]:
        put_text("element is found")
        break
else:
    put_text("required element is not found")






