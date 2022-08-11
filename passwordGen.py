import random,secrets
def GeneratePassword_Ascii(length:int)->str:
    i=0
    output=[]
    while i<length:
        rnum=random.randint(33,126)
        mychar=chr(rnum)
        output.append(mychar)
        i+=1
    stroutput=''.join(output)
    return stroutput


def Generate_Password(length:int,characters:str):
    #characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS!@#$%^&*()_+123456789"
    characters=list(characters)
    outputlist=[]
    i=0
    while i<length:
        
        mychar=secrets.choice(characters)
        outputlist.append(mychar)
        i+=1
    return ''.join(outputlist)


