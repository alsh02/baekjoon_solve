# 1064번: 평행사변형
# 1. 세 점이 주어졌으므로 임의의 한 점에서 다른 두 점을 끝점으로 하는 벡터를 고려하자.
#   1-1. 만약 두 벡터외 외적의 값이 0이라면 평행사변형을 만들 수 없다. 바로 -1.0를 출력한다. 종료.
#   1-2. 그렇지 않다면 두 벡터의 크기의 합의 2배를 계산하여 만든 평행사변형의 둘레를 구한다.
# 2. 1단계에서 구한 평행사변형의 개수가 2개 이상인 경우 가장 큰 둘레값과 가장 작은 둘레값의 차를 계산하여 출력한다.
from math import sqrt

arr = list(map(int, input().split()))
points = [[arr[i], arr[i + 1]] for i in range(0, len(arr) - 1, 2)]
rounds = []

for i in range(3):
    start = points[i]
    idx = [0, 1, 2]

    idx.remove(i)
    ends = []
    for k in idx:
        ends.append(points[k])

    vectors = [[end[j] - start[j] for j in range(2)] for end in ends]
    cross = vectors[0][0] * vectors[1][1] - vectors[0][1] * vectors[1][0]
    if cross == 0:
        break

    norms = []
    for vector in vectors:
        n = sqrt(vector[0] ** 2 + vector[1] ** 2)
        norms.append(n)
    
    rounds.append(2 * sum(norms))

if len(rounds) != 3:
    print(-1.0)
else:
    print(max(rounds) - min(rounds))