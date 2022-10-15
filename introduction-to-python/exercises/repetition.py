def append_each_letter_of_the_word_in_a_list(word):
    list = []
    for letter in word:
        list.append(letter)
    return list


def return_index_of_the_uppercase_letter(word):
    for letter in word:
        if letter.isupper():
            return word.index(letter)


def return_element_from_list_that_is_string(input_list):
    for element in input_list:
        if isinstance(element, str):
            return element
