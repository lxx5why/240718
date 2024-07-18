# 부동산 정보 입력 클래스.
class Ground:
# 부동산 정보 클래스는 위치, 평수, 건물의 종류, 가격, 건물이 지어진 연도 정보를 갖는다.
    def __init__(self, g, m, v, c, y):
        self.ground_g = g
        self.ground_m = m
        self.ground_v = v
        self.ground_c = c
        self.ground_y = y
# 또한, 정보 확인 함수를 사용하면
    def check(self):
# 부동산 객체에 포함된 속성 정보를 화면에 출력한다.
        print("이 부동산의 정보는", "위치:", self.ground_g, "평수:", self.ground_m, "건물의 종류:", self.ground_v, "가격:", self.ground_v, "연도:", self.ground_c, self.ground_y, "입니다.")
my_house = Ground("성수", "50평", "아파트", "100억", "2024년도")
my_house.check()