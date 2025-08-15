class TxtFile:
    def __init__(self,file_path):
        self.path=file_path

    def read_line(self):
        with open(self.path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line[0:-1])

    def write_line(self,increase):
        with open(self.path, "w") as file:
            file.write("Hello, World\n")
            file.write("Hello, World\n")

def main():
     filePath = r"C:\Users\DELL\Documents\02082025_SoftwareEngineering\3week\demo.txt"
     p1=TxtFile(filePath)
     p1.read_line()
     #p1.write_line()
    


if __name__=="__main__":
    main()