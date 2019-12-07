# Скачайте файл по ссылке
# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt

def save_file(file, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(file)

def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        lean_text = len(text)
        print(lean_text)
        count_words = len(text.split())
        print(count_words)
        text = text.replace('.', '!')
        save_file(text, 'referat2.txt')
        
def main():
    read_file('referat.txt')
    
if __name__ == "__main__":
    main()