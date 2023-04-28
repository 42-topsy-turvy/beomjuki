n = int(input())
l = list(map(int, input().split()))
ans = 0
print(l)

l.sort()
print(l)
#3면
l3 = l[:3]
print(l3)
ans += sum(l3) * 4

#2면
l2 = l[:2]
print(l2)
ans += sum(l2) * (n-1) * 4 + sum(l2) * 4 * (n-2)

#1면
l1 = l[:1]
print(l1)
ans += sum(l1) * (n-1) * (n-2) * 4 + sum(l1) * (n-2) * (n-2)

'''
#0면
l0 = l[:0]
ans += sum(l0) * (n-2) * (n-2) * (n-1)
'''

print(ans)

#아직 미완성
