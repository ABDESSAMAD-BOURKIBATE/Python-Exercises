longest = ""
while True:
    sentence = input("Enter a sentence without the letter 'A': ")
    if "a" in sentence.lower():
        print("❌ Sentence contains 'A'. Try again!")
        continue
    if len(sentence) > len(longest):
        longest = sentence
        print("🎉 Congratulations! New longest sentence:", longest)
    else:
        print("Keep trying! Current longest sentence is still:", longest)