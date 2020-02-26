"""
Challenge #279 [Easy] Uuencoding
"""
import binascii


def get_bits(chars):
    return "".join(["{:08b}".format(ord(each)) for each in chars])


def get_24_bits_separated_chars(bits):
    # input: 24 bits // output: 4 6-bits
    bits += "0" * (24 - len(bits))
    _4_6_bits = [bits[each : each + 6] for each in range(0, 24, 6)]
    # print([int(each, 2) for each in _4_6_bits])
    return "".join([chr(int(each, 2) + 32) for each in _4_6_bits])


def separate_to_24_bits_chunk(all_bits):
    # chunks all bits to group of 24 bits
    return [all_bits[each : each + 24] for each in range(0, len(all_bits), 24)]


def separate_to_45_bytes_data(input):
    return [input[each : each + 45] for each in range(0, len(input), 45)]


def uuencode(input):
    encoded = ""
    EOL = "\n"
    for _45_chunk in separate_to_45_bytes_data(input):
        _45_byte = get_bits(_45_chunk)
        line_length = chr(len(_45_byte) // 8 + 32)
        _24_chunks = separate_to_24_bits_chunk(_45_byte)
        enc = "".join([get_24_bits_separated_chars(chunk) for chunk in _24_chunks])
        encoded += line_length + enc + EOL
    return encoded


"""
uuDECODER
"""


def uudecode(encoded):
    """
    <line length><encoded chars><EOL character>
    """
    text = ""
    curr = 0
    # print(r"{} {}".format(len(encoded), encoded))
    while curr < len(encoded):
        line_length = encoded[curr]
        block_length = (ord(line_length) - 32) * 8 // 6
        if block_length < 1:
            break
        block = encoded[curr + 1 : curr + block_length + 1]
        curr += block_length + 2
        # now we have encoded block
        # we convert it into group of 24 bits blocks
        all_bits = ""
        for char in block:
            all_bits += "{:06b}".format(ord(char) - 32)
        for _byte in [all_bits[each : each + 8] for each in range(0, len(all_bits), 8)]:
            text += chr(int(_byte, 2))
        # print(text)
    return text


s = "I feel very strongly about you doing duty. Would you give me a little more documentation about your reading in French? I am glad you are happy - but I never believe much in happiness. I never believe in misery either. Those are things you see on the stage or the screen or the printed pages, they never really happen to you in life."
# s = "Cat."


print(uudecode(uuencode(s)))
