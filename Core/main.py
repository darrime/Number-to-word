import sqlite3

a = []

for i in range(10000):
    a.append(str(i).zfill(4))


conn = sqlite3.connect("C:\\Dev\\Python\\Number-to-word\\kr_korean.db")

cursor = conn.cursor()

cursor.execute('''select * from kr where part='명사' ''')
words = cursor.fetchall()


def number_to_string(number) -> str:
    return words[int(number)]



phone_number = input("전화번호 뒷자리를 입력하세요\n")


woo = number_to_string(phone_number)
print(woo[1])
#TODO 숫자-단어 매칭 알고리즘을 어떻게 할지
#TODO 단어 필터링