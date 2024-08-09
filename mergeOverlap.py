# arr = [[14,16],[20,23],[3,9],[6,16],[11,15],[7,17],[18,26],[13,21]]
# arr = [[22,23],[14,24],[4,5],[10,12],[8,11],[12,20],[16,23],[16,18],[19,26],[1,7],[7,17],[5,10],[9,16],[19,27],[9,16],[23,31]]
arr = [[2,8],[9,11],[7,16],[16,20],[2,3],[11,13]]

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
            
        # print(merged, a, filtered)
    return merged
        

assert mergeOverlap([[1, 3], [8, 10], [2, 6], [10, 16]]) == [[1, 6], [8, 16]]
assert mergeOverlap([[17,23],[19,28],[5,7],[18,22],[12,14],[2,7],[10,12],[11,14],[7,17],[1,11],[17,25],[9,19],[17,26],[13,15],[24,27],[14,19],[20,25],[7,12],[18,19]]) == [[1, 28]]
print(mergeOverlap([[17,23],[19,28],[5,7],[18,22],[12,14],[2,7],[10,12],[11,14],[7,17],[1,11],[17,25],[9,19],[17,26],[13,15],[24,27],[14,19],[20,25],[7,12],[18,19]]))