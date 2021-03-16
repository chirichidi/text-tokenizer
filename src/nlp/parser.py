from konlpy.tag import Mecab


def parse_by_nouns(text):
    # print('text in konlpy.nouns(text): {}'.format(text))
    # return text
    mecab = Mecab()
    return mecab.nouns(text)
