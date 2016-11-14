import sys
def main():
    key = 0
    if len(sys.argv) != 2: 
        print("Error.. Enter the key(int number) \n")
        return 1
    else:
        key = int(sys.argv[1])
    text = str(input("plaintext: "))
    print("ciphertext: ", sep='', end='')
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                cipher = (ord(text[i]) - ord('A') + key) % 26 + ord('A')
                print(chr(cipher), end='')
            else:
                cipher = (ord(text[i]) - ord('a') + key) % 26 + ord('a')
                print(chr(cipher), end='')
        else:
            print(text[i], end='')
    print()
main()
