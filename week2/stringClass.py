class StringManupulator:
    def __init__(self,text):
        self.text =text

    def find_character(self,char):
        return self.text.find(char)
    
    def find_len(self):
        return len(self.text)
    def find_up(self):
        return self.text.upper()
    
if __name__ == "__main__":
    name=StringManupulator("example")
    result=name.find_character('x')
    print(result)
    res1=name.find_len()
    print(res1)
    res2=name.find_up()
    print(res2)
