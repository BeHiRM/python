def isgen(dna):
    if (len(dna) % 3) != 0:
        return False
    if not dna.startswith('ATG'):
        return False
    for i in range(len(dna) - 3):
        if dna[i:i+3] == 'TAA':
            return False
        if dna[i:i+3] == 'TAG':
            return False
        if dna[i:i+3] == 'TGA':
            return False
    if dna.endswith('TAA'):
        return True
    if dna.endswith('TAG'):
        return True
    if dna.endswith('TGA'):
        return True
    return False


def main():
    start = sys.argv[1]
    stop = sys.argv[2]
    genome = stdio.readAll()
    beg = -1
    for i in range(len(genom) - 2):
        codon = genome[i:i+1]
        if codon == start:
            beg = i
        if codon == stop and beg != -1:
            gene = genome[beg+3:i]
            if len(gene) % 3 == 0:
                stdio.writeln(gene)
                beg = -1
