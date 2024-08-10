
"""
  Encryption II: Vigenère Cipher
  You are attempting to solve a Coding Contract. You have 10 tries remaining, after which the contract will self-destruct.


  Vigenère cipher is a type of polyalphabetic substitution. It uses the Vigenère square to encrypt and decrypt plaintext with a keyword.

    Vigenère square:
          A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        +----------------------------------------------------
      A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
      B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
      C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
      D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
      E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
                  ...
      Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
      Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

  For encryption each letter of the plaintext is paired with the corresponding letter of a repeating keyword. For example, the plaintext DASHBOARD is encrypted with the keyword LINUX:
    Plaintext: DASHBOARD
    Keyword:   LINUXLINU
  So, the first letter D is paired with the first letter of the key L. Therefore, row D and column L of the Vigenère square are used to get the first cipher letter O. This must be repeated for the whole ciphertext.

  You are given an array with two elements:
    ["MACROPRINTPASTEVIRUSPOPUP", "BLOGGER"]
    ["CLOUDDEBUGLOGINPOPUPLOGIC", "COMMAND"]
    ["FRAMEENTERMOUSECACHECLOUD", "OFFLINE"]
    ["FLASHENTERPRINTPOPUPVIRUS", "RUNTIME"]
  The first element is the plaintext, the second element is the keyword.

  Return the ciphertext as uppercase string.


  If your solution is an empty string, you must leave the text box empty. Do not use "", '', or ``.
"""

def repeatChar(keyword, length):
    if length<len(keyword):
        return keyword[:length]
    return keyword+repeatChar(keyword, length-len(keyword))

assert repeatChar("LINUX", 9) == "LINUXLINU"
assert repeatChar("BLOGGER",25) == "BLOGGERBLOGGERBLOGGERBLOG"
assert repeatChar("COMMAND",25) == "COMMANDCOMMANDCOMMANDCOMM"
assert repeatChar("OFFLINE",25) == "OFFLINEOFFLINEOFFLINEOFFL"
assert repeatChar("RUNTIME",25) == "RUNTIMERUNTIMERUNTIMERUNT"

def alphabetIndex(c):
    return ord(c)%65

assert alphabetIndex("A") == 0
assert alphabetIndex("B") == 1
assert alphabetIndex("Z") == 25
assert alphabetIndex("Y") == 24
assert alphabetIndex("X") == 23

def shiftRight(p, i):
    shiftIndex = alphabetIndex(i)
    plainIndex = alphabetIndex(p)
    cipherIndex = (plainIndex+shiftIndex)%26
    # print(cipherIndex)
    return chr(65+cipherIndex)

assert shiftRight("A","A") == "A"
assert shiftRight("A","B") == "B"
assert shiftRight("D","L") == "O"
assert shiftRight("C","I") == "K"

def vigenereCipher(input):
    plain = input[0]
    keyword = repeatChar(input[1], len(plain))

    if len(plain)<2:
        return shiftRight(plain, keyword)
    else:
        return shiftRight(plain[0], keyword[0])+vigenereCipher([plain[1:], keyword[1:]])
    
assert vigenereCipher(["D","L"]) == "O"
assert vigenereCipher(["C","I"]) == "K"
assert vigenereCipher(["MACROPRINTPASTEVIRUSPOPUP", "BLOGGER"]) == "NLQXUTIJYHVGWKFGWXAWGPAIV"
assert vigenereCipher(["CLOUDDEBUGLOGINPOPUPLOGIC", "COMMAND"]) == "EZAGDQHDISXOTLPDABUCOQUUO"
assert vigenereCipher(["FRAMEENTERMOUSECACHECLOUD", "OFFLINE"]) == "TWFXMRRHJWXWHWSHFNPRGZTZO"
assert vigenereCipher(["FLASHENTERPRINTPOPUPVIRUS", "RUNTIME"]) == "WFNLPQRKYEIZURKJBICBZZLHL"