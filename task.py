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


#1880_1
import sys 
input = [int(x) for x in sys.stdin.read().split()]

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
  nums.append(set(line.split()))
nums[1].intersection_update(nums[3])
nums[1].intersection_update(nums[5])
print(len(nums[1]))

#1025
import sys, math
input = [int(x) for x in sys.stdin.read().split()]
half = math.ceil(input[0]/2)
input.pop(0)
input.sort()
voters = 0
for x in range(0, half):
    voters+=math.ceil(input[x]/2)
print(voters)


#1020
import sys,math

def length(a, b):
    return math.sqrt(pow((b[0]-a[0]),2) + pow((b[1]-a[1]),2))

nums = []
for line in sys.stdin:
  nums.append([float(x) for x in line.split()])

#nails = nums[0][0]*nums[0][1]*1.57
nails = 2*3.14*nums[0][1]
rope = 0
for x in range(1, len(nums)):
    if x == len(nums)-1:
        rope += length(nums[1], nums[x])
        break
    rope +=length(nums[x], nums[x+1])
rope+=nails
print(format(rope, ".2f"))

#1209
import sys, math
input = [int(x) for x in sys.stdin.read().split()]

line = ""
for x in range(40):
    line+=str(pow(10,x))

for i in range(1, input[0]+1):
    print(line[input[i]-1], end =" ")
print()
for i in range(1, len(input)):
    if ((math.sqrt(8*int(input[i])-7) -1)/2)%1 == 0:
        print(1, end=" ")
    else:
        print(0, end=" ")

print()
print(input)
print(line)


#1100_1
import sys

nums = []

for line in sys.stdin:
  nums.append([int(x) for x in line.split()])

length = len(nums)
stop = 0 
for j in range(1, length):  
    for i in range(1, length-j):
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
"""