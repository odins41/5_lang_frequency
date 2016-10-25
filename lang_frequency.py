from collections import Counter
import re

def load_data(filepath):
    with open(filepath) as text_file:
        text = text_file.read()
        return text
    

def get_most_frequent_words(text_file):
    number_common_words = 10
    words = re.findall('\w+', text_file)
    frequency = Counter(words).most_common(number_common_words)
    return frequency


if __name__ == '__main__':
    file_path = input('Введите путь к файлу\n')
    text_file = load_data(file_path) 
    print ('10 самых частых слов - ', get_most_frequent_words(text_file))
    
    
