"""[4-19-2014] Challenge #154 [Intermediate] Gorellian Alphabet Sort
"""
s = """5 ZYXWVuTSRQpONMLkJIHGFEDCBa
go
aLL
ACM
teamS
Go"""

s = s.split("\n")
count, order = s[0].split(" ")
order = order.upper()
if len(order) < 26:
    raise IOError("Missing alphabets!")
if len(order) > 26:
    dups = set(list(filter(lambda x: order.count(x) > 1, order)))
    raise IOError(f"Duplicate alphabets: {' '.join(dups)}")

words = s[1:]
print("unordered =>", *words, sep=" ")
words.sort(key=lambda word: [order.index(w.upper()) for w in word])
print("Ordered =>", *words, sep=" ")
