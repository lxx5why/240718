# 게임 캐릭터 만들기
# 게임 캐릭터 생성 클래스는 아이디, 성별, 직업 정보를 가지며,
class Game:
    def __init__(self, id, sex, job):
        self.game_id = id
        self.game_sex = sex
        self.game_job = job
# 기본 공격 함수를 갖는다.
    def attack(self, beta_id):
# 기본 공격 함수는 사용시 '공격!' 문자열을 화면에 출력한다.
        print(self.game_id, "(이)가", beta_id, "(을)를 공격했다...!")
cha = Game("킹왕짱", "여", "마법사")
cha.attack("망나뇽")