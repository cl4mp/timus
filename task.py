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


#############
    INPUT
split() a string into a list, default separator is any whitespace

input() read from standard input, input type is a <string> by default

stdin internally calls input() and APPEND newline character
sys.stdin is a file-like object that can be read from using standard file i/o methods, such as read() readline() readlines()
sys.stdin.readline() <class str> //read a single line with a newline character at the end
sys.stdin.readlines() <class list> //read lines and return list of lines with a newline character at the end of each
sys.stdin.read() <class str> //read everything and return as one string->usefull for small data, big - use a lot of memory

for line in sys.stdin: <str>// will iterate through standard input until end-of-file is reached

#############

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



#1005
import sys

vec = [int(x) for x in sys.stdin.read().split()[1:]]

def recurs(vec, i, sum_cal, sum):
    if i == 0:
        return abs((sum - sum_cal)- sum_cal)
    return min(recurs(vec, i - 1, sum_cal + vec[i-1], sum), recurs(vec, i - 1, sum_cal, sum))

def driver(vec):
    return recurs(vec, len(vec), 0, sum(vec))

print(driver(vec))



#1014
import sys
data = int(sys.stdin.readline())
result = []
res = 0
if data in range(0, 10):
    if data == 0:
        res = 10
    else:
        res = data
else:
    x = 9
    while x > 1:
        if data % x == 0:
            data = data // x
            result.append(x)
            x  = 9
        else:
            x -= 1    
    if data != 1:
        res = -1         
    else:
        res = int(result[len(result)-1])
        for x in result[-2::-1]:
            res = res*10 + int(x)
#print(result)
print(res)



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



#1083
import sys

n, m = [x for x in input().split()]
x = int(n)
y = len(m)
if x % y == 0:
    last = y
else:
    last = x % y 

result = x

while x > last:
    x -= y
    result *= x
#result*= last
print(result)



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
    dict.update({str(x):[]}) #created a dictionary with value as list

def process(line):
    k = [x for x in line.split()]
    if len(k)!=1:
        dict[k[1]].append(k[0])

for line in sys.stdin:
    process(line)

for x, y in dict.items(): #items method returns a view object which contains the key-value pairs of the dictionary, as tuples in a list
    if y:
        for t in y:
            print(t, x)



#1110
import sys
data = [int (x) for x in sys.stdin.read().split()]
result = []
for i in range(0, data[1]):
    if i**data[0] % data[1] == data[2]:
        result.append(i)
if len(result) == 0:
    print(-1)
else:
    for r in result:
        print(r, end=' ')



#1120
f=int(input())

def res_a(x):
    rng = int((1 + (1+8*x)**(1/2))/2)
    for x in range(rng,0,-1):
        res = ((2*f)/x -x + 1)/2
        #print(f'isnise {x} & {res}')
        if res >=1 and res %1 == 0: 
            return x, int(res)
            break
res = res_a(f)
print(res[1], res[0])        
#1196
import sys
ll = set()
for i in range(int(sys.stdin.readline())):
    ll.add(sys.stdin.readline())
n = 0
for j in range(int(sys.stdin.readline())):
    if sys.stdin.readline() in ll:
        n += 1
print(n)



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



#1243
import sys
data = int(sys.stdin.readline())
print(data%7)



#1263
import sys

n, m = [int(x) for x in input().split()]
k = [0]*n

for i in range(m):
    x = int(input())
    k[x-1] += 1
for i in range(n):
    #print( "%.2f" % (k[u]*100/ m), "%", sep="" )
    print(f"{(k[i]*100/m):.2f}%")



#1264
import sys
data = [int(x) for x in sys.stdin.read().split()]
print(data[0]*(data[1]+1))



#1293
import sys

input  = [int(x) for x in sys.stdin.read().split()]

res = 1

for x in input:
    res*=x

print(res*2)



#1296
import sys
data = [int(x) for x in sys.stdin.read().split()]

all_max = 0
now_max = 0
for i in range(1,len(data)):
    now_max = now_max + data[i]
    if now_max < 0:
        now_max = 0
    if all_max < now_max:
        all_max = now_max
print(all_max)



#1313
import sys

a = int(input())
#print(f'This is input {a}')
matrix = [[0 for x in range(a)] for x in range(a)]
row = 0
for line in sys.stdin:
    nums = line.split()
    for i in range(a):
        #print(nums[i])
        matrix[row][i]=nums[i]
    row += 1
#print(matrix)

res =[]

res.append(matrix[0][0])
for i in range(1,a):
     k = 0
     for j in range(i,-1,-1):
          res.append(matrix[j][k])
          k += 1


m = 0
for j in range(1,a):
    k = j

    for i in range(a-1,m,-1):
        res.append(matrix[i][k])
        k += 1
    m += 1
for rs in res:
    print(int(rs), end=' ')



#1330
import sys 
inp = sys.stdin.read().split()

N = int(inp[0])
s = [0]*(N+1)
#adding element one by one
for i in range(1,N+1):
   k = int(inp[i])
   s[i] = s[i-1] + k

iter = N+2

while iter<len(inp):
   f, l = int(inp[iter]), int(inp[iter+1])
   sys.stdout.write('%s \n' % (s[l] - s[f-1]))
   iter += 2


   
#1409
import sys

input  = [int(x) for x in sys.stdin.read().split()]

print(input[1]-1, input[0]-1)



#1404
f = input()

my_dict = {}
my_dict2 ={}

lowercase_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
#print(lowercase_alphabet)

for index, element in enumerate(lowercase_alphabet):   
    my_dict[index] = element
for index, element in enumerate(lowercase_alphabet):   
    my_dict2[element] = index

old_lst =list(f)
lst =[]

for x in old_lst:
    lst.append(my_dict2[x])
#print(lst)
#lst = [23, 1, 3, 20, 24, 17]
#def step3(x):

len = len(lst)-1
#print(len)
result =[]
while len >= 1:
    if lst[len] < lst [len-1]:
        
        k = lst[len] + 26 - lst[len-1] 
        #print(k)
        len-=1
        result.append(k)
    else:
        k = lst[len] -lst[len-1] 
        #print(k)
        len-=1
        result.append(k)
if lst[0]<5:
    lst[0]+=26
result.append(lst[0]-5)       

for x in reversed(result):
    print(my_dict[x], end='')



#1496
import sys

data = [x for x in sys.stdin.read().split()]
res = set()
uniq = set()
for x in data:
    if x not in res:
        res.add(x)
    else:
        uniq.add(x)
            
#o(n^2)
#for x in data:
#    if data.count(x)>1:
#        res.add(x)
for l in uniq:        
    print(l)



#1585
import sys
e, m, l = 0, 0, 0
data = sys.stdin.readlines()

for item in data[1:]:
    if item[0] == 'E':
        e += 1
    elif item[0] == 'M':
        m += 1
    else:
        l += 1
if e > m:
    if l > e:
        print('Little Penguin')
    else:
        print('Emperor Penguin')
elif m > l:
    print('Macaroni Penguin')
else:
    print('Little Penguin')



#1785
n = int(input())
if n in range(1,5):
 print('few')
elif n in range(5,10):
 print('several')
elif n in range(10,20):
 print('pack')
elif n in range(20,50):
 print('lots')
elif n in range(50,100):
 print('horde')
elif n in range(100,250):
 print('throng')
elif n in range(250,500):
 print('swarm')
elif n in range(500,1000):
 print('zounds')
else:
 print('legion')

 

#1787
import sys

data = [int(x) for x in sys.stdin.read().split()]
res = 0
for x in range(data[1]):
    if res < 0:
        res = 0
    res += data[2+x]-data[0]
    if res < 0:
        res = 0
print(res)



#1820
a = [int(x) for x in input().split()]
if a[0]<=a[1]:
    print(2)
else:
    if (2*a[0]%a[1]) == 0:
        print(2*a[0]//a[1])
    else:
        print(2*a[0]//a[1]+1)



#1877
import sys
data = sys.stdin.read().split()

if data[1] >= '0001' and int(data[1]) % 2 != 0:
    print("yes")
elif data[0] >= '0002' and int(data[0]) % 2 == 0:
    print('yes')
else:
    print("no")



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



#1893
import re

pathD=input()
res=re.findall(r'[A-Z]|\d+',pathD) #\d+ matches 1-or-more digits 	| either smth or smth
a = res[1]
b = int(res[0])
if b in range(1,3):
    if a in {'A','D'}:
        print('window')
    else:
        print('aisle')

if b in range(3,21):
    if a in {'A','F'}:
        print('window')
    elif a in {'B','C','D','E'}:
        print('aisle')
    else:
        print('neither')

if b in range(21,66):
    if a in {'A','K'}:
        print('window')
    elif a in {'C','D','G','H'}:
        print('aisle')
    else:
        print('neither')



#1910
k = int(input())
ls = [int(x) for x in input().split()]
mid = 0
max = 0
for i in range(k-2):
    value = sum(ls[i:i+3])
    if value > max:
        max = value
        mid = i+2
print(max, mid)



#2001
import sys

data = [int(x) for x in sys.stdin.read().split()]
print(data[0]-data[4])
print(data[1]-data[3])



#2012
f=int(input())

prob = 12 - f
time = 4*60//45
if prob <= time:
    print("YES")
else:
    print("NO")



#2023
import sys
data = sys.stdin.read().split()

list1 = ["Alice", "Ariel", "Aurora", "Phil", "Peter", "Olaf", "Phoebus", "Ralph", "Robin"]
list2 = ["Bambi", "Belle", "Bolt", "Mulan", "Mowgli", "Mickey", "Silver", "Simba", "Stitch"]
list3 = ["Dumbo", "Genie", "Jiminy", "Kuzko", "Kida", "Kenai", "Tarzan", "Tiana", "Winnie"]
current = 1
steps = 0
for x in range(1,int(data[0])+1):
    if data[x] in list1:
        steps += abs(1 - current)
        current = 1
        continue
    if data[x] in list2:
        steps += abs(2 - current)
        current = 2
        continue
    if data[x] in list3:
        steps += abs(3 - current)
        current = 3
        continue

print(steps)



#2056
import sys
data = [int(x) for x in sys.stdin.read().split()]
sum = 0
for i in range(1, data[0]+1):
    sum+=data[i]
avg = 0
avg = sum /data[0]

if 3 in data[1:]:
    print("None")
elif (avg == 5):
    print("Named")
elif (avg >= 4.5):
    print("High")
else:
    print("Common")

    

#2066
import sys
data = [int(x) for x in sys.stdin.read().split()]
if (data[0] == data[1] == 0) or (data[0] == data[1] == 1) or (data[0] == 0 and data[1] == 1):
    print(data[0]-data[1]-data[2])
else:
    print(data[0]-(data[1]*data[2]))



#2100
import sys

data = [x for x in sys.stdin.read().split()]
persons = 2

for x in range(1, int(data[0])+1):
    if '+' in data[x]:
        persons+=2
    else:
        persons+=1
if persons == 13:
    print(1400)
else:
    print(persons*100)
"""





   


