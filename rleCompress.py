def rleCompress(string):
    count = 1
    pre = string[0]
    result = ''

    for s in string[1:]:
        if(s==pre and count<9):
            count += 1
        else:
            result += str(count)+pre
            count = 1
            pre = s
    result += str(count)+pre
    return result


string = 'ooooooofftttttttttwwwwwwwwwwwwFFPPPPPPPPSBBBBBBBBBB661Q4666666666b3ggggggggggggC'
print(rleCompress(string))


assert rleCompress('aaaaabccc') == '5a1b3c'
assert rleCompress('aAaAaA') == '1a1A1a1A1a1A'
assert rleCompress('111112333') == '511233'
assert rleCompress('zzzzzzzzzzzzzzzzzzz') == '9z9z1z'
assert rleCompress('6XXXXXXXXXXsKK55JJGGvooPccccccgggggggggggggssRRRRRRRRR0055eekkkkkkkkubbbbEEJJ7ffSS8') == '169X1X1s2K252J2G1v2o1P6c9g4g2s9R20252e8k1u4b2E2J172f2S18'
assert rleCompress('kzRnndddddddwwwwwwwwwwDDDDDN4FFFFzzzCDDg555555iiiiiiiiiiiMklllllUJEEEEEEEEEEEEE222') == '1k1z1R2n7d9w1w5D1N144F3z1C2D1g659i2i1M1k5l1U1J9E4E32'
assert rleCompress('3ZZZZZZZMMMMMMMMMhhhhhhhhhhhhhiiiiiiiiiiiO00ssFFllNNNNNNNNNNNNNDDHHHq8pphh') == '137Z9M9h4h9i2i1O202s2F2l9N4N2D3H1q182p2h'
assert rleCompress('SUUUUUUWWWWWWWWWXuuuuummmzzzzzzzzyyyyyyyyefffffffVV577MqqxnaaM233zMzzzZttXJJR000000') == '1S6U9W1X5u3m8z8y1e7f2V15271M2q1x1n2a1M12231z1M3z1Z2t1X2J1R60'
assert rleCompress('I88IIQQ4lIIAeeeeeeee6KKKKKKKKKMMGrrrrrrrrrrrU111111evvvvvvvv777777qqqqqqqqqq66c111') == '1I282I2Q141l2I1A8e169K2M1G9r2r1U611e8v679q1q261c31'
assert rleCompress('eeOOWWesQQ0044qqHH66666666OOOOOOOOOOObbcccrrrrrPPPPPIIggggggggggXX') == '2e2O2W1e1s2Q20242q2H869O2O2b3c5r5P2I9g1g2X'
assert rleCompress('mjr6DDDDDDDDDDD888888888888Xvvvvvz22YY44444444OOOOOOOOw0pppppppppppppp') == '1m1j1r169D2D98381X5v1z222Y848O1w109p5p'
assert rleCompress('bbbbbGGGGGGGGGGGGGHHoooo3VV77ddddddddddddddQdd22MMMMMMczz') == '5b9G4G2H4o132V279d5d1Q2d226M1c2z'
assert rleCompress('0000000000FFFJJKKKKKKKKKjGUUS0QQQQQQQQQQQQQJJJJJJJJJJJggggg00EEpDDbGLv') == '90103F2J9K1j1G2U1S109Q4Q9J2J5g202E1p2D1b1G1L1v'
assert rleCompress('ooooooofftttttttttwwwwwwwwwwwwFFPPPPPPPPSBBBBBBBBBB661Q4666666666b3ggggggggggggC') == '7o2f9t9w3w2F8P1S9B1B26111Q14961b139g3g1C'
assert rleCompress('2jjjjjjjjji66666666666ooRRRRRssssssssssHHh77f44BBaaaaaaaaammmmttZvvo88MMWW0') == '129j1i96262o5R9s1s2H1h271f242B9a4m2t1Z2v1o282M2W10'
assert rleCompress('IIIIIIIIIIIIII16kk5YMMMBOOOOOOOOOOOOa66uummmmHHbDDDSSVVVVVVVVVFFFFFFFKjjmmcc2') == '9I5I11162k151Y3M1B9O3O1a262u4m2H1b3D2S9V7F1K2j2m2c12'