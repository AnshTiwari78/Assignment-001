M = int(input())
values = input()
N = int(input())
condii = 0
for i in range(len(values)):
    if values[i] != ',':
        if int() == N:
            print(int(i/2))
            condii=condii+1
            break
        i = i + 1
if condii==0:
    print("Better Luck Next Time")