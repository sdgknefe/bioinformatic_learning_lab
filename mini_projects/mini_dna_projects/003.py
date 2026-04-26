import random

random.seed(42) # Controls randomness so results are reproducible every time the code runs

# Create Random DNA String

def random_dna(min_len, max_len):

    bases = "ATGC" # List for random dna string

    length = random.randint(min_len, max_len)
    
    return ''.join(random.choices(bases, k=length))

# Counting DNA Nucleotides

def base_content(dna):

    a = t = g = c = 0
    
    for base in dna:
        if base == "A":
            a += 1
        elif base == "T":
            t += 1
        elif base == "G":
            g += 1
        elif base == "C":
            c += 1

    return a, t, g, c

# Transcribing DNA into RNA

def dna_rna(dna):
    
    return dna.replace("T", "U")

# Report 

def report(dna):

    a, t, g, c = base_content(dna)
    rna = dna_rna(dna)
    gc = (g + c) / len(dna) * 100

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


dna = random_dna(25, 50) 

report(dna)

