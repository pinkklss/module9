first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

z = zip(first, second)

first_result = (len(i) - len(j) for i, j in z if len(i) != len(j))

second_result = ((len(first[i]) == len(second[i])) for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))
