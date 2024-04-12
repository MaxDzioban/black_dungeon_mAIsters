def DNA_strand(dna):
    # create a dictionary that maps each nucleotide to its complement
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # use a list comprehension to replace each nucleotide in the dna string with its complement
    complement_dna = ''.join([complements[nucleotide] for nucleotide in dna])
    return complement_dna

print(DNA_strand("ATTGC"))  # returns "TAACG"
print(DNA_strand("GTAT"))  # returns "CATA"
