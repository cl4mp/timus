"""
#binary search
#number to search
value = int(input())

mid = len(a) // 2
print(mid)
low = 0
max = len(a)-1
print(max)

while a[mid] != value and low <= max:
    if value > a[mid]:
        low = mid+1
    else:
        max = mid-1
    mid = (low + max) // 2

if low > max:
    print("No value")
else:
    print(mid)

    

#1000
import sys

val = [int (x) for x in sys.stdin.read().split()]

res = val[0] + val[1]

print(res)



#1001
import sys, math

val = [int (x) for x in sys.stdin.read().split()]

length = len(val)

for x in range(length-1, -1, -1):
    print(format((math.sqrt(val[x])), ".4f"))


    
#1020
import sys,math
def length(a, b):
    return math.sqrt(pow((b[0]-a[0]),2) + pow((b[1]-a[1]),2)) #length between 2 dots

nums = []
for line in sys.stdin:
  nums.append([float(x) for x in line.split()]) #add each line as list

#nails = nums[0][0]*nums[0][1]*1.57
nails = 2*3.14*nums[0][1] #circumference 2pr
rope = 0
for x in range(1, len(nums)):
    if x == len(nums)-1:
        rope += length(nums[1], nums[x])
        break
    rope +=length(nums[x], nums[x+1])
rope+=nails
print(format(rope, ".2f"))



#1025
import sys, math
input = [int(x) for x in sys.stdin.read().split()]
half = math.ceil(input[0]/2) #round a number upward to its nearest integer
input.pop(0) #removes the element at the specified position
input.sort() #sorts the list ascending by default
voters = 0
for x in range(0, half):
    voters+=math.ceil(input[x]/2)
print(voters)



#1068
import sys

val = [int (x) for x in sys.stdin.read().split()]

res = 0

if val[0] >= 1:
    for x in range(1, val[0]+1):
        res+=x
else:
    for x in range(val[0], 2):
        res+=x
print(res)



#1100_1
import sys

nums = []

for line in sys.stdin:
  nums.append([int(x) for x in line.split()])

length = len(nums)
stop = 0 
for j in range(1, length-1):  #biggest go to the end, comparing second-to-last
    for i in range(1, length-j): #length to work on -1 each time
        if nums[i][1]<nums[i+1][1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
            stop=1
    if stop == 0:
        break
for x in range(1, length):
    print(nums[x][0], nums[x][1])


#1100_2
import sys

dict ={}
for x in range(100,-1,-1):
    dict.update({str(x):[]})

def process(line):
    k = [x for x in line.split()]
    if len(k)!=1:
        dict[k[1]].append(k[0])
   # print(type(x))
    #print(x)

for line in sys.stdin:
   #print(type(line))
    process(line)
print(dict)
for x, y in dict.items():
    if y:
        for t in y:
            #print(type(t))
            print(t, x)



#1209
import sys, math
input = [int(x) for x in sys.stdin.read().split()]

#line = ""
#for x in range(40):
#    line+=str(pow(10,x)) #concatenating strings

#for i in range(1, input[0]+1):
#    print(line[input[i]-1], end =" ")
#print()

for i in range(1, len(input)):
    if ((math.sqrt(8*int(input[i])-7) -1)/2)%1 == 0: #sequence generalization
        print(1, end=" ") #by default print fn ends with a newline(\n), can end a print statement with any character/string
    else:
        print(0, end=" ")

print()
#print(input)
#print(line)


            
#1880_1
import sys 
input = [int(x) for x in sys.stdin.read().split()] #list comprehension
delim2 = input[0]+1
first = set(input[1:delim2])
delim1 = delim2+1
delim2 = delim1+input[delim2]
second = set(input[delim1:delim2])
delim1 = delim2+1
third = set(input[delim1:])
first.intersection_update(second)
first.intersection_update(third)
print(len(first))


#1880_2
import sys
nums = []
for line in sys.stdin:
  nums.append(set(line.split())) #appends an element to the end of the list, splits a string into a list where each word is a list item, set constructor
nums[1].intersection_update(nums[3], nums[5]) #removes the items that is not present in all sets
print(len(nums[1]))

"""