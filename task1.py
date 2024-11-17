import nltk
from nltk.corpus import gutenberg
import string
import matplotlib.pyplot as plt
from collections import Counter

# Завантажуємо необхідні ресурси
nltk.download('gutenberg')
nltk.download('stopwords')

# Функція для токенізації тексту
def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    return tokens

# Функція для побудови стовпчастої діаграми
def plot_bar_chart(words, counts, title):
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Слова')
    plt.ylabel('Частота')
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.show()

# Функція для видалення стоп-слів і пунктуації
def remove_stopwords_punctuation(tokens):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]
    return filtered_tokens

# Завантажуємо текст з Project Gutenberg
file_id = 'austen-persuasion.txt'
text = gutenberg.raw(file_id)

# Видалення пунктуації
text = text.translate(str.maketrans('', '', string.punctuation))

# Токенізація тексту
tokens = tokenize_text(text)

# Підрахунок кількості слів
total_words = len(tokens)
print(f"Кількість слів у тексті: {total_words}")

# Меню для користувача
while True:
    print("\nОберіть опцію:")
    print("1. Побудувати діаграму 10 найбільш вживаних слів (без пунктуації)")
    print("2. Побудувати діаграму 10 найбільш вживаних слів (після видалення стоп-слів та пунктуації)")

    choice = input("Ваш вибір: ")

    if choice == '1':
        # Підрахунок найбільш вживаних слів без фільтрації
        word_counts = Counter(tokens)
        common_words = [word for word, _ in word_counts.most_common(10)]
        plot_bar_chart(common_words, [word_counts[word] for word in common_words], '10 Найбільш Вживаних Слів (без пунктуації)')

    elif choice == '2':
        # Видалення стоп-слів та пунктуації
        filtered_tokens = remove_stopwords_punctuation(tokens)
        filtered_word_counts = Counter(filtered_tokens)
        filtered_common_words = [word for word, _ in filtered_word_counts.most_common(10)]
        plot_bar_chart(filtered_common_words, [filtered_word_counts[word] for word in filtered_common_words], '10 Найбільш Вживаних Слів (після видалення стоп-слів та пунктуації)')
