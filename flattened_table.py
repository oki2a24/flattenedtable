import pyperclip

cb = pyperclip.paste()
print(cb)
cb_splited = cb.split('¥t')
# エクセルセル内で改行した場合、最初と最後に半角ダブルクォーテーションがあり、これを除去
cb_splited_striped = [
    v.strip('"') for v in cb_splited
]
cb_splited_striped_text = '¥r¥n'.join(cb_splited_striped)
print(cb_splited_striped_text)
pyperclip.copy(cb_splited_striped_text)
