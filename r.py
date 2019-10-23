slogan = str(input ("Write your sentence: "))
sentence = slogan [::-1]
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print(sentence_rev)
