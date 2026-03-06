import string


ALPHA = string.ascii_uppercase
def matrice(key):
    
    ALPHA_list = list(string.ascii_uppercase)
    matrix = [[],[],[],[],[]]
    U= key.upper() #switching to upper case letters
    k = list(dict.fromkeys(U))
    
    

    for i in k:
        if i == "J":
            ALPHA_list.remove('I')
        elif i == "I":
            ALPHA_list.remove("J")

        if i in ALPHA_list:
            ALPHA_list.remove(i)
        
        
    if "I" in ALPHA_list and "J" in ALPHA_list:
        ALPHA_list.remove("J")


    for i in ALPHA_list:
        k.append(i)
    
    
    for i in range(0,len(k)):
        matrix[i//5].insert(i%5,k[i])
            
    
    return matrix

def encryption(text,key):

    matrice(key) #making of matrix
    add = []
    e_add = []
    cipher = []

    
    text = text.upper()
    text = list(text.replace(' ',''))
    

    for i in range(0,len(text),2):#adding spaces to every second space
        if text[i] == text[i+1]:
            text.insert(i+1,'X')
        

    if len(text) % 2 != 0:#checking if the length is even or not
        text.append('X')

   

    for k in range(0,len(text)):
        for i in range(0,5):
            for j in range(0,5):
                if text[k] == matrix[i][j]:
                    add.append([i,j])
    
    for i in range(0,len(add),2):   
        
        if add[i][0] == add[i+1][0]:# checking for case 1 or same row
            e_add.append([add[i][0],(add[i][1]+1)%5])
            e_add.append([add[i+1][0],(add[i+1][1]+1)%5])

            
        elif add[i][1] == add[i+1][1]: # checking for same column
            
            e_add.append([(add[i][0]+1)%5,add[i][1]])
            e_add.append([(add[i+1][0]+1)%5,add[i+1][1]])
           
            
        else:
            e_add.append([add[i][0],add[i+1][1]])
            e_add.append([add[i+1][0],add[i][1]])
    
                
    for i in range(0,len(e_add)):
        cipher.append(matrix[e_add[i][0]][e_add[i][1]])
    
    return "".join(cipher)
        

def decryption(cipher,key):
    matrice(key)
    plaintext = []
    add =  []
    e_add =[]

    for k in range(0,len(cipher)):
        for i in range(0,5):
            for j in range(0,5):
                if cipher[k] == matrix[i][j]:
                    add.append([i,j])

    for i in range(0,len(add),2):   
        
        if add[i][0] == add[i+1][0]:# checking for case 1 or same row
            e_add.append([add[i][0],(add[i][1]-1)%5])
            e_add.append([add[i+1][0],(add[i+1][1]-1)%5])

            
        elif add[i][1] == add[i+1][1]: # checking for same column
            
            e_add.append([(add[i][0]-1)%5,add[i][1]])
            e_add.append([(add[i+1][0]-1)%5,add[i+1][1]])
           
            
        else:
            e_add.append([add[i][0],add[i+1][1]])
            e_add.append([add[i+1][0],add[i][1]])

    for i in range(0,len(e_add)):
        plaintext.append(matrix[e_add[i][0]][e_add[i][1]])

    return "".join(plaintext)

def main():
    try:
        print("choose the process: 1.Encryption 2:Decryption")
        choice = int(input("enter the no. of choice"))
            
    except ValueError:
        print("invalid input")
        print("choose the one of these process: 1.Encryption 2:Decryption")
        choice = int(input("enter the no. of choice"))

    
    key = input("enter the key")


    if choice == 1:
        text = input("enter the plaintext")
        x = encryption(text,key)
        print(x)

    elif choice == 2:
        cipher = input("enter the cipher text")
        x = decryption(cipher,key)
        print(x)

    
main()