M=(input())
values=input()
str = ' '
i=0
list = []
sum=0
for i in values:
    if(i==';'):
        list.append(str)
        str = ' '
    else:
        str = str+i
if(str!=';'):
    list.append(str)
for i in range(len(list)):
    list[i] = int(list[i])

    i = i+1
for j in list:
    sum = sum+j
print(sum)