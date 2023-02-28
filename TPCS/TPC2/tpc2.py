import sys

def concatNumList(l):

    num = ['']
    k = 0
    for i in range(len(l)):
        num[0] += l[i]

    return num   

def reader(inp):
    print("")
    i = 0
    flag = 0
    sum = 0
    l = []
    numb = []
    concatL = []
    l = list(inp.split(" "))
    for i in range(0,len(l)):
        strin = l[i]
        for j in range (0,len(strin)):
            if(j< len(strin)-1 and strin[j].upper() == 'O' and strin[j+1].upper() == 'N'):
                print("» SUM ON...")
                flag = 0
   
            elif(j < len(strin)-2 and strin[j].upper() == 'O' and strin[j+1].upper() == 'F' and strin[j+2].upper() == 'F'):
                print("» SUM OFF...")
                flag = 1
     
            if(flag == 0):
                if(strin[j].isdigit()):
                    numb.append(strin[j])
                else:
                    if(numb != []):      
                        concatL = concatNumList(numb)
                        numb = []
                        sum += int(concatL[0])
                if(strin[j] == "="):
                    print(f"[SUM => {sum}]")        
            if(flag == 1):
                if(numb != []):
                    concatL = concatNumList(numb)
                    numb = []
                    sum += int(concatL[0])
                if(strin[j] == "="):
                    print(f"[SUM => {sum}]")
  

def main():

   while(1):
    print("")
    reader(inp = input("Digite o texto: "))
    
if __name__ == "__main__":
    main()