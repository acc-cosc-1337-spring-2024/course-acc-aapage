def get_hamming_distance(dna1, dna2):
    distance = 0
    i = 0
    for letter in dna1:
        if dna1[i] != dna2[i]:
            distance += 1
        i += 1
    return distance

def get_dna_compliment(dna):
    sequence = []
    compliment = ""
    i = 0

    # create compliment
    for letter in dna:
        if dna[i] == "A":
            sequence.append("T")
        if dna[i] == "T":
            sequence.append("A")
        if dna[i] == "C":
            sequence.append("G")
        if dna[i] == "G":
            sequence.append("C")
        i += 1
    # flip list around
    sequence = sequence[::-1]

    # convert list to string in new variable
    for letter in sequence:
        compliment += letter

    return compliment