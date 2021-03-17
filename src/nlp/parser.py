from konlpy.tag import Mecab


def parse_as_nouns_with_konlpy(text):
    # print('text in konlpy.nouns(text): {}'.format(text))
    # return text
    mecab = Mecab()
    return mecab.nouns(text)
