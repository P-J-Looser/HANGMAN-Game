from random import choice,randint
from support import stages,list,logo,alphabets,s
from time import sleep


lives = 7
j=randint(1,3)
hint=list[j-1][0]
new_list=list[j-1][1:]
selected = choice(new_list)
right=1;wrong=1
used = []
k=len(selected)
left=k

ans=[]
for i in range(k):
    ans.append('_')

print("Hi !  Welcome To ")
sleep(1)
print(logo)
sleep(1)
print("You have 6 Chances to save a life",'\n')
sleep(1)


print("Guess the word :",*ans,"\n")
sleep(1)
print("Lets START")



while right and wrong:
    sleep(1)
    print("\n",stages[-lives])
    sleep(1)
    print('\n',"Hint :",hint,'\n')
    letter = input("Guess a Letter : ").lower()
    if letter=="":
        sleep(1)
        print("\n","Enter a Valid letter",'\n')
        print(*ans)
        continue
    if letter not in alphabets:
        sleep(1)
        print("\n","Enter a valid letter",'\n')
        print(*ans)
        continue
    print()
    if letter in used:
        sleep(1)
        print("The Letter :",letter,"was already used")
        print(*ans)
        continue
    else:
        used.append(letter)
    if letter not in selected:
        lives=lives-1
        print("OOPS ! You Miised it ,You lost a Chance",'\n')
        sleep(1)

    else:
        sleep(1)
        print("Well Done , It's a correct Guess",'\n')
        for i in range(k):
            if selected[i]==letter:
                ans[i]=letter
                left-=1
        sleep(1)
    print("Remaining Chances :",lives-1,'\n')
    
    
    if left==0:
        right=0
    if lives==1:
        wrong=0
    print(*ans,'\n')
print() 
if wrong:
    print(s)
    print('\n',"HURRAH ! You Saved a Life ",'\n')
if right:
    print(stages[6])
    sleep(1)
    print('\n',"Nice try , G A M E   O V E R","\n\n","The Word is",selected)
    
    
            
            



 

