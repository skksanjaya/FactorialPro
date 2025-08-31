class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'A'     # private
        self.__studentId = 'S0001'  

    def get_grade(self):
        return self.__grade
    
    def get_ID(self):
        return self.__studentId
    
class OnlineStudent(Student):
    def __init__(self,name, age,userName):
        self.userName = userName       # public


    
def main():
    s = Student('Ali', 20)
    print(s.name)         # accessible
    print(s._age)         # discouraged
    print(s.get_grade())  # correct way
    print(s.get_ID())

    s2 = OnlineStudent('Ali', 20, 'Ali1998')
    print(s.name)         # accessible
    print(s._age)         # discouraged
    #print(s.__grade)  # Cannot Accessible Becasue It private
    #print(s.__get_ID()) # Cannot Accessible Becasue It private



if __name__ == "__main__":
    main()
