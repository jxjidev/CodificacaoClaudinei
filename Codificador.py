# SHA-1 Implementation (Simplified and Complete)

def left_rotate(n, b):
    """Performs a left rotation on a 32-bit integer n by b bits."""
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def sha1(message):

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    message_bin = ''.join(format(ord(c), '08b') for c in message)
    original_length = len(message_bin)

    message_bin += '1'
    while len(message_bin) % 512 != 448:
        message_bin += '0'
    message_bin += format(original_length, '064b')

    for i in range(0, len(message_bin), 512):
        chunk = message_bin[i:i+512]
        w = [int(chunk[j:j+32], 2) for j in range(0, 512, 32)]

        for j in range(16, 80):
            w.append(left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1))

        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main loop
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff


    digest = (h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4
    return hex(digest)[2:]

message = "Hello, SHA-1!"
hash_result = sha1(message)
print("SHA-1 Hash:", hash_result)
