from ckiptagger import data_utils, construct_dictionary, WS, POS, NER
import argparse
import os
import json

model_path = os.environ['WORKDIR'] + '/data'

# 讀取參數
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-file", type=str, required=True)
parser.add_argument("-o", "--output-file", type=str, required=True)
parser.add_argument("--pos", dest="pos", action="store_true")
parser.add_argument("--ner", dest="ner", action="store_true")
args = parser.parse_args()

# 載入模型
ws = WS(model_path)
pos = POS(model_path) if args.pos else None
ner = NER(model_path) if args.ner else None

# 輸出檔案
f = open(args.output_file, "w")

# 斷詞並輸出至檔案
def tagging(sentence_list):
    word_sentence_list = ws(
        sentence_list,                                                                                                   [25/1907]
        # sentence_segmentation = True, # To consider delimiters
        # segment_delimiter_set = {",", "。", ":", "?", "!", ";"}), # This is the defualt set of delimiters
        # recommend_dictionary = dictionary1, # words in this dictionary are encouraged
        # coerce_dictionary = dictionary2, # words in this dictionary are forced
    )
    pos_sentence_list = pos(word_sentence_list) if pos is not None else None
    entity_sentence_list = ner(word_sentence_list, pos_sentence_list) if ner is not None else None

    def print_word_pos_sentence(word_sentence, pos_sentence):
        assert len(word_sentence) == len(pos_sentence)
        for word, pos in zip(word_sentence, pos_sentence):
            print(f"{word}({pos})", end="\u3000")
        print()
        return

    for i, sentence in enumerate(sentence_list):
        #print()
        #print(f"'{sentence}'")
        #print_word_pos_sentence(word_sentence_list[i],  pos_sentence_list[i])
        #for entity in sorted(entity_sentence_list[i]):
        #    print(entity)
        data = {}

        data['ws'] = word_sentence_list[i]
        if pos_sentence_list is not None:
            data['pos'] = pos_sentence_list[i]
        if entity_sentence_list is not None
            data['ner'] = sorted(entity_sentence_list[i])

        f.write(json.dumps(data, ensure_ascii=False) + "\n")


# 載入欲斷詞的檔案
input_file = args.input_file

# 進行斷詞，每次處理 1000 筆
with open(input_file) as file:
    sentence_list = []
    for line in file:
        sentence_list.append(line.strip())
        if len(sentence_list) == 1000:
            tagging(sentence_list)
            sentence_list = []
    # 最後不足 1000 筆的資料
    tagging(sentence_list)


# 釋放記憶體
del ws
del pos
del ner
