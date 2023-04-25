n, m, k = map(int, input().split(' '))

array = []
array += input().split()
cnt = 0
i = 0

array.sort(reverse=True)
print(array)
while m > k:
    cnt += int(array[i]) * k
    print(cnt, array[i], k)
    m -= k
    if array[i+1] != array[i]:
        continue
    else:
        i += 1
cnt += int(array[i+1]) * (m%k)

print(cnt)

