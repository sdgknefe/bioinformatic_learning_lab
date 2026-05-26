import random

random.seed(3) # controls randomness so results are reproducible every time the code runs

# Create Random DNA String

def random_dna(min_length, max_length):

    bases = "ATGC"
    length = random.randint(min_length, max_length)

    return ''.join(random.choices(bases, k=length))

# Counting DNA Nucleotides 

def base_count(dna):
    
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

def dna_to_rna(dna):

    return dna.replace("T", "U")

# Report

def report(dna):
    
    a, t, g, c = base_count(dna)
    
    gc = (g+c) / len(dna) * 100

    rna = dna_to_rna(dna)
    
    print("\n=================================== Sequence Analysis of DNA =============================================\n")
    print(f"DNA: {dna}")
    print("\n==========================================================================================================\n")
    print(f"Length of DNA: {len(dna)}")
    print(f"Adenine  (A): {a}, Percentage A: %{a / len(dna) * 100:.2f}")
    print(f"Thymine  (T): {t}. Percentage T: %{t / len(dna) * 100:.2f}")
    print(f"Guanine  (G): {g}. Percentage T: %{g / len(dna) * 100:.2f}")
    print(f"Cytosine (C): {c}. Percentage T: %{c / len(dna) * 100:.2f}")
    print(f"\nGC Content: %{gc}")
    print("\n==========================================================================================================\n")
    print(f"RNA : {rna}")
    print("\n==========================================================================================================")

dna = random_dna(50, 150)

report(dna)