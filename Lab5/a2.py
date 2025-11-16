import re

def new_text(text):
    sentences = re.split(r'(?<=[.?!]) ', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    return sentences

text = input('Введите текст: ')

my_list = new_text(text)

for sentence in my_list:
    print(sentence)

print(f'В тексте: {len(my_list)} предложений')