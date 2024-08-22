import math

def lzDecompress(str):
    result = ''
    index = 0
    cut = 0
    new = True

    while (cut+index<len(str)):
        # print(cut, index)
        if new:
            index += int(str[cut+index])+1
            result += str[cut+1:cut+index]
            new = False
            # print('index',index)
        else:
            # print(result)
            l = int(str[cut+index])
            # print('l ', l)
            
            if(l==0):
                index += 1
                continue
            
            left = str[cut+index+1]
            # print('left', left)
            
            if (not left.isdigit()):
                cut += index
                index = 0
                new = True
                continue
            
            left = int(left)
            temp = result[-left:-left+l] if l<left else result[-left:]
            # print(temp)
            time = math.floor(l/left)
            result += temp*time
            result += temp[0:(l%left)]
            index += 2
        # print(result)
    return result
            

str = '8jHsJOXA1269DLhgBoPIr075kK8x6N654T3t2463r6c749Knm6K0z4K06ULbxjf426eExBjf'
print(lzDecompress(str))

assert lzDecompress('9BbCVxtw4I') == 'BbCVxtw4I'
assert lzDecompress('5aaabb') == 'aaabb'
assert lzDecompress('5aaabb45') == 'aaabbaaab'
assert lzDecompress('5aaabb450') == 'aaabbaaab'
assert lzDecompress('5aaabb45072') == 'aaabbaaababababa'
assert lzDecompress('5aaabb450723abb') == 'aaabbaaababababaabb'
assert lzDecompress('9zh6KuGzO403DeD28') == 'zh6KuGzO4DeDuG'
assert lzDecompress('9BbCVxtw4I9zh6KuGzO403DeD28') == 'BbCVxtw4Izh6KuGzO4DeDuG'
assert lzDecompress('9BbCVxtw4I9zh6KuGzO403DeD289LrN5PzW3505lBPzu88096') == 'BbCVxtw4Izh6KuGzO4DeDuGLrN5PzW35lBPzuW35lBPzu5lBPzu5lB'
assert lzDecompress('34aj929jayAtGEG6872sT693VDm970784jxHa432mU61') == '4ajajajajajajayAtGEG6yAtGEG6ysTAtGEG6VDmGEG6VDmGEEG6VDmGjxHaxHaxmUUUUUUU'
assert lzDecompress('981HSsU6Iv09PqXsrL1VO09uTWuOuTu1929J2M4gn1m602B4912WI887paMoSaM') == '81HSsU6IvPqXsrL1VOuTWuOuTu1u1u1u1u1uJ2M4gn1m6B4444444444WI444444WIpaMoSaM'
assert lzDecompress('68VzcvR556Zad663583TX6760651P415WwxKH392LP') == '8VzcvRVzcvRZad663vRZadTX6ZadTX6ZdTX6ZdPPPPPWwxKHPPPLP'
assert lzDecompress('3dyL315K4K4x498INemYaNH829G1qaSrwrR624t5go812VV473B1G37') == 'dyLLLLK4K4xLLLLINemYaNHNHNHNHNHG1qaSrwrRrRrRrRt5goooooooooVVooooB1Gooo'
assert lzDecompress('7QTdhQf7149M2n063E5G07qc60iV6675Y6qBy980850511X336CLLXcf') == 'QTdhQf7hM2n063E5Gqc60iV6qc60iVY6qBy0iVY6qBy06qBy06qBBBBBBXBBXCLLXcf'
assert lzDecompress('9geanZw8sY05x0Qlg364ZR8b572Ij796eXN6P6414ptqq495sC7Iq979kYu0uSCkL08MuSgk5nH28') == 'geanZw8sYx0QlgYx0ZR8bYx0ZRIj8bYx0ZReXN6P66666ptqq6666sC7Iq66sC7Iq66kYu0uSCkLMuSgk5nHMu'
# assert lzDecompress('2Me718Oy8L08yu836tKD2hF456JHWD2I9392IDrKm6fe06PUkrXl671e') == 'MeeeeeeeeOy8L08yu8yu8yu8ytKD2hFKD2hJHWD2ID2ID2ID2I2IDrKm6fePUkrXlePUkrXe'


str = '2Me718Oy8L08yu836tKD2hF456JHWD2I9392IDrKm6fe06PUkrXl671e'
print(lzDecompress(str))