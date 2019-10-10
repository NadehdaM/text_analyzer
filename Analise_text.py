try:
    import os
    import pymorphy2
    import csv
    import stop_words
except:
    print("Ошибка загрузки библиотеки.")

file_name = input('Введите имя файла с расширением (например: Kipling.txt) - ')
file_dir = input('Введите путь к файлу (например: C:\\Users\Logos\PycharmProjects\HSE_python_lesson) - ')
file = os.path.abspath(file_dir + '\\' + file_name)
print(file)

file = open(file, 'r', encoding='utf-8-sig')
text = []
symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '`', '{', '}', '|', '\\', '"', '?', '>', '<', '-', '-', '–', '—' '=', '[', ']', ';', '/', '.', ',']
for line in file.readlines():
    line = line.strip().split( )
    for word in line:
        for symbol in symbols:
            word = word.replace(symbol, '')
        if word != '':
            text.append(word.lower())
file.close()

text_normal = []
morph = pymorphy2.MorphAnalyzer()
for word in text:
    word_morph = morph.parse(word)[0]
    text_normal.append(word_morph.normal_form)

from stop_words import get_stop_words
stop_words = get_stop_words('russian')
text_normal = [word for word in text_normal if not word in stop_words]
print(text_normal)

dict_count_word = {}
for word in text_normal:
    if word not in dict_count_word.keys():
        dict_count_word[word] = 1
    else:
        dict_count_word[word] = text_normal.count(word)

with open('Result.csv', 'w') as result:
    writer = csv.writer(result, delimiter=';',  lineterminator='\n')
    for key, value in sorted(dict_count_word.items(), key=lambda x: (x[1],x[0]), reverse=True):
        writer.writerow([key, value])
