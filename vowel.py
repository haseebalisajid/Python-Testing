def anti_vowel(text):
    t=""
    for c in text:
        for i in "aeiouAEIOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t
text=str(input("enter word:"))
print(anti_vowel(text))
