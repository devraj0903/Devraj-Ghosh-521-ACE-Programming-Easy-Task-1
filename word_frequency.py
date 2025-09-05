#word frequency counter

paragraph = input("Enter a paragraph:\n").lower()

#to keep only alphabets and spaces
cleaned = ""
for ch in paragraph:
    if ch.isalpha() or ch.isspace():
        cleaned += ch

words = cleaned.split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

freq_list = []
for word, count in freq.items():
    freq_list.append((count, word))

#for decending order by count
freq_list.sort(reverse=True)

print("\nTop 3 most frequent words:")
for i in range(min(3, len(freq_list))):
    print(freq_list[i][1], "-->", freq_list[i][0])