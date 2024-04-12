def complement_dna(dna):
    complement = ""
    for symbol in dna:
        if symbol == "A":
            complement += "T"
        elif symbol == "T":
            complement += "A"
        elif symbol == "C":
            complement += "G"
        elif symbol == "G":
            complement += "C"
    return complement