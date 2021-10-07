import os

arr=[]

f1 = open("c:\목록.txt", 'r')
while 1:
    line = f1.readline()
    if not line: break
    arr.append(line)
f1.close()

i=0
while i<len(arr):
    if "https://" in arr[i]:
        arr[i] = arr[i].replace("https://","")
    else:
        arr[i] = arr[i].replace("http://","")
    i=i+1

j=0
while j<len(arr):
    if "/" in arr[j]:
        arr[j] = arr[j].replace("/","")
    j=j+1

k=0
while k<len(arr):
    if "www." in arr[k]:
        arr[k] = arr[k].replace("www.","")
    k=k+1

print(arr)

f2 = open("c:\새목록.txt", "w")
for n in arr:
    f2.write(n)
f2.close()

os.startfile("c:\새목록.txt")