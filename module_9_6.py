def all_variants(text):
    text_1 = len(text)
    for sym in range(text_1):
        for j in range(sym + 1, text_1 + 1):
            yield text[sym:j]


a = all_variants("abc")
for i in a:
    print(i)
