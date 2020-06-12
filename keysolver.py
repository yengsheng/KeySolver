# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:26:56 2020

@author: Yong Sheng
"""

def left_circular_shift(num, bits):
    shift_mask = 2 ** num.bit_length()-1
    return ((num << bits) & shift_mask) | (num >> (num.bit_length()-bits)) 

def key_finder(plaintexts, ciphertexts):
    pass
    


important_list = ['01100101011001010110100001110111', '11100101011001010110100001110111', 
                  '00100101011001010110100001110111', '01000101011001010110100001110111', 
                  '01110101011001010110100001110111', '01101101011001010110100001110111', 
                  '01100001011001010110100001110111', '01100111011001010110100001110111', 
                  '01100100011001010110100001110111', '01100101111001010110100001110111', 
                  '01100101001001010110100001110111', '01100101010001010110100001110111', 
                  '01100101011101010110100001110111', '01100101011011010110100001110111', 
                  '01100101011000010110100001110111', '01100101011001110110100001110111', 
                  '01100101011001000110100001110111', '01100101011001011110100001110111', 
                  '01100101011001010010100001110111', '01100101011001010100100001110111', 
                  '01100101011001010111100001110111', '01100101011001010110000001110111', 
                  '01100101011001010110110001110111', '01100101011001010110101001110111', 
                  '01100101011001010110100101110111', '01100101011001010110100011110111', 
                  '01100101011001010110100000110111', '01100101011001010110100001010111', 
                  '01100101011001010110100001100111', '01100101011001010110100001111111', 
                  '01100101011001010110100001110011', '01100101011001010110100001110101', 
                  '01100101011001010110100001110110']


cipher_list = ['10001110001110111110111010111011', '10001110100110000110110010110011', 
               '00001001011000101110111000111111', '11001110000100110100111011111000', 
               '11101110011011011111111011011010', '10101110001100010110111010111011', 
               '10010110000111101000101010101011', '00110010001010111100010010110111', 
               '11011000001110101111011110111111', '10101110001101011110000000111001', 
               '11011111001111110110100010111011', '00000011001110011010110100011011', 
               '00011000011110111010111110101011', '11101101000110111101111000110011', 
               '11001011011100111110111011011111', '10000100100110111110101010001001', 
               '10011111010110011110111010101010', '00001110001101111110111010111001', 
               '10001110001111110110111011111010', '10101110111110010110111010011011', 
               '10001110000110101000111010101011', '01100110000010111101111010111011', 
               '11011110001110111111011010111111', '10111100001110111110011010111011', 
               '10011110001110011110100010111010', '10000110101110011110110010111011', 
               '00001011001110111010111100111011', '00001101000110111110111000111011', 
               '11001111011010111110111011011011', '10111110111100111110011010011011', 
               '10011110010111111110111010101011', '10000010000000011110111010110111', 
               '10001100001000111110111110111111']
