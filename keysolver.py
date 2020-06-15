# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:26:56 2020

@author: Yong Sheng

"""
import Simon_3

def left_circular_shift(num, bits):
    shift_mask = 2 ** num.bit_length()-1
    return ((num << bits) & shift_mask) | (num >> (num.bit_length()-bits)) 

def intermediate_constant(pt_l, pt_r):
    interim_const = []
    for i in range(len(pt_l)):
        x = (int(pt_l[(i+1)%16]) & int(pt_l[(i+8)%16])) ^ int(pt_l[(i+2)%16]) ^ int(pt_r[i])
        interim_const.append(str(x))
    return ''.join(interim_const)

def formula(a, b, c, d, e):
    x = ((a & b) ^ c ^ d == e)
    return x

def k1_solver(spam):
    k = {}
    b_li = []
    for i in range(len(spam[0])):
        x = []
        for j in range(len(spam)):
            x.append(spam[j][i])
        b_li.append(x)
    for i in range(len(b_li)):
        tmp = []
        for a in range(0, 2):
            for b in range(0, 2):
                for c in range(0, 2):
                    for d in range(0, 2):
                        temp = []
                        for j in b_li[i]:
                            temp.append(formula(a ^ int(j[0]), b ^ int(j[1]), c ^ int(j[2]), d ^ int(j[3]), int(j[4])))
                        tmp.append(temp)
                        if False not in temp:
                            k[(i+1)%16] = a
                            k[(i+8)%16] = b
    k1 = []
    for i in range(16):
        k1.append(k[i])                   
    return k1

def key_finder(plaintexts, ciphertexts):
    interim_constants = []
    for j in plaintexts:
        interim_constants.append(intermediate_constant(j[0], j[1]))
    pony = []
    for i in range(len(interim_constants)):
        li = []
        for k in range(len(interim_constants[i])):
            li.append([interim_constants[i][(k+1)%16], interim_constants[i][(k+8)%16], interim_constants[i][(k+2)%16], plaintexts[i][0][k], ciphertexts[i][1][k]])
        pony.append(li)
    k1 = k1_solver(pony)
    k1_str = []
    for i in k1:
        k1_str.append(str(i))
    k1_str = ''.join(k1_str)
    ic = interim_constants[0]
    pt = plaintexts[0][0]
    ct = ciphertexts[0][1]
    ct2 = ciphertexts[0][0]
    k2 = []
    for i in range(16):
        k2.append(((int(ic[(i+1)%16]) ^ int(k1[(i+1)%16])) & (int(ic[(i+8)%16]) ^ int(k1[(i+8)%16]))) ^ int(ic[(i+2)%16]) ^ int(k1[(i+2)%16]) ^ int(pt[i]) ^ int(ct[i]))
    k2_str = []
    for i in k2:
        k2_str.append(str(i))
    k2_str = ''.join(k2_str)
    k3 = []
    for i in range(16):
        k3.append(((int(ct[(i+1)%16])) & (int(ct[(i+8)%16])) ^ int(ct[(i+2)%16]) ^ int(ic[i]) ^ int(k1[i]) ^ int(ct2[i])))
    k3_str = []
    for i in k3:
        k3_str.append(str(i))
    k3_str = ''.join(k3_str)
    k1 = hex(int(k1_str, 2))
    k2 = hex(int(k2_str, 2))[2:]
    k3 = hex(int(k3_str, 2))[2:]
    k2 = '0' * (4 - len(k2)) + k2
    k3 = '0' * (4 - len(k3)) + k3
    return k1 + k2 + k3

plaintext = 0b00000000000000000000000000000000
key_schedule = [0x1914, 0x1110, 0xa908]
plains, ciphers = Simon_3.generator(plaintext, key_schedule)
ans = key_finder(plains, ciphers)
print(ans)


