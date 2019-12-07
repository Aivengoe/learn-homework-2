# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(sum([*map(word.lower().count, "ауоыиэяюёе")]))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    if len(i) > 1:
      print(i[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
for i in sentence.split():
    if len(i) > 1:
      n = int(len(i) / 2) 
      print(i[0:n] ,end=" ")
    else:
      print(i ,end=" ")