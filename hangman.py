import random 
list=["developer","programmer","architect","repository","debugging"]
word=random.choice(list)

new_word=["_"for i in range(len(word))]
print(*new_word)
attempt=6
used_letters=[]
while(attempt):
    x=input()
    x=x.lower()
    if x in used_letters:
        print("repeated letter\nenter another letter")
        continue
    else:
        used_letters.append(x)
        if x in word:
             for i in range(len(word)):
                 if x==word[i]:
                      new_word[i]=x
    
        else:
             attempt=attempt-1
        
    print(*new_word)
    if "".join(new_word)==word:
        print("CONGRATS..YOU WON!!")
        print("attempts =",(6-attempt))
        break
if attempt==0:
    print("You lost..... :(")