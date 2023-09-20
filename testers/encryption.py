# A - Z 65-90
# a - z 97-122
# ord(your_letter)
# chr(your_code)

#Use isupper() to decide which unicodes to work def name(name, lastName='john')
# Add the key (number of characters to shit) and if
# the key is bigger or small then the unicode for
# A, Z, a, zincrease or decrease by 26

# recieve the message to encryptand the number of characters to shift
message = input("Enter your message: ")
key = int(input("How many characters should we shift (1 - 26)"))
# prepare the secret_message
secret_message = ""
# cycle through each character in the message
for char in message:
    # if it isnt a letter then keep it as is
    if char.isalpha():
        # get the character code and add the shift amount for key
        char_code = ord(char)
        char_code += key
        
        # if uppercase then compare to uppercase unicodes
        if char.isupper():
            
            # if bigger then Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
            # if smaller then A add 26
            if char_code < ord('A'):
                char_code += 26
    # do the same for lower case characters
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
        # convert from code to letter and add to message
        secret_message += chr(char_code)
    
    else:
        secret_message += char 

print("Encrypted :", secret_message)

key = -key

orig_message = ""

for char in secret_message:
    
    # if it isnt a letter then keep it as is
    if char.isalpha():
            
        # get the character code and add the shift amount
        char_code = ord(char)
        char_code += key
        # if uppercase then compare to uppercase unicodes
        
        if char.isupper():        
            # if bigger then Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
            # if smaller then A add 26
            if char_code < ord('A'):
                char_code += 26
            # do the same for lower case characters
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
    
            # convert from code to letter and add to message
        orig_message += chr(char_code)
    
    else:
        orig_message += char

print("Decrypted :", orig_message)
