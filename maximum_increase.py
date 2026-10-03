#given array like 1 7 2 11 15, we need to print the maximum sized subarray that is in
#ascending order. So in this case, 2 11 15 is in increasing sequence, so answer is 3 <3 terms>
n = int(input())
arr = input().split()
arr = [int(x) for x in arr]
size = 1
max_subarr = [1]
for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        size = size + 1
        max_subarr.append(size)
    else:
        size = 1
print(max(max_subarr))