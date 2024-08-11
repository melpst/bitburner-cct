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
    return result

assert rleCompress('aaaaabccc') == '5a1b3c'
assert rleCompress('aAaAaA') == '1a1A1a1A1a1A'
assert rleCompress('111112333') == '511233'
assert rleCompress('zzzzzzzzzzzzzzzzzzz') == '9z9z1z'
assert rleCompress('6XXXXXXXXXXsKK55JJGGvooPccccccgggggggggggggssRRRRRRRRR0055eekkkkkkkkubbbbEEJJ7ffSS8') == '169X1X1s2K252J2G1v2o1P6c9g4g2s9R20252e8k1u4b2E2J172f2S18'
assert rleCompress('kzRnndddddddwwwwwwwwwwDDDDDN4FFFFzzzCDDg555555iiiiiiiiiiiMklllllUJEEEEEEEEEEEEE222') == '1k1z1R2n7d9w1w5D1N144F3z1C2D1g659i2i1M1k5l1U1J9E4E32'
assert rleCompress('3ZZZZZZZMMMMMMMMMhhhhhhhhhhhhhiiiiiiiiiiiO00ssFFllNNNNNNNNNNNNNDDHHHq8pphh') == '137Z9M9h4h9i2i1O202s2F2l9N4N2D3H1q182p2h'

string = '3ZZZZZZZMMMMMMMMMhhhhhhhhhhhhhiiiiiiiiiiiO00ssFFllNNNNNNNNNNNNNDDHHHq8pphh'
print(rleCompress(string))