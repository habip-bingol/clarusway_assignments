sentence = input("Enter a sentence please : ").lower()
letters = {}
for i in sentence:
    if i not in letters:
        letters[i] = sentence.count(i)
    
print(letters)
