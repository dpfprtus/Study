# 문제
# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

# 입력
# 첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
n, m = map(int, input().split())
graph1 = []
graph2 = []
count = 0

def convertgraph(i, j):			# 3x3을 뒤집는 함수
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            graph1[x][y] = 1 - graph1[x][y]


for i in range(n):				# 변환 전 함수 입력
    graph1.append(list(map(int, input())))

for i in range(n):				# 변환 후 함수 입력
    graph2.append(list(map(int, input())))

for i in range(n - 2):
    for j in range(m - 2):
        if graph1[i][j] != graph2[i][j]: # 일치하지 않는 부분 발생
            convertgraph(i, j)			 # 뒤집고
            count += 1				 	 # 횟수 + 1
flag = 0							# 변환 할 수 있는지 나타내는 변수

for i in range(n):					# 변환 후 일치하는지 확인
    for j in range(m):
        if graph1[i][j] != graph2[i][j]:
            flag = 1
            break

if flag == 1:							# 변환이 불가능 하면 -1 반환
    print(-1)
else:
    print(count)


# n,m = map(int,input().split())

# graph = [list(map(int,input())) for _ in range(n)]
# graph1 = [list(map(int,input())) for _ in range(n)]
# count = 0

# def reverse(x,j):
#   for k in range(x,x+3):

#     for t in range(j,j+3):
#       if graph[k][t] != graph1[k][t]:
#         graph[k][t] = 1 - graph[k][t]

  

# for x in range(n-2):
#   for j in range(m):
#     if graph[x][j] != graph1[x][j]:
#       reverse(x,j)
#       count +=1

# flag = 0
# print(graph)
# print(graph1)

# for x in range(n):
#   for j in range(m):
#     if graph[x][j] != graph1[x][j]:
#       flag = 1
#       break

# if flag == 1:
#   print(-1)
# else:
#   print(count)

