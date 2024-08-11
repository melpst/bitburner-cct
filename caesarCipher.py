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
assert cipher(["EMAIL MEDIA TRASH MACRO TABLE", 1]) == 'DLZHK LDCHZ SQZRG LZBQN SZAKD'
assert cipher(["ENTER CLOUD MOUSE PRINT CACHE", 18]) == 'MVBMZ KTWCL UWCAM XZQVB KIKPM'
assert cipher(["VIRUS ENTER EMAIL CACHE MEDIA", 8]) == 'NAJMK WFLWJ WESAD USUZW EWVAS'
assert cipher(["POPUP ARRAY CACHE PRINT FLASH", 24]) == 'RQRWR CTTCA ECEJG RTKPV HNCUJ'
print(cipher(["POPUP ARRAY CACHE PRINT FLASH", 24]))