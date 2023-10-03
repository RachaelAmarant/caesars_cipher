import string

''' The Caesar Cipher is a simple encryption technique that was used by Julias Caesar to communicate 
with his allies. The method involved subsituting a letter with another letter in a fixed position. 
This program uses lists to represent the English alphabet. '''

eng_caps = list(string.ascii_uppercase) 
eng_lowercase = list(string.ascii_lowercase)

''' The above lists are then modified to create the cipher. This has been done by using list slicing. 
In a right shift the last few letters are moved to the beginning of the alphabet. '''

shift = 3 
cipher_caps = eng_caps[-shift:] + eng_caps[:-shift] 
cipher_lowercase = eng_lowercase[-shift:] + eng_lowercase[:-shift]


def encrypt():
    encrypted_phrase = []
    encryption_caps = dict(zip(cipher_caps, eng_caps))
    encryption_lowercase = dict(zip(cipher_lowercase, eng_lowercase))
    eng_phrase = input('Plain English: ')
    for char in eng_phrase:
        if char.isupper():
            char = encryption_caps[char]
            encrypted_phrase.append(char)
        elif char.islower():
            char = encryption_lowercase[char]
            encrypted_phrase.append(char)
        else:
            char = char
            encrypted_phrase.append(char)
    encrypted = ''.join(encrypted_phrase)
    print(encrypted)


def decrypt():
    decrypted_phrase = []
    decryption_caps = dict(zip(eng_caps, cipher_caps))
    decryption_lowercase = dict(zip(eng_lowercase, cipher_lowercase))
    encrypted_phrase = input('Cipher: ')
    for char in encrypted_phrase:
        if char.isupper():
            char = decryption_caps[char]
            decrypted_phrase.append(char)
        elif char.islower():
            char = decryption_lowercase[char]
            decrypted_phrase.append(char)
        else:
            char = char
            decrypted_phrase.append(char)
    decrypted = ''.join(decrypted_phrase)
    print(decrypted)


def run():
    while True:
        start_program = input('\nEnter e for encrypt or d for decrypt: ').lower()
        if start_program == 'e':
            encrypt()
        else:
            decrypt()
        restart = input('Do you want to continue (y/n)?: ').lower()
        if restart.lower() == 'y':
            continue
        else:
            break


run()
