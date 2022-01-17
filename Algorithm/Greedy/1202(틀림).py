# **틀림 문제
# 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.

# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.

# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)

# 다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)

# 다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)

# 모든 숫자는 양의 정수이다.

# 출력
# 첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.

#heapq: 이진트리 기반의 최소 힙 자료구조.
import sys
import heapq

n, k = map(int,sys.stdin.readline().split())

bosuk = []
for _ in range(n):
  weight,price = map(int,sys.stdin.readline().split())
  heapq.heappush(bosuk,[weight,price])

bag = []

for _ in range(k):
  heapq.heappush(bag,int(sys.stdin.readline()))

print(bag)
guess = []
result = 0
for _ in range(k):
  a = heapq.heappop(bag) #왜이런건가 싶었는데 heap공식이있었음
  while bosuk and a >= bosuk[0][0]:
      [weight,price] = heapq.heappop(bosuk) #중요 문법!!
      heapq.heappush(guess,-price)
  if guess:
    result -= heapq.heappop(guess)
  elif not bosuk:
    break
print(result)





# n, k = map(int,sys.stdin.readline().split())

# jewel_line = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# bag_line = [int(sys.stdin.readline()) for _ in range(k)]
# bag_line.sort()
# price = sorted(jewel_line,key=lambda x:-x[1])

# result = 0

# for x in bag_line:
#   for j in range(n):
#     if(x >= price[j][0]):
#       n -= 1
#       result += price[j][1]
#       del price[j]
#       break;
# print(result)