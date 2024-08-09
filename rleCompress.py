# string = '6XXXXXXXXXXsKK55JJGGvooPccccccgggggggggggggssRRRRRRRRR0055eekkkkkkkkubbbbEEJJ7ffSS8'
string = 'kzRnndddddddwwwwwwwwwwDDDDDN4FFFFzzzCDDg555555iiiiiiiiiiiMklllllUJEEEEEEEEEEEEE222'
def rleCompress(string):
    count = 1
    pre = string[0]
    result = ''

    for s in string[1:]:
        # print(count)
        if(s==pre and count<9):
            count += 1
        else:
            result += str(count)+pre
            count = 1
            pre = s
    result += str(count)+pre

    # print(result)
    return result

assert rleCompress('aaaaabccc') == '5a1b3c'
assert rleCompress('aAaAaA') == '1a1A1a1A1a1A'
assert rleCompress('111112333') == '511233'
assert rleCompress('zzzzzzzzzzzzzzzzzzz') == '9z9z1z'

print(rleCompress(string))