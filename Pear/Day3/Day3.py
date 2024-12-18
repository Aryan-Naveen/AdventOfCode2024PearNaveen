f = open('Input3.txt')
data = f.read()
index_m = data.find ("mul(")
index_c = data.find ("," , index_m)
index_p = data.find(")" , index_m)
multnumber = 0
finalnumber = 0
active = True

while index_m != -1 and index_c != -1 and index_p != -1:
    value1 = data[index_m +4 :index_c]
    value2 = data[index_c +1: index_p]
    do = data.rfind("do()" , 0, index_m)
    dont = data.rfind("don't()" , 0, index_m)
    if do > dont:
        active = True
    elif do < dont:
        active = False
    if active == True and (value1.isdigit() and value2.isdigit()):
        multnumber = int(value1) * int(value2)
    else:
        multnumber = 0
    finalnumber += multnumber
    data = data[index_m + 1:]
    index_m = data.find ("mul(")
    index_c = data.find ("," , index_m)
    index_p = data.find(")", index_m)

print (finalnumber)




#figure out where index m and index c and index p 
#check to see if there is an m left, comma left, and closing paranthesis , index_m and index_c and index_p != -1
#retrieve the numbers in the parenthsis -> value1 = data[index mul + 4:index_c] value2 = data[index_c + 1: index_p]
#find the most recent do and don't. do = data.rfind("do" , 0 , index_m) dont = data.rfind("don't", 0, index_m)
#if do > dont: 
# active = true
#elif dont < do:
# active = false
# if active and (value1 isdigit and value2 is digit) then mult number = int(value 1) * int(value 2)
#final number += mult number
#change data to data[1+indexm:]
#recalcualting the indexes the while loop


