class StringManupulator:


    def find_character(self,text,char):
        return text.find(char)
    
    def find_len(self,text):
        return len(text)
    def find_up(self,text):
        return text.upper()
    
        

    
if __name__ == "__main__":
    name=StringManupulator()
    result=name.find_character('example','x')
    print(result)
    res1=name.find_len("example")
    print(res1)
    res2=name.find_up("example")
    print(res2)

    # we have to pass text one by one for methods without initializer