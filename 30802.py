# 30802번: 웰컴 키트
N = int(input())
tshirts = list(map(int, input().split()))
T, P = map(int, input().split())

t_bundle = 0
for tshirt in tshirts:
    bundle = 0
    if tshirt != 0:
        if tshirt > T:
            bundle += tshirt // T
            
            if tshirt % T != 0:
                bundle += 1
        else:
            bundle += 1

    #print(f"신청수: {tshirt}, 필요한 묶음수: {bundle}")
    t_bundle += bundle
        
print(t_bundle)
print(N // P, N % P)