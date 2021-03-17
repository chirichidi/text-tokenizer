import argparse
import sys
from nlp.parser import parse_as_nouns_with_konlpy

print(sys.path)

parser = argparse.ArgumentParser(description='text tokenizer')
parser.add_argument('--language', type=str, help='target language')
parser.add_argument('--text', type=str, help='parse to nouns')

args = parser.parse_args()

language = args.language
print('language: {}'.format(language))

text = args.text
print('text: {}'.format(text))

nouns = parse_as_nouns_with_konlpy(text)
print('nouns: {}'.format(nouns))

# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_trf")

# Process whole documents
text = ("Hi. I am JongWon Lee, BI Technical Team, BI Office."
        "I am developing a morpheme tokenizer."
        "Take good care of me")
doc = nlp(text)

# Analyze syntax
print("---------------------------------- en tokenize test -----------------------------")
print("text:", text)
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
