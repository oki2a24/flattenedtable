# flattenedtable
エクセル等で範囲選択してコピーしたクリップボードを、1セル1行のテキストとなるように編集します。

## 使い方
```bash
pip install -r requirements.txt
# クリップボードにエクセル等のシートの任意の範囲をコピーしてから次を実行
python flattened_table.py
```

## 補足。使い方、の前の準備
```bash
git clone https://github.com/oki2a24/flattenedtable.git
cd flattenedtable
python3 -m venv venv
# Mac の場合
source venv/bin/activate
# 以上を行った後、使い方へ続く。
```
