import re

def simple_sentence(sentence):
    return re.sub('[^A-Za-z0-9]', '', sentence).lower()

def number_of_characters(sentence):
    return len(sentence)

def reverse(sentence, rev_sentence = []):
    num = number_of_characters(sentence)
    if num == 0:
        return rev_sentence
    rev_sentence.append(sentence[num - 1])
    return reverse(sentence[:num - 1], rev_sentence)


def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    num = number_of_characters(sentence)
    if num <= 1:
        return True
    rev_sentence = reverse(sentence)
    return rev_sentence == list(sentence)


def main():
    # TODO: put your input/output code here
    sentence = input("Enter a phrase, sentence, or sentences: ")
    sentence = simple_sentence(sentence)
    if is_palindrome(sentence):
        print("Your entry is a palindrome")
    else:
        print("Your entry is not a palindrome")


if __name__ == '__main__':
    main()
