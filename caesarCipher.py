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
    return result

input = ["ENTER ARRAY LOGIN PRINT MOUSE", 9]
print(cipher(input))

assert cipher(['BCD',1]) == 'ABC'
assert cipher(["VIRUS LOGIC ENTER CACHE LOGIN", 2]) == 'TGPSQ JMEGA CLRCP AYAFC JMEGL'
assert cipher(["MEDIA TABLE FLASH ARRAY QUEUE", 19]) == 'TLKPH AHISL MSHZO HYYHF XBLBL'
assert cipher(["EMAIL MEDIA TRASH MACRO TABLE", 1]) == 'DLZHK LDCHZ SQZRG LZBQN SZAKD'
assert cipher(["ENTER CLOUD MOUSE PRINT CACHE", 18]) == 'MVBMZ KTWCL UWCAM XZQVB KIKPM'
assert cipher(["VIRUS ENTER EMAIL CACHE MEDIA", 8]) == 'NAJMK WFLWJ WESAD USUZW EWVAS'
assert cipher(["POPUP ARRAY CACHE PRINT FLASH", 24]) == 'RQRWR CTTCA ECEJG RTKPV HNCUJ'
assert cipher(["INBOX LINUX FLASH CLOUD PRINT", 2]) == 'GLZMV JGLSV DJYQF AJMSB NPGLR'
assert cipher(["CLOUD ENTER TABLE LOGIN MOUSE", 23]) == 'FORXG HQWHU WDEOH ORJLQ PRXVH'
assert cipher(["ENTER CACHE FRAME QUEUE ARRAY", 17]) == 'NWCNA LJLQN OAJVN ZDNDN JAAJH'
assert cipher(["MEDIA TABLE ENTER VIRUS DEBUG", 17]) == 'VNMRJ CJKUN NWCNA ERADB MNKDP'
assert cipher(["SHELL LINUX LOGIC VIRUS ARRAY", 1]) == 'RGDKK KHMTW KNFHB UHQTR ZQQZX'
assert cipher(["SHIFT ARRAY LOGIN MOUSE CACHE", 13]) == 'FUVSG NEENL YBTVA ZBHFR PNPUR'
assert cipher(["DEBUG CLOUD VIRUS MACRO LOGIC", 15]) == 'OPMFR NWZFO GTCFD XLNCZ WZRTN'
assert cipher(["LINUX CACHE QUEUE CLOUD SHIFT", 20]) == 'ROTAD IGINK WAKAK IRUAJ YNOLZ'
assert cipher(["ENTER ARRAY LOGIN PRINT MOUSE", 9]) == 'VEKVI RIIRP CFXZE GIZEK DFLJV'
