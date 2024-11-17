import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import string

# Завантаження додаткових ресурсів
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Зчитати текст з файлу
with open("input_text.txt", "r") as file:
    text = file.read()

# 1. Токенізація по словам
tokens = word_tokenize(text)

# 2. Лематизація та стемінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_words = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_words = [stemmer.stem(token) for token in tokens]

# 3. Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_words = [
    word for word in lemmatized_words if word.lower() not in stop_words
]

# 4. Видалення пунктуації
filtered_words_no_punct = [
    word for word in filtered_words if word not in string.punctuation
]

# Вивести оброблений текст в консоль
processed_text = ' '.join(filtered_words_no_punct)
print(processed_text)
