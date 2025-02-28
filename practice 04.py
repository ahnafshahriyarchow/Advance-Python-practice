
import random


def write_short_story(input_dict, n, target_word):


    def generate_sentence():

        a = random.choice(input_dict['article']).capitalize()
        b = random.choice(input_dict['noun'])
        c = random.choice(input_dict['verb'])
        d = random.choice(input_dict['preposition'])
        e = random.choice(input_dict['article'])
        f = random.choice(input_dict['noun'])

        return f"{a} {b} {c} {d} {e} {f}."
    
    sentences = []
    for i in range(n):
        sentences.append(generate_sentence())

    out_story = ' '.join(sentences)

    word_ct = out_story.lower().split().count(target_word.lower())

    return out_story, word_ct