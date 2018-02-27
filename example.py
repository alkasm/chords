from chord import Chord

chords = [
    Chord('A Maj', 'x02220', '213'),
    Chord('A7', 'x02020', '12'),
    Chord('A min', 'x02210', '231'),
    Chord('A min7', 'x02x10', '21'),
    Chord('A Maj7', 'x02120', '213'),
    Chord('Bb Maj', 'x1333x', '1234'),
    Chord('B7', 'x21202', '2134'),
    Chord('B min', 'x2443x', '1342'),
    Chord('C Maj', 'x32010', '321'),
    Chord('C7', 'x32310', '3241'),
    Chord('C Maj7', 'x32000', '32'),
    Chord('D', 'xx0232', '132'),
    Chord('D7', 'xx0212','213'),
    Chord('D min', 'xx0231','231'),
    Chord('D min7', 'xx0222','123'),
    Chord('E Maj', '022100','231'),
    Chord('E7', '020100','21'),
    Chord('E min', '022000','23'),
    Chord('E min7', '020000','2'),
    Chord('F', 'xx3211','3211'),
    Chord('F Maj7', 'xx3210','321'),
    Chord('G Maj', '320003','213'),
    Chord('G7', '320001', '321')
]



for c in chords:
    print(repr(c))
    print(c)