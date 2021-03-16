import argparse
import sys
from nlp.parser import parse_by_nouns

print(sys.path)

parser = argparse.ArgumentParser(description='text tokenizer')
parser.add_argument('--language', type=str, help='target language')
parser.add_argument('--text', type=str, help='parse to nouns')

args = parser.parse_args()

language = args.language
print('language: {}'.format(language))

text = args.text
print('text: {}'.format(text))

nouns = parse_by_nouns(text)
print('nouns: {}'.format(nouns))
