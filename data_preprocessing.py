import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Function to remove URLs
def remove_urls(text):
    url_pattern = re.compile(r'http[s]?://\S+|www\.\S+')
    return url_pattern.sub('', text)

# Function to remove words containing numbers
def remove_words_with_numbers(text):
    return re.sub(r'\b\w*\d\w*\b', '', text)

# Function to remove special characters
def remove_special_characters(text):
    return re.sub(r'[^A-Za-z0-9\s]', '', text)

# Function to remove extra spaces
def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()

# Function to remove stop words
def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    return ' '.join(word for word in text.split() if word.lower() not in stop_words)

# Function to perform lemmatization
def lemmatize_words(text):
    lemmatizer = WordNetLemmatizer()
    return ' '.join(lemmatizer.lemmatize(word) for word in text.split())

# Step 1: Read the text from the file
with open('captions.txt', 'r') as file:
    text = file.read()

# Step 2: Remove URLs from the text
text_without_urls = remove_urls(text)

# Step 3: Remove newline characters from the text
text_without_newlines = text_without_urls.replace('\n', ' ')

# Step 4: Remove words containing numbers
text_without_numbers = remove_words_with_numbers(text_without_newlines)

# Step 5: Remove special characters
text_without_special_chars = remove_special_characters(text_without_numbers)

# Step 6: Remove extra spaces
text_without_extra_spaces = remove_extra_spaces(text_without_special_chars)

# Step 7: Remove stop words
text_without_stopwords = remove_stop_words(text_without_extra_spaces)

# Step 8: Perform lemmatization
lemmatized_text = lemmatize_words(text_without_stopwords)

# Step 9: Convert the text to lowercase
lowercase_text = lemmatized_text.lower()

# Step 10: Write the cleaned text back to the file
with open('captions.txt', 'w') as file:
    file.write(lowercase_text)

print("Data Preprocessing is succesfull and saved back to captions.txt")
