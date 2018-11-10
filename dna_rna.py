#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    line = line.rstrip()
    
class Rna(self):
    def _init_(self, line):
        self.line = line
        if len(line) < 0:
            raise ('lil line')
        elif TypeError:
            raise TypeError('not a line')
    def gc(self, line):
        c_count = 0
        g_count = 0
        for i in line:
            if i == "G":
                g_count =+ 1
            elif i == "C":
                c_count =+ 1
        return ((g_count + c_count)/len(line))*100        
    def reverse_complement(self, line):
        complement_seq = ''
        nucleotides = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'}
        for nuc in line[::-1]:
            complement_seq += nucleotides[nuc]
        return complement_seq   
        
    
class Dna(Rna):
    def _init_(self, line):
        self.nucleotides = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'} 
    def transcribe(self, line):
        transcribed_seq = ''
        transcription_dict = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'}
        for nuc in line:
            transcribed_seq += transcription_dict [nuc]
        return transcribed_seq   
            
        

    
        