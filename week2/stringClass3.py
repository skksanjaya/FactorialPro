class StringManupulator:
    def __init__(self,text):
        self.text =text

    def find_wordcount(self):
        words= self.text.split()
        return len(words)
    
def main():
    name=StringManupulator(input("Enter your sentence: "))
    result=name.find_wordcount()
    print(result)
    
    
if __name__ == "__main__":
        main()
