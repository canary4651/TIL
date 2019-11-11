# phone review raw file preprocess
import re
import pandas as pd
corpus = pd.read_csv("raw_content.csv")
data = list(corpus["content"])

REMOVE_CHARS = re.compile("(\\s|\r|\n|\t|<U\+00A0>|=|\+|/|>|<|\*|#|\[|\]|\(|\)|\\|ㅡ|;|:|!|\?|\.|,|\^|\'|\"|-|~|%|&|_|゙|゚|　)+", re.UNICODE)
EMAIL_PATTERN = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.UNICODE)
URL_PATTERN = re.compile("((ftp|http|https):\/\/)?(www.)?(?!.*(ftp|http|https|www.))[a-zA-Z0-9_-]+(\.[a-zA-Z]+)+((\/)[\w#]+)*(\/\w+\?[a-zA-Z0-9_]+=\w+(&[a-zA-Z0-9_]+=\w+)*)?$", re.UNICODE)

sentences = []
with open("data/phone_review.txt", "w", encoding="utf-8") as f1:
    for sentence in data:
        if type(sentence) == str:
            sentence = re.sub(URL_PATTERN, ' ', sentence)  # remove url pattern
            sentence = re.sub(EMAIL_PATTERN, ' ', sentence)  # remove email pattern
            sentence = re.sub(REMOVE_CHARS, ' ', sentence)  # remove unnecessary chars
            if sentence.strip():
                f1.writelines(sentence.strip() + "\n")
                sentences.append(sentence.strip())

# phone review tokenize
from konlpy.tag import Mecab
tokenizer = Mecab()


def post_processing(tokens):
    results = []
    for token in tokens:
        # 숫자에 공백을 주어서 띄우기
        processed_token = [el for el in re.sub(r"(\d)", r" \1 ", token).split(" ") if len(el) > 0]
        results.extend(processed_token)
    return results


with open("phone_review_mecab.txt", "w", encoding="utf-8") as f2:
    for sentence in sentences:
        tokens = tokenizer.morphs(sentence)
        tokenized_sent = ' '.join(post_processing(tokens))
        if tokenized_sent:
            f2.writelines(tokenized_sent + '\n')