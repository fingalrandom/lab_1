import sys


def encrypt(text, key):
    alph = ''
    for i in range(256):
        alph += chr(i)
    i = 0
    lenth = len(text)
    code = ''
    while len(text) > len(key):
        key = key + key[i]
        i = i + 1
    i = 0
    while i < lenth:
        cur = alph.find(key[i])
        ch = alph.find(text[i])
        code = code + alph[(ch+cur) % len(alph)]
        i = i+1
    return code


def decrypt(text, key):
    alph = ''
    for i in range(256):
        alph += chr(i)
    i = 0
	lenth = len(text)
    decode = ''
    while len(text) > len(key):
        key = key + key[i]
        i = i + 1
    i = 0
    while i < lenth:
        ch = alph.find(text[i])
        cur = alph.find(key[i])
        decode = decode + alph[(ch-cur) % len(alph)]
        i = i+1
    return decode


def main():
    print "Example of main string:"
    print "[*.py] [input file name] [key file name]\
        [result file name] [encode or decode]"
    print "    ""-c"" - encode"
    print "    ""-d"" - decode"
    countPar = len(sys.argv)
    if (countPar != 5):
        print "There is wrong number of parameters."
        exit()
    if(sys.argv[4] != "-c" and sys.argv[4] != "-d"):
        print "irregular operation"
        exit()

    inFileName = sys.argv[1]
    keyFileName = sys.argv[2]
    rezFileName = sys.argv[3]
    fl = sys.argv[4]

    with open(inFileName, 'r') as inFile:
        TXT = inFile.read()
    with open(keyFileName, 'r') as keyFile:
        KEY = keyFile.read()
    if fl == '-c':
        rez = encrypt(TXT, KEY)
    else:
        rez = decrypt(TXT, KEY)
    with open(rezFileName, 'w') as rezFile:
        rezFile.write(rez)
if __name__ == "__main__":
    main()
