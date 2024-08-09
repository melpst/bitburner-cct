def cipher(input):
    str = input[0].replace('"', '')
    shift = int(input[1])
    result = ''
    ascii = list(range(65, 91, 1))

    for s in str:
        if(s!=' '):
            asc = (ord(s)-shift-65)%26
            result += chr(ascii[asc])
        else:
            result += s
    # print(result)
    return result

assert cipher(['BCD',1]) == 'ABC'
assert cipher(["VIRUS LOGIC ENTER CACHE LOGIN", 2]) == 'TGPSQ JMEGA CLRCP AYAFC JMEGL'
assert cipher(["MEDIA TABLE FLASH ARRAY QUEUE", 19]) == 'TLKPH AHISL MSHZO HYYHF XBLBL'