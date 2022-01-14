# (틀림)문제
# 길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다. 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다. 어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다. 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다. 그리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.

# 예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다. 하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.

# 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.

# 수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수열의 크기 N이 주어진다. N은 50보다 작은 자연수이다. 둘째 줄부터 N개의 줄에 수열의 각 수가 주어진다. 수열의 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

# 출력
# 수를 합이 최대가 나오게 묶었을 때 합을 출력한다. 정답은 항상 231보다 작다.

# ** 수 묶기의 규칙을 찾는 것이 중요
# 양수, 양수 = 곱셈
# 음수, 음수 = 곱셈
# 양수, 음수 = 덧셈

# 0, 양수 = 덧셈
# 0, 음수 = 곱셈

# 1, 양수 = 덧셈
# 1, 음수 = 덧셈
import sys

n = int(input())


number = [int(sys.stdin.readline()) for _ in range(n)]
number.sort(reverse=True)
negative = []
positive = []
one = []
result = 0

for x in number:
  if x > 1:
    positive.append(x)
  elif x <= 0:
    negative.append(x)
  else:
    one.append(x)
positive.sort(reverse=True)
negative.sort()

if len(positive) % 2 == 0:
  for x in range(0,len(positive),2):
    result += positive[x] * positive[x+1]
elif len(positive) == 1:
  result += positive[0]
else:
  for x in range(0,len(positive)-1,2):
    result += positive[x] * positive[x+1]
  result += positive[len(positive)-1]


if len(negative) % 2 == 0:
  for x in range(0,len(negative),2):
    result += negative[x] * negative[x+1]
elif len(negative) == 1:
  result += negative[0]

else:
  for x in range(0,len(negative)-1,2):
    result += negative[x] * negative[x+1]
  result += negative[len(negative)-1]



result += sum(one)

print(result)

