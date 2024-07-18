class Dog: #클래스 이름의 첫글자는 대문자
    def __init__(self, name, breed):
        self.dog_name = name
        self.dog_breed = breed
        self.dog_sex = "남"

    def bark(self):
        print(self.dog_breed, "가 짖습니다.")
# print(Dog("뽀삐", "말티즈"))
Dog("뽀삐", "말티즈").bark()