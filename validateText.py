import difflib
import re
import string

with open('vocab.txt', 'r', encoding='utf-8') as f:
    vocab = set(f.read().split('\n'))

with open('stopword.txt', 'r', encoding='utf-8') as f:
    stopword = set(f.read().split('\n'))


def text_cleaning(sent1, sent2):

    sent1 = re.split('([\d]+[.,\d]+)|([\d]*[.][\d]+)| |([\d]+)|(\W)', sent1)
    sent2 = re.split('([\d]+[.,\d]+)|([\d]*[.][\d]+)| |([\d]+)|(\W)', sent2)

    sent1 = [ele for ele in sent1 if ele not in stopword and ele is not None and ele not in string.punctuation ]
    sent2 = [ele for ele in sent2 if ele not in stopword and ele is not None and ele not in string.punctuation ]

    new_sent1 = '_'.join(sent1)
    new_sent2 = '_'.join(sent2)

    return new_sent1, new_sent2


def get_overlap_size(s1, s2):
    s = difflib.SequenceMatcher(None, s1, s2)
    pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2))

    return size


def validate(s1, s2):
    list_s2 = s2.split()

    if len(list_s2) < 3:
        err_code = 1
        err_txt = 'Câu quá ngắn, vui lòng thử lại.'
        return err_code, err_txt

    for word in list_s2:
        if word not in vocab and not word.isdigit():
            err_code = 2
            err_txt = 'Vui lòng kiểm tra lại cú pháp: ' + word
            return err_code, err_txt

    new_s1, new_s2 = text_cleaning(s1, s2)
    size_overlap = get_overlap_size(new_s1, new_s2)
    maxlen = max(len(new_s1), len(new_s2))

    print(size_overlap)
    if size_overlap >= (maxlen * 9 // 10):
        err_code = 3
        err_txt = 'Câu trùng lặp với câu gốc, vui lòng thử lại.'
        return err_code, err_txt
    else:
        err_txt = 'OK'
        err_code = 0
        return err_code, err_txt
