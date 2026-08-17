# Loops

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 4 == 0 and i % 6 == 0:
         print("Fizzbuzz")
        elif i % 4 == 0:
           print("Fizz")
        elif i % 6 == 0:
           print("Buzz")
        else:
           print(i)

fizzbuzz(30)


def count_words(sentence):
    words = sentence.split()
    total_words = len(words)

    long_words = 0
    for word in words:
        if len(word) > 4:
            long_words += 1

    print(f"Total words: {total_words}")
    print(f"Words longer than four letters: {long_words}")

count_words("The quick brown fox jumps over the lazy dog")

   