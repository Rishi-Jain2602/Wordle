import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def common_keywords(desc1, desc2):
    stop_words = set(stopwords.words('english'))
    if (desc1 and desc2 ):   
        tokens1 = word_tokenize(desc1.lower())
        tokens2 = word_tokenize(desc2.lower())
    else: return None
    filtered1 = {word for word in tokens1 if word.isalpha() and word not in stop_words}
    filtered2 = {word for word in tokens2 if word.isalpha() and word not in stop_words}

    common_words = filtered1.intersection(filtered2)

    return ', '.join(common_words)