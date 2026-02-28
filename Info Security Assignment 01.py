
def caesar_encrypt(text, shift):   #for encryption
    encrypted_message = ''   #for storing encrypted message
    for character in text:  #loop to compare each character with entered characters
        if character in lowercase:   #for lowercase characters
            encrypted_message += lowercase[(lowercase.index(character) + shift) % 26]    #shift character forward and using mode 26, returns remainder which is our new value
        elif character in uppercase:    #for uppercase characters
            encrypted_message += uppercase[(uppercase.index(character) + shift) % 26]
        else:    #for characters other than alphabet
            encrypted_message += character  #spaces and symbols will remain unchanged

    return encrypted_message  #it returns encrypted message

def caesar_decrypt(ciphertext, shift):    #for Decryption
    decrypted_message = ''  #for storing decrypted message
    for character in ciphertext:
        if character in lowercase:
            decrypted_message += lowercase[(lowercase.index(character) - shift) % 26]    #shift character backward and using mode 26, returns remainder which is our initial or original value
        elif character in uppercase:
            decrypted_message += uppercase[(uppercase.index(character) - shift) % 26]
        else:
            decrypted_message += character

    return decrypted_message  #it returns decrypted message

lowercase = 'abcdefghijklmnopqrstuvwxyz'    #alphabets keys in Lowercase
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    #alphabets keys in Uppercase

#main
print("Caesar Cipher: ")
message = input("Enter message: ")     #to take message as input
shift = int(input("Enter shift value: "))    #to take shift value as input

encrypted = caesar_encrypt(message, shift)   #encrypt function calling
print("Encrypted Text:", encrypted)

decrypted = caesar_decrypt(encrypted, shift)   #decrypt function calling
print("Decrypted Text:", decrypted)
