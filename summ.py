import spacy
from collections import Counter
from string import punctuation


nlp = spacy.load("en_core_web_lg")
with open('microsoftsupply', 'r') as file:
    data = file.read().replace('\n', '')
cleaned = data.lower().replace(',','').replace('.','')
doc = nlp(cleaned)
# all tokens that arent stop words or punctuations
words = [token.text
         for token in doc
         if not token.is_stop and not token.is_punct]

# noun tokens that arent stop words or punctuations
nouns = [token.text
         for token in doc
         if (not token.is_stop and
             not token.is_punct and
             token.pos_ == "NOUN")]

# five most common tokens
word_freq = Counter(words)
common_words = word_freq.most_common(10)

# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(10)

print(common_words)

