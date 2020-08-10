var='''One never ought to listen to the flowers.
One should simply look at them and breathe their fragrance.
Mine perfumed all my planet. But I did not know how to take pleasure in all her grace.
This tale of claws, which disturbed me so much, should only have filled my heart with tenderness and pity.'''

space_ps = var.split('.')

char_frequency={}

for char in space_ps:
    char_frequency.setdefault(char,0)
    char_frequency[char] +=1
    print(char_frequency)
