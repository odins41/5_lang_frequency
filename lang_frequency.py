from collections import Counter
import re

def load_data(filepath):
    with open(file_path) as text_file:
        text_file = open(file_path)
        text_string = text_file.read()
    return text_string
    

def get_most_frequent_words(file_path):
    words = re.findall('\w+', open(file_path).read().lower())
    frequency = Counter(words).most_common(const)
    return frequency


if __name__ == '__main__':
    const = 10
    file_path = input('Введите путь к файлу\n')
    print ('10 самых частых слов - ',get_most_frequent_words(file_path))
    
    
