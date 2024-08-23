import math
from enum import Enum

class Type(Enum):
    Simple = 1
    Repeat = 2
    Zero = 3

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

def isZero(s):
    if s == '0':
        return True
    else:
        return False
    
assert isZero('0') == True
assert isZero('1') == False
assert isZero('a') == False
assert isZero('@') == False
assert isZero('"') == False

def isNum(s):
    return s.isdigit() and not isZero(s)

def simple(str):
    length = int(str[0])
    return str[1:length+1]

assert simple('1a') == 'a'
assert simple('2ab') == 'ab'
assert simple('9BbCVxtw4I') == 'BbCVxtw4I'
assert simple('5aaabb') == 'aaabb'
assert simple('5aaabb0') == 'aaabb'
assert simple('5aaabb450') == 'aaabb'


def repeatFromPrevious(decompressed, length, shift):
    length = int(length)
    shift = int(shift)
    temp = decompressed[-shift:]

    if length>shift:
        left = int(length%shift)
        time = int(math.floor(length/shift))
        temp = (temp*time)+temp[-shift:-shift+left]
    else:
        temp = temp[:length]
    return temp

assert repeatFromPrevious('BbCVxtw4Izh6KuGzO4DeD', '2', '8') == 'uG'
assert repeatFromPrevious('hTXlDy5B', '5', '1') == 'BBBBB'
assert repeatFromPrevious('sJJ22j5rc', '5', '6') == '22j5r'
assert repeatFromPrevious('sJJ22j5rc22j5r', '7', '2') == '5r5r5r5'
assert repeatFromPrevious('Rd7W11eD88Y11eDm7HfL', '8', '8') == '1eDm7HfL'


def isValid(str):
    return str=='' or str[0].isdigit()

assert isValid('2as') == True
assert isValid('212') == True
assert isValid('012') == True
assert isValid('0') == True
assert isValid('e') == False
assert isValid('e12') == False
assert isValid('esdrftgyhujkl') == False

def type(str, previousType):
    a = str[0]

    if isZero(a):
        return Type.Zero

    b = str[1]
    if isNum(a) and not isNum(b):
        return Type.Simple
    
    if previousType==Type.Repeat:
        return Type.Simple
    else:
        next = str[2:]
        if isNum(a) and isNum(b) and isValid(next):
            return Type.Repeat
        else:
            return Type.Simple

assert type('10', Type.Simple) == Type.Simple
assert type('1a', Type.Simple) == Type.Simple
assert type('012', Type.Simple) == Type.Zero
assert type('72', Type.Zero) == Type.Repeat
assert type('11', Type.Simple) == Type.Repeat
assert type('412114446iEm81099', Type.Simple) == Type.Repeat
assert type('2114446iEm81099', Type.Repeat) == Type.Simple
assert type('4446iEm81099', Type.Simple) == Type.Repeat
assert type('46iEm81099', Type.Repeat) == Type.Simple
assert type('81099', Type.Simple) == Type.Repeat
assert type('099', Type.Repeat) == Type.Zero
assert type('99', Type.Zero) == Type.Repeat

def decompress(str):
    length = int(str[0])
    decompressed = str[1: length+1]
    str = str[length+1:]
    t = Type.Simple

    while len(str)>0:
        t = type(str, t)
        
        if t==Type.Simple:
            decompressed += simple(str)
            length = int(str[0])
        elif t==Type.Repeat:
            decompressed += repeatFromPrevious(decompressed, str[0], str[1])
            length = 1
        else:
            length = 0

        str = str[length+1:]

    return decompressed

assert decompress('1a')=='a'
assert decompress('9BbCVxtw4I') == 'BbCVxtw4I'
assert decompress('5aaabb') == 'aaabb'
assert decompress('5aaabb45') == 'aaabbaaab'
assert decompress('5aaabb450') == 'aaabbaaab'
assert decompress('5aaabb45072') == 'aaabbaaababababa'
assert decompress('5aaabb450723abb') == 'aaabbaaababababaabb'
assert decompress('9zh6KuGzO403DeD28') == 'zh6KuGzO4DeDuG'
assert decompress('9BbCVxtw4I9zh6KuGzO403DeD28') == 'BbCVxtw4Izh6KuGzO4DeDuG'
assert decompress('9BbCVxtw4I9zh6KuGzO403DeD289LrN5PzW3505lBPzu88096') == 'BbCVxtw4Izh6KuGzO4DeDuGLrN5PzW35lBPzuW35lBPzu5lBPzu5lB'
assert decompress('34aj929jayAtGEG6872sT693VDm970784jxHa432mU61') == '4ajajajajajajayAtGEG6yAtGEG6ysTAtGEG6VDmGEG6VDmGEEG6VDmGjxHaxHaxmUUUUUUU'
assert decompress('981HSsU6Iv09PqXsrL1VO09uTWuOuTu1929J2M4gn1m602B4912WI887paMoSaM') == '81HSsU6IvPqXsrL1VOuTWuOuTu1u1u1u1u1uJ2M4gn1m6B4444444444WI444444WIpaMoSaM'
assert decompress('68VzcvR556Zad663583TX6760651P415WwxKH392LP') == '8VzcvRVzcvRZad663vRZadTX6ZadTX6ZdTX6ZdPPPPPWwxKHPPPLP'
assert decompress('3dyL315K4K4x498INemYaNH829G1qaSrwrR624t5go812VV473B1G37') == 'dyLLLLK4K4xLLLLINemYaNHNHNHNHNHG1qaSrwrRrRrRrRt5goooooooooVVooooB1Gooo'
assert decompress('7QTdhQf7149M2n063E5G07qc60iV6675Y6qBy980850511X336CLLXcf') == 'QTdhQf7hM2n063E5Gqc60iV6qc60iVY6qBy0iVY6qBy06qBy06qBBBBBBXBBXCLLXcf'
assert decompress('9geanZw8sY05x0Qlg364ZR8b572Ij796eXN6P6414ptqq495sC7Iq979kYu0uSCkL08MuSgk5nH28') == 'geanZw8sYx0QlgYx0ZR8bYx0ZRIj8bYx0ZReXN6P66666ptqq6666sC7Iq66sC7Iq66kYu0uSCkLMuSgk5nHMu'
assert decompress('2Me718Oy8L08yu836tKD2hF456JHWD2I9392IDrKm6fe06PUkrXl671e') == 'MeeeeeeeeOy8L08yu8yu8yu8ytKD2hFKD2hJHWD2ID2ID2ID2I2IDrKm6fePUkrXlePUkrXe'
assert decompress('6kvwxOv9651Zt1s256G6nRg3264RGHC453naM965xIs72417mGj6hm868') == 'kvwxOvkvwxOvkvw1Zt1s1ZG6nRg3G6RGHC6RGHnaMRGHnaMRGHxIs722222mGj6hm82mGj6h'
assert decompress('6bcz7sB118NkRmvKOq953g66352Oi5237WK299J3OsNQSnD61') == 'bcz7sBBNkRmvKOqmvKOqmvKOg66KOgOiOiOiO7WKiOJ3OsNQSnDDDDDDD'
assert decompress('8IPOMIoqt676O4hGl64138h7386jrjwLD853MFf953q4l4980p13V6DF95072') == 'IPOMIoqtPOMIoqO4hGl666668h7666jrjwLDrjwLDrjwMFfjwMFfjwMFq4lFfjw0p13V6DF3V6DF3V6D6D6D6D6'
assert decompress('8jHsJOXA1269DLhgBoPIr075kK8x6N654T3t2463r6c749Knm6K0z4K06ULbxjf426eExBjf') == 'jHsJOXA1sJDLhgBoPIr5kK8x6NK8x6NKT3t2NKT3r6c3r6c3r6Knm6K0z4KULbxjfjfjfeExBjf'
assert decompress('8hTXlDy5B514U8MG412114446iEm810999ym8LKgwe304d0Am1687b65fHaP962m836') == 'hTXlDy5BBBBBBU8MGGGGG11GG116iEmmmmmmmmmmmmmmmmmmym8LKgwe3d0Ame7b65fHaP65fHaP65fm8P65'
assert decompress('9Rd7W11eD8028Y475m7HfL8816679s8hiWhiWx09sJJ22j5rc56072') == 'Rd7W11eD88Y11eDm7HfL1eDm7HfL6Dm7HfLs8hiWhiWxsJJ22j5rc22j5r5r5r5r5'