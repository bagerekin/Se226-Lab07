from string_package import reverse_string, capitalize_words, remove_punctuation, count_characters, count_words, average_word_length

sentence = input("Enter a sentence: ")

reversed_s = reverse_string(sentence)
capitalized_s = capitalize_words(sentence)

print("Reversed sentence:", reversed_s)
print("Capitalized sentence:", capitalized_s)

clean_s = remove_punctuation(sentence)
char_count = count_characters(clean_s)
word_count = count_words(clean_s)
avg_length = average_word_length(clean_s)

print("\nAfter removing punctuation:", clean_s)
print("Number of characters:", char_count)
print("Number of words:", word_count)
print("Average word length:", avg_length)
