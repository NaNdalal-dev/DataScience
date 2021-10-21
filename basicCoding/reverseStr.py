sentence = "No Pain No Gain"
print('Original Sentence:',sentence)

#Split the sentence by space
splited_sentence = sentence.split(' ')
print("Splitted Sentence:",splited_sentence)

#Reverse the Splited sentence
rev_sentence = splited_sentence[::-1]
print("Reversed Sentence List:",rev_sentence)

#Join the revesed list to new string
new_sentence = ' '.join(rev_sentence)

print("Reversed Sentence:",new_sentence)

