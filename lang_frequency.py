from collections import Counter
import re

def load_data(filepath):
    text_file = open(file_path)
    text_string = text_file.read()
    return text_string
    

def get_most_frequent_words(file_path):
    words = re.findall('\w+', open(file_path).read().lower())
    print (Counter(words).most_common(10))
    


if __name__ == '__main__':
    file_path = input()
    get_most_frequent_words(file_path)