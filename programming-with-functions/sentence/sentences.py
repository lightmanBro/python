import random
# # Create a list of strings and assign
# # the list to a variable named words.
# words = ["boy", "girl", "cat", "dog", "bird", "house"]

# # Call the random.choice function which will choose
# # one string from the words list. Store the chosen
# # string in a variable named word.
# word = random.choice(words)
# print(word)
# word_cap = word.capitalize()

# print(word_cap)
# def main():

singular = 1
plural = 2
present = 'present'
past = 'past'

def get_determiner(quantity):
        """Return a randomly chosen determiner. A determiner is
        a word like "the", "a", "one", "some", "many".
        If quantity == 1, this function will return either "a",
        "one", or "the". Otherwise this function will return
        either "some", "many", or "the".

        Parameter
        quantity: an integer.
                    If quantity == 1, this function will return a
                    determiner for a single noun. Otherwise this
                    function will return a determiner for a plural
                    noun.
        Return: a randomly chosen determiner.
        """
        if quantity == 1:
                    words = ["a", "one", "the"]
        else:
                    words = ["some", "many", "the"]

        # Randomly choose and return a determiner.
        word = random.choice(words)
        return word.capitalize()



def get_noun(quantity):
        if quantity == 1:
                    words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
        else:
                    words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

        word = random.choice(words)
        return word.capitalize()

# print(wrd)

def get_verb(quantity, tense):
        """Return a randomly chosen verb. If tense is "past",
        this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
        If tense is "present" and quantity is 1, this
        function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
        If tense is "present" and quantity is NOT 1,
        this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
        If tense is "future", this function will return one of
        these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

        Parameters
        quantity: an integer that determines if the
                    returned verb is single or plural.
        tense: a string that determines the verb conjugation,
                    either "past", "present" or "future".
        Return: a randomly chosen verb.
        """

        if tense == 'past':
                    verb = ["drank", "ate", "grew", "laughed", "thought",
                    "ran", "slept", "talked", "walked", "wrote"]
        elif tense == 'present' and quantity == 1:
                    verb = ["drinks", "eats", "grows", "laughs", "thinks",
                    "runs", "sleeps", "talks", "walks", "writes"]

        elif tense == 'present' and quantity != 1:
                    verb = ["drink", "eat", "grow", "laugh", "think",
                    "run", "sleep", "talk", "walk", "write"]

        elif tense == 'future':
                    verb = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk",
                    "will walk", "will write"]

        vrb = random.choice(verb)
        return vrb

# def get_preposition():
#         preposition = ['In',' on', 'at', 'through', 'across', 'above', 'over', 'up', 'down', 'to', 'with', 'by', 'beside', 'beneath', 'in', 'front of', 'between', 'among',]
#         prep = random.choice(preposition)
#         return prep


def sentence():
    veb = get_verb(plural, past)
    nou = get_noun(2)
    det = get_determiner(singular)
    return f'{det} {nou} {veb}'

sent = sentence()
print(sent)
# if __name__ == '__main__':
#     main()