#버블정렬
def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1): #index 는 0부터 시작이니 index가 n-1 이면 마지막 원소고, range는 -1된거까지니, n-2 인거 까지 돌아가는 것임
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#삽입정렬
def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

#선택정렬
def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

#병합 정렬

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = arr[:mid]
    high_arr = arr[mid:]

    # low_arr와 high_arr를 각각 재귀호출하여 정렬
    merge_sort(low_arr)
    merge_sort(high_arr)

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    # 정렬된 결과를 입력받은 배열(arr)에 복사
    for i in range(len(merged_arr)):
        arr[i] = merged_arr[i]

    return arr


#퀵 정렬
def qsort(arr, left, right):
    pl = left
    pr = right
    x = arr[(left + right) // 2]

    while pl <= pr:
        while arr[pl] < x:
            pl += 1
        while arr[pr] > x:
            pr -= 1
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1

    if left < pr:
        qsort(arr, left, pr)
    if pl < right:
        qsort(arr, pl, right)


def quickSort(arr):
    qsort(arr, 0, len(arr)-1)



arr = [6,4,1,7,3,9,8]
'''
with open('/Users/david.kim/PycharmProjects/mid_assignment1/name.txt', 'r') as file:
    line = file.readline().strip('\n') # 첫 번째 라인을 읽어오면서 바로 strip() 함수를 적용
    while line != '':
        arr.append(line)
        line = file.readline().strip('\n') # 다음 라인을 읽어오면서 바로 strip() 함수를 적용


bubbleSort(arr)

quickSort(arr)

'''

#Bucket 정렬




print("[Sorted array is]")
for i in range(len(arr)):
    print("[%04d] %s " % (i+1, arr[i]), end="\n")




