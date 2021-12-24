n = int(input())
a1 = list(map(int,input().split())) 
a2 = list(map(int,input().split()))


a1.sort(reverse=True)
sum = 0

for k in range(n):
  sum += a1[k] * min(a2)
  del a2[a2.index(min(a2))]
  
print(sum)