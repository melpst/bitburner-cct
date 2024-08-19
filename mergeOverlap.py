
def mergeOverlap(arr):
    merged = [arr[0]]
    for a in arr[1:]:
        filtered = list(filter(lambda x: x[0]<=a[1] and x[1]>=a[0], merged))
        if(len(filtered)==0):
            merged.append(a)
        else:
            for f in filtered:
                if f[0]<=a[1] and f[0]<a[0]:
                        a[0] = f[0]
                if f[1]>=a[0] and f[1]>a[1]:
                        a[1] = f[1]
            # print(a)
            merged = list(filter(lambda x: x not in filtered and x != a, merged))
            merged.append(a)
            merged.sort()
    return merged
        

assert mergeOverlap([[1, 3], [8, 10], [2, 6], [10, 16]]) == [[1, 6], [8, 16]]
assert mergeOverlap([[17,23],[19,28],[5,7],[18,22],[12,14],[2,7],[10,12],[11,14],[7,17],[1,11],[17,25],[9,19],[17,26],[13,15],[24,27],[14,19],[20,25],[7,12],[18,19]]) == [[1, 28]]
assert mergeOverlap([[22,27],[19,21],[13,14],[20,26],[18,26]]) == [[13, 14], [18, 27]]

input = [[22,27],[19,21],[13,14],[20,26],[18,26]]
print(mergeOverlap(input))