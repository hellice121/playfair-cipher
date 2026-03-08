import string


ALPHA = string.ascii_uppercase
def matrice(key):
    ALPHA_list = list(string.ascii_uppercase)
    matrix = [[],[],[],[],[]]
    pos = {}
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

    for i in range(5):
        for j in range(5):
            pos[matrix[i][j]] = [i,j]
    

    return pos,matrix

def algo(text,key,dir:int):
    pos,matrix =matrice(key)
    add = []
    e_add = []
    
    for i in range(0,len(text)):#adding the address
        add.append(pos[text[i]])

    
    for i in range(0,len(add),2):   
        
        if add[i][0] == add[i+1][0]:# checking for case 1 or same row
            e_add.append([add[i][0],(add[i][1]+dir)%5])
            e_add.append([add[i+1][0],(add[i+1][1]+dir)%5])

            
        elif add[i][1] == add[i+1][1]: # checking for same column
            
            e_add.append([(add[i][0]+dir)%5,add[i][1]])
            e_add.append([(add[i+1][0]+dir)%5,add[i+1][1]])
           
            
        else:# case 3
            e_add.append([add[i][0],add[i+1][1]])
            e_add.append([add[i+1][0],add[i][1]])



    return e_add,pos,matrix

def encryption(text,key):
    e_add = []
    cipher = []
    pairs =[]
    i=0
    
    text = text.upper()
    text = text.replace(' ','')
    text = list(text.replace('J','I'))
    

    while i < len(text):

        first = text[i]

        if i + 1 < len(text):
            second = text[i+1]

            if first == second:
                pairs.append([first, "X"])
                i += 1
            else:
                pairs.append([first, second])
                i += 2

        else:
            pairs.append([first, "X"])
            i += 1
    
    text = [letter for pair in pairs for letter in pair]
    

    e_add,pos,matrix = algo(text,key,+1)
    
    # adding them in the cipher to return the final output
    for i in e_add: 
        cipher.append(matrix[i[0]][i[1]])
    
    
    return "".join(cipher)
        

def decryption(cipher,key):
    plaintext = []
    cipher = cipher.upper()
    cipher = cipher.replace(' ','')
    
    
    e_add =[]

    e_add,pos,matrix = algo(cipher,key,-1) 

    for i in e_add:
        plaintext.append(matrix[i[0]][i[1]])
    
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