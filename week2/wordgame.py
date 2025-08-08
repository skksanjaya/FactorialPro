import random;

fullword=""
empword=""

def random_word():
    words = ["apple", "banana", "cherry", "dragonfruit", "elderberry"]
    random_word = random.choice(words)
    return random_word

def blank_word(wordemp):
    blanks = "_" * len(wordemp)
    return blanks

if __name__ == "__main__":
    fullword=random_word()
    empword=blank_word(fullword)

    name = input("Enter your letter: ")
    i=0
    while i < len(fullword):
    if name== fullword[0]
    i +=1


    

