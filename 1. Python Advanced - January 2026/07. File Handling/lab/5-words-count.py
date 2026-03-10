import re

with open("words.txt", "r") as f:
    words = f.read().lower().split()

word_counts = { word: 0 for word in words }

with open("txt.txt", "r") as f:
    text = f.read().lower()

text_words = re.findall(r"\b[a-z]+\b", text)

for word in text_words:
    if word in word_counts:
        word_counts[word] += 1

sorted_words = sorted(word_counts.items(), key=lambda x: -x[1])

with open("output.txt", "w") as f:
    for word, count in sorted_words:
        f.write(f"{word} - {count}\n")