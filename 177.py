"""[8/27/2014] Challenge #177 [Intermediate] .- ..- -.. .. ---"""
import wave, struct, math, random

MORSE_CODE = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--.", "-----", ".----", "..---",
    "...--", "....-", ".....", "-....", "--...", "---..", "----."
]

def get_code(char):
    return MORSE_CODE[ord(char)-97]

output = []

if __name__ == "__main__":
    INPUT = "hello morse code".lower()
    for char in INPUT:
        if char == " ":
            output.append(char)
        else:
            output.append(get_code(char))

print("".join(output))


sample_rate = 44100

wav_file = wave.open('./results/177.wav', 'w')
wav_file.setparams((1, 2, sample_rate, 0, "NONE", "not compressed"))

def make_sine(freq=440, datasize=7500, frate=44100.00):
    # global wav_file
    amp = 8000.0
    sine_list = []
    for x in range(datasize):
        sine_list.append(math.sin(2*math.pi * freq * (x/frate)))
    for s in sine_list:
        wav_file.writeframes(struct.pack('h', int(s*amp/2)))

for m_code in output:
    for letter in m_code:
        if letter == ".":
            make_sine(440)
            make_sine(0, 2500)
        elif letter == "-":
            make_sine(440, 20000)
            make_sine(0, 2500)
        else:
            make_sine(0, 10000)

wav_file.close()
