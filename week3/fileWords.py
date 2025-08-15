class TxtFile:
    def __init__(self,file_path):
        self.path=file_path

    def file_count(self):
        with open(self.path, "r", encoding="UTF-8") as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    
def main():
     filePath = r"C:\Users\DELL\Documents\02082025_SoftwareEngineering\3week\demo.txt"
     p1=TxtFile(filePath)
     print(f"word count: {p1.file_count()}")
     

if __name__=="__main__":
    main()
