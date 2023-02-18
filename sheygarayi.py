
import stdio


def translate(dna):
    dna = dna.upper()
    rna = dna.replace("T", "U")
    return rna


if __name__ == '__main__':
    dna = 'ATGCGGTACTTQA'
    rna = translate(dna)
    stdio.writeln(rna)
