# Writing methods
def sing_a_song():
    print(
        """A 60 ton angel falls to the earth
A pile of old metal, a radiant blur
Scars in the country, the summer and her"""
    )

def read_a_poem():
    print("""Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
“’Tis some visitor,” I muttered, “tapping at my chamber door—
            Only this and nothing more.”""")

def repeat_sentence(sentence, loops=10):
    for _ in range(loops):
        print(sentence)

def split_in_half(sentence):
    sentence_lenght = len(sentence)
    part_a = sentence[-sentence_lenght:-sentence_lenght//2]
    part_b = sentence[-sentence_lenght//2::]
    return part_a, part_b

# main method
if __name__ == '__main__':
    sing_a_song()
    read_a_poem()
    repeat_sentence('Default loops')
    repeat_sentence('Loop me 3 times', 3)

    h1, h2 = split_in_half('Kobyła ma mały bok')
    print(h1)
    print(h2)