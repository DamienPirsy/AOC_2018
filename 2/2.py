from collections import Counter

# Getting input data
with open('./input.txt') as file:
    inputs = file.readlines()

"""
part 1
"""
num_2 = 0
num_3 = 0
for line in inputs:
    c = Counter(line)
    word_has_2 = 0
    word_has_3 = 0
    for k, v in c.items():
        if v == 2:
            # just need to know if there's at least one, not how many
            word_has_2 = 1
        if v == 3:
            word_has_3 = 1
    num_2 += word_has_2 
    num_3 += word_has_3
print(num_2*num_3)


"""
part 2
"""
def compare_word(word, all_words, found):
    for w in all_words:
        diff_amount = 0
        for i in range(len(w)):
            if word[i] != w[i]:
                diff_amount +=1
            if diff_amount > 1:
                break
        if diff_amount == 1:
            found.append(w)

found = []
for line in inputs:
    compare_word(line, inputs, found)

common_letters = []
for i in range(len(found[0].strip())):
    if found[0][i] == found[1][i]:
        common_letters.append(found[0][i])

print("".join(common_letters))