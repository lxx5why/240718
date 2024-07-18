# 사용자의 이름, 나이, 연락처를 입력 받아서
class Info:
    def __init__(self, name, year, phone):
        self.info_name = name
        self.info_year = year
        self.info_phone = phone
# 화면에 '입력하신 이름은 ㅇㅇㅇ이며, 나이는 ㅇㅇㅇ, 그리고 연락처는 ㅇㅇㅇ-ㅇㅇㅇㅇ-ㅇㅇㅇㅇ입니다.'를 출력하는
    def check(self):
        print("입력하신 이름은", self.info_name, "이며,", "나이는", self.info_year, ", 그리고 연락처는", self.info_phone, "입니다.")
my_privacy = Info("이승연", "26살", "010-2731-6486")
my_privacy.check()
# 클래스를 작성하시오.