import pyperclip
import re

cb = pyperclip.paste()
# セル 1 つでリストの 1 要素とするためにタブまたは改行で区切る
cb_splited = re.split('\t|\r\n', cb)
# エクセル等のセル内で改行した場合、最初と最後に半角ダブルクォーテーションがあり、これを除去
cb_splited_striped = [
    v.strip('"') for v in cb_splited
]
cb_splited_striped_text = '\r\n'.join(cb_splited_striped)
print('クリップボードは以下の状態に編集されます。')
print(cb_splited_striped_text)
pyperclip.copy(cb_splited_striped_text)
