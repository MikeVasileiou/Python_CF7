#Challenge No 1
#F
#aa
#ccc
#....

#(Factory)

message1 = "Factory" 

for i in range(len(message1)):
    print(message1[1] * (i + 1))


#Challenge No 2
#F******
#aa*****
#ccc****
#....***

for i in range(len(message1)):
    print(message1[i] * (i+1), end="*" * (len(message1) -i -1))
    print()