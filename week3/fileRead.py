class TxtFile:
    def __init__(self,file_path):
        self.path=file_path

    def read_line(self):
        with open(self.path, "r", encoding="UTF-8") as file:
            lines = file.readlines()
            for line in lines:
                print(line[0:-1])

    def write_line(self,cont):
        with open(self.path, "w", encoding="UTF-8") as file:
            file.write(cont)
            file.close()


def main():
     filePath = r"C:\Users\DELL\Documents\02082025_SoftwareEngineering\3week\demo.txt"
     p1=TxtFile(filePath)
     p1.read_line()
     p1.write_line("Hello 1 st line")
    


if __name__=="__main__":
    main()