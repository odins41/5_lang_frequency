from collections import Counter
import re

def load_data(filepath):
    with open(file_path) as text_file:
        return text_file
    

def get_most_frequent_words(file_path):
    words = re.findall('\w+', open(file_path).read().lower())
    frequency = Counter(words).most_common(number_common_words)
    return frequency


if __name__ == '__main__':
    number_common_words = 10
    file_path = input('Введите путь к файлу\n')
    print ('10 самых частых слов - ',get_most_frequent_words(file_path))
    
    
