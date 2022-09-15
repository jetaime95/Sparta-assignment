'''
프로필 관리 기능 만들어보기
- 사용자들의 프로필을 관리할 수 있는 클래스를 선언해주세요
- 메소드를 호출해서 사용자의 프로필을 설정할 수 있도록 해주세요
- 사용자의 정보를 각각 출력할 수 있는 메소드를 만들어주세요
'''

class Profile:
    def __init__(self):
        self.profile = {
            "name": "-",
            "gender": "-",
            "birthday": "-",
            "age": "-",
            "phone": "-",
            "email": "-",
        }
    
    def set_profile(self, profile):
        self.profile = profile
        
    def get_name(self):
        name = self.profile.get("name")
        return name
    
    def get_gender(self):
        gender = self.profile.get("gender")
        return gender
    
    def get_birthday(self):
        birthday = self.profile.get("birthday")
        return birthday
    
    def get_age(self):
        age = self.profile.get("age")
        return age
    
    def get_phone(self):
        phone = self.profile.get("phone")
        return phone
    
    def get_email(self):
        email = self.profile.get("email")
        return email
    
    
profile = Profile()
profile.set_profile({
    "name": "lee",
    "gender": "man",
    "birthday": "01/01",
    "age": 32,
    "phone": "01012341234",
    "email": "python@sparta.com",
})

print(profile.get_name()) # 이름 출력
print(profile.get_gender()) # 성별 출력
print(profile.get_birthday()) # 생일 출력
print(profile.get_age()) # 나이 출력
print(profile.get_phone()) # 핸드폰번호 출력
print(profile.get_email()) # 이메일 출력
