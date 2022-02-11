a = []

for i in range(10):
    a.append(str(i).zfill(4))

dic = ['말괄양이', '삐삐', '너는바보', '개빡치네', '내가CTO?', '바', '사', '아', '자']


def number_to_string(number) -> str:
    uu = a.index(number)
    return dic[uu]

dd = number_to_string('0001')
print(dd)