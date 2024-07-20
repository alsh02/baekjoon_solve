# 1064번: 평행사변형
# 1. 세 점이 주어졌으므로 임의의 한 점에서 다른 두 점을 끝점으로 하는 벡터를 고려하자.
#   1-1. 만약 두 벡터 사이의 각이 180도라면 평행사변형을 만들 수 없다. 바로 -1.0를 출력한다. 종료.
#   1-2. 두 벡터 사이의 각이 180도가 아닌 경우라면 점 D는 1단계에서 고른 한 점에서 뻗은 각이등분선과 다른 두 점을 이은 대각선의 교점과 점 대칭을 이루는 위치에 존재한다.
# 2. 1단계에서 점 D를 구한 경우(1-2), 1단계에서 구한 두 벡터의 합의 2배를 계산하여 만든 평행사변형의 둘레를 구한다.
# 3. 2단계에서 구한 평행사변형의 개수가 2개 이상인 경우 가장 큰 둘레값과 가장 작은 둘레값의 차를 계산하여 출력한다.
from math import acos, sqrt, degrees

arr = list(map(int, input().split()))
points = [[arr[i], arr[i + 1]] for i in range(0, len(arr) - 1, 2)]

for i in range(3):
    start = points[i]
    idx = [0, 1, 2]

    idx.remove(i)
    ends = []
    for k in idx:
        ends.append(points[k])

    vectors = [[start[j] - end_point[j] for j in range(2)] for end_point in ends]
    
    norms = []
    for vector in vectors:
        norms.append(sqrt(vector[0] ** 2 + vector[1] ** 2))
    
    product_norm = norms[0] * norms[1]
    dot = vectors[0][0] * vectors[1][0] + vectors[0][1] * vectors[1][1]

    angle = degrees(acos(dot / product_norm))
    
    
