def what_note(string, fret):
    if fret == 0: return string.upper()
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    return notes[(notes.index(string.upper()) + fret) % len(notes)]