from chord import Chord
from chordlist import chords
import random


print('\nEnter [q] to quit.\n')
inp = ''
while inp != 'q':
    ch = random.choice(chords)
    print('===================\n')
    print('What chord is this?\n')
    fingering = '\n'.join(str(ch).split('\n')[2:-1])
    print(fingering)
    inp = input()
    if inp.lower() == 'q': break
    if inp.lower().replace(' ', '') == ch.name.lower().replace(' ', ''):
        print('\nBoom! You got it!\n')
    else:
        print('\nNope, try your luck with another chord.\n')