import random

random.seed(1)

# Create Random DNA String

def random_dna(min_len, max_len):

    bases = list("ATGC")
    length = random.randint(min_len, max_len)

    return ''.join(random.choices(bases, k=length))

# Counting DNA Nucleotides and %GC

def base_content(dna):
    
    a = t = c = g = 0

    for base in dna:
        if base == "A":
            a += 1
        elif base == "G":
            g += 1
        elif base == "T":
            t += 1
        elif base == "C":
            c += 1
    
    return a,t,g,c

# Transcribing DNA into RNA

def dna_rna(dna):
    return dna.replace("T", "U")

# Report

def report(dna):
    
    a, t, g, c = base_content(dna)
    gc = (g + c) / len(dna) * 100
    rna = dna_rna(dna)

    print("================ DNA REPORT =======================\n")
    print(f"DNA: {dna}")
    print("\n===================================================\n")
    print(f"Length: {len(dna)}\n")
    print(f"A: {a}")
    print(f"T: {t}")
    print(f"G: {g}")
    print(f"C: {c}")
    print(f"\nPercentage GC: {gc:.2f}%")
    print("\n====================  RNA =========================\n")
    print(f"RNA: {rna}")
    print("\n===================================================\n")

dna = random_dna(25,80)

report(dna)