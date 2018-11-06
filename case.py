
text = input('{}'.format(ru_local.TEXT_INPUT))
counter = 0
word_counter = 1

# Xenia

for i in text:
    if i == '.' or i == '!' or i == '?' or i == '...':
        counter += 1
if 5 <= counter % 10 <= 20:
    print('{}'.format(ru_local.NUMBER_OF_SENTECES), counter)
elif counter % 10 == 1:
    print('{}'.format(ru_local.NUMBER_OF_SENTECES_1), counter)
elif counter % 10 == 2 or counter % 10 == 3 or counter % 10 == 4:
    print('{}'.format(ru_local.NUMBER_OF_SENTECES_2), counter)


for i in text:
    if i == ' ':
        word_counter += 1
if 5 <= word_counter % 10 <= 20:
    print('{}'.format(ru_local.NUMBER_OF_WORDS), word_counter)
elif word_counter % 10 == 1:
    print('{}'.format(ru_local.NUMBER_OF_WORDS_1), word_counter)
elif word_counter % 10 == 2 or word_counter % 10 == 3 or word_counter % 10 == 4:
    print('{}'.format(ru_local.NUMBER_OF_WORDS_2), word_counter)

# Dariya + Arina

text = text.lower()
vowers = list(text)
w1 = vowers.count('а')
w2 = vowers.count('о')
w3 = vowers.count('и')
w4 = vowers.count('е')
w5 = vowers.count('ё')
w6 = vowers.count('э')
w7 = vowers.count('ы')
w8 = vowers.count('у')
w9 = vowers.count('ю')
w10 = vowers.count('я')
syllables = w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8 + w9 + w10

if 5 <= syllables % 10 <= 20:
    print('{}'.format(ru_local.NUMBER_OF_SYLLABLES), syllables)
elif syllables % 10 == 1:
    print('{}'.format(ru_local.NUMBER_OF_SYLLABLES_1), syllables)
elif syllables % 10 == 2 or syllables % 10 == 3 or syllables % 10 == 4:
    print('{}'.format(ru_local.NUMBER_OF_SYLLABLES_2), syllables)

# Arina

ASL = word_counter / counter
print('{}'.format(ru_local.ASL_1), ASL)

ASW = syllables / word_counter
print('{}'.format(ru_local.ASW_1), ASW)



FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)
print('{}'.format(ru_local.FRE_1), FRE)

if FRE <= 25:
    print('{}'.format(ru_local.FRE_VERY_HARD))
elif FRE > 25 and FRE <= 50:
    print('{}'.format(ru_local.FRE_HARD))
elif FRE > 50 and FRE <= 80:
    print('{}'.format(ru_local.FRE_EASY))
else:
    print('{}'.format(ru_local.FRE_VERY_EASY))