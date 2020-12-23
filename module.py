m = int(input())
n = int(input())

twod_list = []                                     
for i in range (0, m):                               
    new = []                 
    for j in range (0, n):  
        new.append(int(input()))       
    twod_list.append(new) 

print(type(twod_list))
print(twod_list)

anderson = []

for v in range(0,m):
	anderson += twod_list[v]

print(sum(anderson))