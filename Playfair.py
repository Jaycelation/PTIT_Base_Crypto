def toLowerCase(text):
    return text.lower()


def removeSpaces(text):
    return text.replace(" ", "")


def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
        group = i
    Diagraph.append(text[group:])
    return Diagraph


def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + 'x' + text[i+1:]
                return FillerLetter(new_word)
        return text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + 'x' + text[i+1:]
                return FillerLetter(new_word)
        return text


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = key_letters[:]
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix


def search(mat, element):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == element:
                return i, j


def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[e1r][(e1c + 1) % 5]
    char2 = matr[e2r][(e2c + 1) % 5]
    return char1, char2


def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[(e1r + 1) % 5][e1c]
    char2 = matr[(e2r + 1) % 5][e2c]
    return char1, char2


def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    return matr[e1r][e2c], matr[e2r][e1c]


def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(len(plainList)):
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        CipherText.append(c1 + c2)

    return "".join(CipherText)


def decrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[e1r][(e1c - 1) % 5]
    char2 = matr[e2r][(e2c - 1) % 5]
    return char1, char2


def decrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[(e1r - 1) % 5][e1c]
    char2 = matr[(e2r - 1) % 5][e2c]
    return char1, char2


def decrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    return matr[e1r][e2c], matr[e2r][e1c]


def decryptByPlayfairCipher(Matrix, cipherList):
    PlainText = []
    for i in range(len(cipherList)):
        ele1_x, ele1_y = search(Matrix, cipherList[i][0])
        ele2_x, ele2_y = search(Matrix, cipherList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = decrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = decrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = decrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        PlainText.append(c1 + c2)

    return "".join(PlainText)


# Input
text_Plain = 'instruments'
text_Plain = removeSpaces(toLowerCase(text_Plain))
PlainTextList = Diagraph(FillerLetter(text_Plain))
if len(PlainTextList[-1]) != 2:
    PlainTextList[-1] += 'z'

key = "Monarchy"
key = toLowerCase(key)
Matrix = generateKeyTable(key, list1)

# Encryption
CipherText = encryptByPlayfairCipher(Matrix, PlainTextList)
print("Cipher Text:", CipherText)

# Decryption
cipherPairs = Diagraph(CipherText)
DecryptedText = decryptByPlayfairCipher(Matrix, cipherPairs)
print("Decrypted Text:", DecryptedText)