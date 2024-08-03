# 1065번: 한수
N = int(input())

ans = 0
for i in range(1, N + 1):
    arr = list(str(i))
    num_list = []
    
    for element in arr:
        num_list.append(int(element))
    
    if len(num_list) == 1 or len(num_list) == 2:
        ans += 1
    else:
        if 2 * num_list[1] == num_list[0] + num_list[2]:
            ans += 1

print(ans)