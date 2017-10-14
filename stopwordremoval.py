
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sesntence="this is an example showing off tokenise nltk stuffs"

stop_words=set(stopwords.words("english"))

words = word_tokenize(sesntence)

# filtered_sentence = []

# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)

# print(filtered_sentence)


filtered_stuff=[ w for w  in words if not w in stop_words]
print(filtered_stuff)