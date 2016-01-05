
# Name: Ahsan Mahmood


def ceaser(filename, key):
    '''(string, integer) --> list
    Returns a list of ciphered lines by changing letters according to key
    >>> print ceaser('plain1.txt', 1)
    >>> ['BCDEFGH']
    '''
    original_file = open(filename, 'r')
    ciphered_list = []
           
    for line in original_file:
        ciphered_line = ""
        line = line.replace("\n"," ") #Strips the 'next line' substring to prevent unnecessary deciphering of letter 'n'
        
        for character in line: # For every character in line
           if character.isalpha and 65 <= ord(character) <= 91: # For all capital letters
                letter_index = ord(character) - 65
                cipher_index = ((letter_index + key) % 26) + 65
                ciphered_line += chr(cipher_index)              #Ciphered letter added to line
           elif character.isalpha and 97 <= ord(character) <= 122: # For all lower case letters
                letter_index = ord(character) - 97
                cipher_index = ((letter_index + key) % 26) + 97
                ciphered_line += chr(cipher_index) 
           else:
                ciphered_line += character                      #Else if not letter, copy verbatim
                
        ciphered_list += [ciphered_line]                        #Ciphered line added to list

    original_file.close()

    return ciphered_list
        
def vigenere(filename, key_list):
    '''(string, list) --> list
    Returns a list of all the lines ciphered by the function by changing letters according to key values
    >>> print vigenere('plain3.txt', vigenere_key('BAD'))
    >>> ['BA      ec!!     zc?? ', '   fxwsa    vqaffs  ! ']
    '''
    original_file = open(filename, 'r')
    ciphered_list = []
    index = -1                          #Since first index is zero in key_list

    for line in original_file:
        ciphered_line = ""
        line = line.replace("\n"," ")
        for character in line:
            if character.isalpha and 65 <= ord(character) <= 91: 
                    index += 1
                    key = key_list[index % len(key_list)] # Repeat first key after using the last one
                    
                    letter_index = ord(character) - 65
                    cipher_index = ((letter_index + key) % 26) + 65
                    ciphered_line += chr(cipher_index) 
            elif character.isalpha and 97 <= ord(character) <= 122:
                    index += 1
                    key = key_list[index % len(key_list)]
                    
                    letter_index = ord(character) - 97
                    cipher_index = ((letter_index + key) % 26) + 97
                    ciphered_line += chr(cipher_index) 
            else:
                    ciphered_line += character
                    
        ciphered_list += [ciphered_line]

    original_file.close()

    return ciphered_list

def vigenere_key(key):
    '''(string) --> list
    Returns a list of key values represented by letters in the original user key
    >>> vigenere_key('KEY')
    >>> [10,4,24]
    '''
    key_list = []
    
    for letter in key:
        key_list += [ord(letter) - 65] # Value is equal to place in alphabet, starting with A = 0
        
    return key_list


def vigenere_rotate_key(key):
    '''(string) --> list
    Returns a list of rotated keys by going through each letters for deciphering purposes
    >>> vigenere_rotate_key('KEY')
    >>> [16, 22, 2]
    '''
    key_list = []

    for letter in key:
        key_list +=  [26 - (ord(letter) - 65)] #Saves rotated position of key

    return key_list

def write_to_file(filename, line_list):
    '''(string of name of file, list of lines) --> None
    Writes the list of lines passed as a parzmeter into a file with the file name provided
    '''
    cipher_file = open(filename, 'w')

    for line in line_list:
        cipher_file.write(line)
        cipher_file.write("\n") #Compensates for the 'next line' substrings removed earlier in the helper functions
    cipher_file.close()

    return

def crack_code(filename):
    '''(string of name of file) --> int
    Returns a key by breaking the code in a ciphered file by the file name provided 
    >>> crack_code(cipher1.txt)
        2
    '''
    code_file = open(filename)

    letter_count = {}

    count_to_letter = {}

    for line in code_file:
        line = line.replace("\n"," ")
        for letter in line:
            if letter in letter_count and letter != " ":
                letter_count[letter] += 1
            elif letter not in letter_count and letter != " ":
                letter_count[letter] = 1
     
    for letter in letter_count:
        count_to_letter[letter_count[letter]] = letter
                  
    most_frequent = count_to_letter[max(count_to_letter)]
    
    if 65 <= ord(most_frequent) <= 91: # For all capital letters
        key_value = ord(most_frequent) - ord('E')
        
    elif 97 <= ord(most_frequent) <= 122: # For all lower case letters
        key_value = ord(most_frequent) - ord('e')

    code_file.close

    return key_value


def vigenere_crack(filename):
    '''(string of filename) --> string
    Returns a key by breaking the code in a ciphered file by the file name provided
    >>> print vigenere_crack('mystery_challenge.txt')
        COMPUTER
    '''

    code_file = open(filename)

    list_of_dict = [{},{},{},{},{},{},{},{}] #List of dictionaries where each dictionary represent
                                             #an index of the keywhich was used to cipher

    index = 0
    i = 0
    j = 0
    list_of_keys = []
    
    
    for line in code_file:
        line = line.replace("\n"," ")
        for letter in line:
            if letter in list_of_dict[i] and letter != " ": #If letter is present in the dictionary
                list_of_dict[i][letter] += 1
                i = (i + 1) % 8                             #Ensures that letter is added to appropriate dictionary
            elif letter not in list_of_dict[i] and letter != " ": #if letter is not present in the dictionary
                list_of_dict[i][letter] = 1
                i = (i + 1) % 8
        

    for dictionary in list_of_dict: #This for loop inverses all the dictionaries in the list
        new_dict = {}

        for letter in dictionary:
            new_dict[dictionary[letter]] = letter
        
        list_of_dict[index] = new_dict
        index += 1
    
    for dictionary in list_of_dict: #For every dictionary's most occuring letter
        if 65 <= ord(dictionary[max(dictionary)]) <= 91: # For all capital letters
            list_of_keys += [chr(ord(dictionary[max(dictionary)]) - ord('E') + 65)] #Saves the chracter of the key calculated
            
        elif 97 <= ord(dictionary[max(dictionary)]) <= 122: # For all lower case letters
            list_of_keys += [chr(ord(dictionary[max(dictionary)]) - ord('e') + 65)]
  
          
    return ''.join(list_of_keys) #Returns concatenated list


def main():
    '''() --> None
    Function asks the user for inputs, calls relevantt functions and writes results to files
    '''
    user_req = raw_input("Do you want to (c)ipher, (d)ecipher? or (cr)ack? ")
    
    if user_req == "c" or user_req == "C":
        cipher_req = raw_input("Which cipher (c)easer or (v)igenere? " )
        key = int(raw_input("Enter key: "))
        read_file = raw_input("Name of file to read: ")
        write_file = raw_input("Name of file to write: ")
         
        if cipher_req == "c" or cipher_req == "C":
            key = int(key)
            line_list = ceaser(read_file,key)
        elif cipher_req == "v" or cipher_req == "V":
            key = vigenere_key(key)
            line_list = vigenere(read_file,key)

        write_to_file(write_file, line_list)
        
    elif user_req == "d" or user_req == "D":
        cipher_req = raw_input("Which cipher (c)easer or (v)igenere? " )
        key = raw_input("Enter key: ")
        read_file = raw_input("Name of file to read: ")
        write_file = raw_input("Name of file to write: ")
        
        if cipher_req == "c" or cipher_req == "C":
            key = 26 - int(key)                              #No need for helper function as calculation for decipher key is simple
            line_list = ceaser(read_file,key)
            
        elif cipher_req == "v" or cipher_req == "V":
            key = vigenere_rotate_key(key)              #Helper function called to calculate decipher key values here
            line_list = vigenere(read_file,key)
        
        write_to_file(write_file, line_list)
        
    elif user_req == "cr" or user_req == "CR":
        crack_req = raw_input("Which cipher (c)aeser or (v)ignere? ")
        read_file = raw_input("Name of file to read: ")

        if crack_req == 'c':
            key = crack_code(read_file)
        elif crack_req == 'v':
            key = vigenere_crack(read_file)

        print "I cracked the code! The key is", key
            
    return

main()
