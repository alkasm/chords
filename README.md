## Example use:

View chord fingerings:

    >>> from chord import Chord
    >>> AMaj = Chord('A Maj', 'x02220', '213')
    >>> print(AMaj)
    ## A Maj ##

    x 0 2 1 3 0
    ╒═╤═╤═╤═╤═╕
    | | | | | |
    ├─┼─┼─┼─┼─┤
    | | █ █ █ |
    ├─┼─┼─┼─┼─┤
    | | | | | |
    ├─┼─┼─┼─┼─┤
    | | | | | |
    └─┴─┴─┴─┴─┘
    
    
Generate permutations of chords to practice chord switching:

    >>> from chord import Chord
    >>> from itertools import permutations
    >>> chords = [Chord('A', 'x02220', '213'), Chord('E', '022100','231'), Chord('D', 'xx0232', '132')]
    >>> for ch1, ch2 in permutations(chords, 2):
    ...     print(ch1.name, '---', ch2.name)
    ...
    A --- E
    A --- D
    E --- A
    E --- D
    D --- A
    D --- E
