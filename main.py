import re


# reference paper used: https://web.stanford.edu/~jurafsky/slp3/3.pdf

def create_word_list(text, add_markers):
    text = text.replace(".", " </s> <s>")  # add markers for start and end of sentence
    text = re.sub(r'[^a-zA-Z0-9</>\s]', ' ', text)  # replaces all non-alphanumerics with spaces, creating duplicate
    # spaces
    text = re.sub('[\n, \t]', ' ', text)
    # ^ means not in and the list is of all alphanumeric characters
    text = re.sub(" +", " ", text)  # removes any duplicate whitespace
    words_list = text.lower().split(" ")
    if add_markers:
        words_list.insert(0, "<s>")
        if words_list[-1] == "<s>": # period at end of sentence will create extraneous start marker
            words_list.pop(-1)
        if words_list[-1] != "</s>":  # if there was no period at the end of the last sentence, we have to make sure
            # the ending marker is added
            words_list.append("</s>")
    print(words_list)
    return words_list


def create_grams(n, words):
    gram_list = []
    if n == len(words):  # prevent nothing being returned if n = the amount of words in text
        gram_list.append(words)
        return gram_list
    i = 0
    while i < len(words) - (n - 1):  # goes to the value n before the end of the word list, then creates that last
        # n-gram. Fits just right due to going back the right amount
        gram = []
        x = 0
        while x < n:
            gram.append(words[i + x])
            x += 1
        i += 1
        gram_list.append(gram)
    return gram_list


# check how many times target_gram occurs in the corpus
def gram_probability(target_gram, corpus_grams):
    gram_count = 0
    for gram in corpus_grams:
        if gram == target_gram:
            gram_count += 1
    first_word_count = 0
    # to normalize the data, we have to divide the count of the gram's occurrences by the amount of times the gram's
    # first word occurs in the entire corpus
    for gram in corpus_grams:
        if gram[0] == target_gram[0]:
            first_word_count += 1
    if first_word_count == 0:
        first_word_count = 1  # prevent division by 0. If a word in the gram does not even exist, the gram should
        # return 0 probability anyway since gram_count will be 0
    return gram_count / first_word_count


# with an n value of 2, P(when | has two possible orientations) = P(two | has) * P(possible | two) * P(orientations |
# possible) * P(when | orientations)
def calculate_probability(n, corpus, find_prob, find_prob_is_sentence_input):
    corpus_grams = create_grams(n, create_word_list(corpus, True))
    if find_prob_is_sentence_input == "True":
        find_prob_is_sentence = True
    else:
        find_prob_is_sentence = False
    find_prob_grams = create_grams(n, create_word_list(find_prob, find_prob_is_sentence))
    probability = 1
    for gram in find_prob_grams:
        # calculate the total probability of all the grams
        probability *= gram_probability(gram, corpus_grams)
    return probability


corpus = input("Please enter a training corpus. ")
while True:
    find_prob = input("Please enter a phrase or sentence to determine the probability of. ")
    find_prob_is_sentence = input("Did you type a sentence? Please enter True if so, enter False if you typed in a "
                                  "phrase. ")
    n = input("Please enter an n value. ")
    print("The probability of finding that phrase, based off the entered corpus, is: ",
          calculate_probability(int(n), corpus, find_prob, find_prob_is_sentence) * 100, "%")
    should_continue = input("Would you like to enter another sentence and n value? ")
    if should_continue == "no" or "No":
        exit()
# https://web.stanford.edu/~jurafsky/slp3/3.pdf
