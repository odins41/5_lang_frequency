from collections import Counter
import re

def load_data(filepath):
    with open(filepath) as text_file:
        text = text_file.read()
        text = text.lower()
        return text
    

def get_most_frequent_words(text_file):
    most_frequent_words = []
    number_common_words = 10
    all_words = re.findall('\w+', text_file)
    frequency = Counter(all_words).most_common(number_common_words)
    for words in frequency:
         most_frequent_words.append(words[0])    
    return most_frequent_words


if __name__ == '__main__':
    file_path = input('Введите путь к файлу\n')
    text_file = load_data(file_path) 
    print ('10 самых частых слов - ', get_most_frequent_words(text_file))
    
    
