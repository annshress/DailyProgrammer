CHROMATIC_SCALE = "C  C#  D  D#  E  F  F#  G  G#  A  A#  B"
CHROMATIC_SCALE = [each for each in CHROMATIC_SCALE.split()]

SOLFEGE_POSITIONS = "0, 2, 4, 5, 7, 9, 11"
SOLFEGE_POSITIONS = [int(each) for each in SOLFEGE_POSITIONS.split(",")]
SOLFEGE_NAMES = "Do, Re, Mi, Fa, So, La, Ti"
SOLFEGE_NAMES = [each for each in SOLFEGE_NAMES.split(", ")]

SOLFEGE_KV = {name: pos for name, pos in zip(SOLFEGE_NAMES, SOLFEGE_POSITIONS)}

def note(major, name):
  base_index = CHROMATIC_SCALE.index(major)
  distance = SOLFEGE_KV[name]
  scale_note = CHROMATIC_SCALE[(base_index + distance) % len(CHROMATIC_SCALE)]
  print("note({}, {}) is {}".format(major, name, scale_note))
  return scale_note

assert note("C", "Do") == "C", note("C", "Do")
assert note("C", "Re") == "D", note("C", "Re")
assert note("C", "Mi") == "E", note("C", "Mi")
assert note("D", "Mi") == "F#", note("D", "Mi")
assert note("A#", "Fa") == "D#", note("A#", "Fa")
