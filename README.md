# docker-ckiptagger

## Installation

```
docker build -t openfun/ckiptagger .
```

## Usage

```
docker run -it --rm -v "$PWD":/data -w /data openfun/ckiptagger -i input.txt -o output.jsonl --pos --ner
```

* `--pos`, `--ner` 為可選參數，詳見 https://github.com/ckiplab/ckiptagger
* 將 `input.txt` 置換成欲進行斷詞的檔名，將以行為單位進行斷詞
* 將 `ouput.jsonl` 置換成欲輸出的檔名，輸出格式為 jsonl。若有 `--pos` 或 `--ner` 參數則將產生對應的字段
