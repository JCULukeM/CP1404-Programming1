
sentence = {}


def main():
    text_sentence = input("What is the sentence: ")
    words = text_sentence.split()
    for word in words:
        frequency = sentence.get(word, 0)
        sentence[word] = frequency + 1

    words = list(sentence.keys())
    words.sort()

    max_length = max((len(word)for word in words))
    for word in words:
        print("{:{}} : {}".format(word, max_length, sentence[word]))


main()