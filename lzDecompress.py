import math

# str = '9BbCVxtw4I09zh6KuGzO403DeD289LrN5PzW3505lBPzu880967eFNwUoq591i920811l71'
str = '34aj929jayAtGEG6872sT693VDm970784jxHa432mU61'

def lzDecompress(str):
    result = ''
    index = 0
    cut = 0
    new = True

    while (cut+index<len(str)):
        print(cut, index)
        if new:
            index += int(str[cut+index])+1
            result += str[cut+1:cut+index]
            new = False
            print('index',index)
        else:
            l = int(str[cut+index])
            print('l ', l)
            
            if(l==0):
                index += 1
                continue
            
            left = str[cut+index+1]
            print('left', left)
            
            if (not left.isdigit()):
                cut += index
                index = 0
                new = True
                continue
            
            left = int(left)
            temp = result[-left:-left+l] if l<left else result[-left:]
            print(temp)
            time = math.floor(l/left)
            result += temp*time
            result += temp[0:(l%left)]
            index += 2
        print(result)
    return result
            

# assert lzDecompress('9BbCVxtw4I') == 'BbCVxtw4I'
# assert lzDecompress('5aaabb') == 'aaabb'
# assert lzDecompress('5aaabb45') == 'aaabbaaab'
# assert lzDecompress('5aaabb450') == 'aaabbaaab'
# assert lzDecompress('5aaabb45072') == 'aaabbaaababababa'
# assert lzDecompress('5aaabb450723abb') == 'aaabbaaababababaabb'
# assert lzDecompress('9zh6KuGzO403DeD28') == 'zh6KuGzO4DeDuG'
# assert lzDecompress('9BbCVxtw4I9zh6KuGzO403DeD28') == 'BbCVxtw4Izh6KuGzO4DeDuG'
assert lzDecompress('9BbCVxtw4I9zh6KuGzO403DeD289LrN5PzW3505lBPzu88096') == 'BbCVxtw4Izh6KuGzO4DeDuGLrN5PzW35lBPzuW35lBPzu5lBPzu5lB'

print(lzDecompress(str))