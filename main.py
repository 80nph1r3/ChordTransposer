current_chords = ['Am', 'Fmsus2', 'C', 'G']
ALL_CHORDS = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']


def transposer(tones, chord):  
    if len(chord) > 1 and chord[1] == '#':
        transposed_chord = ALL_CHORDS[
            (ALL_CHORDS.index(chord[:2]) + tones) % len(ALL_CHORDS)
            ] + chord[-1:1:-1][-1::-1]
    else:
        transposed_chord = ALL_CHORDS[
            (ALL_CHORDS.index(chord[0]) + tones) % len(ALL_CHORDS)
            ] + chord[-1:0:-1][-1::-1]
    return transposed_chord


if __name__ == '__main__':
    for chord in enumerate(current_chords):
        current_chords[chord[0]] = transposer(-1, chord[1])
    print(*current_chords)
