# 문자 메시지 길이 판별 클래스
class Message:
    var = input("문자를 입력하세요: ")
    x = "내가 입력하는 문자 메시지"
    def __init__(self, len, cost1, cost2):
        self.message_len = len
        self.message_cost1 = cost1
        self.message_cost2 = cost2
    def price(self, text):
        print(text)
        if len(text) <= self.message_len:
            print(self.message_cost1)
        elif len(text) > self.message_cost2:
            print(self.message_cost2)
mms = Message(100, 50, 1000)
mms.price("임의의 텍스트입니다.")
    #     def 길이 (self, len):
    #     result =
    #     return result
    # def mul (self, a, b):
    #     result = a * b
    #     return result
# 문자 메시지 길이에 따라 문자 요금이 결정되는 프로그램을 작성하시오.
# 문자 메시지의 길이에 따라 부과되는 요금은,
# 클래스를 생성할 때 속성 정보로 갖게 된다.
# 또한, 요금이 부과될 문자 메시지의 길이를 정할 수 있도록 설정하시오. (속성 정보)
# 이 때, 사용자로부터 문자 메시지를 입력 받아서
# 문자 요금을 반환하는 코드를 작성하시오.

# if len("문자길이를 확인합니다.") <=