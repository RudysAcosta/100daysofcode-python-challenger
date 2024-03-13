alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    text_procese = ''
    for char in text:
        index = alphabet.index(char)
        new_index = (index + shift)
        # if index is more than len of alphabet start by init 
        if new_index >= len(alphabet):
            new_index -= len(alphabet)
        
        text_procese +=  alphabet[new_index]
    print(f"The encoded text is {text_procese}")

def decrypt(text, shift):
    text_procese = ''

    for char in text:
        index = alphabet.index(char)
        new_index = (index - shift)
        text_procese +=  alphabet[new_index]
    print(text_procese)

if direction == 'encode': 
    encrypt(text, shift) 
else: 
    decrypt(text, shift)