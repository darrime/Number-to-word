import sqlite3

a = []

for i in range(10000):
    a.append(str(i).zfill(4))


conn = sqlite3.connect("D:\\Dev\\PythonProject\\Num-to-word\\kr_korean.db")

cursor = conn.cursor()

cursor.execute('''select * from kr where part='명사' ''')
subject = cursor.fetchall()

cursor.execute('''select * from kr where part='형용사' ''')
adverse = cursor.fetchall()

def number_to_string(number) -> str:
    number = number.split('-')
    first, last = int(number[1]), int(number[2])

    firstStr, lastStr = str(subject[first][1]), str(adverse[last][1])

    firstStr, lastStr = firstStr.replace('-', ''), lastStr.replace('-', '')

    return firstStr + '-' + lastStr


phone_number = input("전화번호를 입력하세요\n")


woo = number_to_string(phone_number)
print(woo)
#TODO 숫자-단어 매칭 알고리즘을 어떻게 할지
#TODO 단어 필터링