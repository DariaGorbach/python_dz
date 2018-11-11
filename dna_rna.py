class Rna:

    def __init__(self, line):

        self.line = line

        if len(self.line) < 0:
            raise 'lil line'
        rna_nuc = ['A', 'G', 'C', 'U']
        for nuc in line:
            if nuc in rna_nuc:
                pass
            else:
                raise Exception('not an RNA')

    def gc(self):
        c_count = 0
        g_count = 0
        for i in self.line:
            if i == 'G':
                g_count += 1
            elif i == 'C':
                c_count += 1

        return (g_count + c_count) / len(self.line) * 100

    def reverse_complement(self):
        complement_seq = ''
        nucleotides = {
            'A': 'U',
            'G': 'C',
            'C': 'G',
            'T': 'A',
            }
        for nuc in self.line[::-1]:
            complement_seq += nucleotides[nuc]
        return complement_seq


class Dna(Rna):

    def _init_(self, line):
        
        self.line = line

        if len(self.line) < 0:
            raise 'lil line'
        rna_nuc = ['A', 'G', 'C', 'U']
        for nuc in line:
            if nuc in rna_nuc:
                pass
            else:
                raise Exception('not an RNA')
                
        self.nucleotides = {
            'A': 'T',
            'G': 'C',
            'C': 'G',
            'T': 'A',
            }

    def transcribe(self):
        transcribed_seq = ''
        transcription_dict = {
            'A': 'U',
            'G': 'C',
            'C': 'G',
            'T': 'A',
            }
        for nuc in self.line:
            transcribed_seq += transcription_dict[nuc]
        return transcribed_seq

input = str("ACGTCG")

test_rna = Rna(input)
print(test_rna.line)
print(type(test_rna.line))
print(len(test_rna.line))
print(test_rna.gc())
print(test_rna.reverse_complement())

test_dna = Dna(input)
print(test_dna.line)
print(len(test_dna.line))
print(test_dna.gc())
print(test_dna.reverse_complement())
print(test_dna.transcribe())
        

    
        