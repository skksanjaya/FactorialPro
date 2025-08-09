import random;

class wordGame:
    def __init__(self):
        self.fullword = None
        self.empword = None
        
    def random_word(self):
        words = ["apple", "banana", "cherry", "dragonfruit", "elderberry"]
        self.fullword = random.choice(words)

    def blank_word(self):
        self.empword = "_" * len(self.fullword)

    def print_info(self):
        print(f"fullword is {self.fullword} and empword is {self.empword} ")    
    
    def startGame(self):  
        i=0
        while i < len(self.fullword):
            name = input("Enter your letter: ")
            if name== self.fullword[0]:
                i += 1

if __name__ == "__main__":
    p1 = wordGame()
    p1.random_word()
    p1.blank_word()
    p1.print_info()
    p1.startGame()


    

