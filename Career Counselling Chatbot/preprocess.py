import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return filtered_tokens

# Example usage
if __name__ == "__main__":
    sample = "I am interested in technology and programming!"
    print(preprocess_text(sample))
