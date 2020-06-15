word_size = 16
key_rev = [0x0908, 0x1110, 0x1918]

result_x = 0x8e3b
result_y = 0xeebb


def left_circular_shift(num, bits):
    shift_mask = (2 ** word_size) - 1
    return ((num << bits) & shift_mask) | (num >> (word_size-bits))

def right_circular_shift(num, bits):
    shift_mask = (2 ** word_size) - 1
    return (num >> bits) | (num << (word_size-bits) & shift_mask)

def split(plaintext):
    mask = (2 ** word_size) - 1
    x = (plaintext >> word_size) & mask
    y = plaintext & mask
    return x, y

def Simon_round(plaintext, ks):
    x, y = split(plaintext)
    for i in range(3):
        tmp = x
        x = y ^ (left_circular_shift(x,1) & left_circular_shift(x,8)) ^ left_circular_shift(x,2) ^ ks[i]
        y = tmp
    return int(hex(x) + hex(y)[2:], 16)

def decrypt(cipherText):
    x, y = split(cipherText)
    for i in range(3):
        tmp = y
        y = x ^ (left_circular_shift(y,1) & left_circular_shift(y,8)) ^ left_circular_shift(y,2) ^ key_rev[i]
        x = tmp
    return x,y

def generator(pt, ks):
    pt = (34 - len(bin(pt))) * '0' + bin(pt)[2:]
    pt_list = [pt]
    for i in range(len(pt)):
        pt_list.append(pt[:i] + str(int(pt[i]) ^ 1) + pt[i+1:])
    new_pt_list = []
    for i in pt_list:
        new_pt_list.append('0b' + i)
    ct_list = []
    for i in new_pt_list:
        x = bin(Simon_round(int(i, 2), ks))
        y = x[:2] + '0' * (34 - len(x)) + x[2:]
        ct_list.append(y)
    new_ct_list = []
    for i in ct_list:
        new_ct_list.append(i[2:])
    plain = []
    for i in pt_list:
        plain.append([i[:(len(i)+1)//2], i[(len(i)+1)//2:]])
    cipher = []
    for i in new_ct_list:
        cipher.append([i[:(len(i)+1)//2], i[(len(i)+1)//2:]])
    return plain, cipher







