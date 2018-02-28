class Chord:
    """Holds the frets and fingerings for a chord, with nice str & repr."""

    nut   = '╒═╤═╤═╤═╤═╕'
    fret  = '├─┼─┼─┼─┼─┤'
    ffret = '└─┴─┴─┴─┴─┘'
    string = '│'
    finger = '█'


    def __init__(self, name, frets, fingers):
        """Creates the chord"""
        self.name = name
        fingers = list(fingers)
        self.fingers = [f if f in 'xX0' else fingers.pop(0) for f in frets]
        self.frets = [-1 if f in 'xX' else int(f) for f in frets]


    def __str__(self):
        """Printable form of the chord showing fingerings and frets"""
        lines = []
        lines.append('## ' + self.name + ' ##\n')
        lines.append(' '.join(c for c in self.fingers))  # print finger positions
        lines.append(Chord.nut)
        n_frets = max(4, max(self.frets))
        for i in range(1, n_frets+1):    # up to max(fret) in chord
            lines.append(' '.join(Chord.finger if f == i else Chord.string for f in self.frets))
            lines.append(Chord.ffret if i == n_frets else Chord.fret)
        lines.append('\n')
        return '\n'.join(lines)


    def __repr__(self):
        """Chord text representation"""
        fingers = ''.join([f for f in self.fingers if f not in 'xX0'])
        frets = ''.join(['x' if f == -1 else str(f) for f in self.frets])
        return '''Chord('%s', '%s', '%s')'''%(self.name, frets, fingers)
