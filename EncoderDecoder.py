"""
Encoder Decoder is a file which encodes an english language written text into binary numbers or decodes the hidden message behind the binary numbers.
Methods:
    binaryDecoder(text) : takes a string of binary numbers to decode, returns the message
    stringEncoder(text) : takes the message to convert to binary numbers

    @author: Ishpreet Singh
    @build: November 5, 2020
    @LastUpdate: November 5, 2020

"""
def binaryDecoder(text: str) -> str:
    """@param text: space separated string of binary numbers to be decoded"""
    # binary = input("Enter your binary code here(separated by space): ").split(" ")
    binary = text.split(" ")
    message = ""
    chars = []

    for sub in binary:
        if len(sub) != 8:
            print(f"Binary {sub} is wrong! Length of 8 not matched.")
            break
        else:
            character_ascii = int(sub, 2)   # returns a number which will be the ascii value
            letter = chr(character_ascii)   # returns a letter specified to the ascii value
            chars.append(letter)            # append to a list
    
    message = message.join(chars)   # join the list to form a message

    return message

def stringEncoder(text: str) -> str:
    """@param text: space separated string to be encoded"""
    # String = input("Enter your text here (separated by space): ").split(" ")
    String = text.split(" ")
    ascii_values = []
    binary_values = []
    message = ""

    # collect all the ascii values of every letter
    for substring in String:
        for sub in substring:
            ascii_values.append(ord(sub))
    
    # convert all ascii values into binary format
    for elem in ascii_values:
        binary_values.append((bin(elem).replace('0b', '0')) + " ")
        
    message = message.join(binary_values)
    return message

