import random

random.seed(1)

def random_dna(min_len, max_len):

    bases = "ATGC"
    length = random.randint(min_len, max_len)

    return''.join(random.choices(bases, k=length))

def base_content(dna):

    a = t = c = g = 0

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

def revers_complement(dna):
    
    revc = {"A": "T", "G": "C", "T": "A", "C":"G"}
    
    return ''.join(revc[base] for base in dna)[::-1]

def transcription(dna):
    
    return dna.replace("T", "U")

def report(dna):
    
    a, t, g, c = base_content(dna)
    rna = transcription(dna)
    revc = revers_complement(dna)

    gc = (g + c) / len(dna) * 100

    print("================= Sequence Analysis =================\n")
    print(f"DNA: {dna}\n")
    print(f"Length of DNA: {len(dna)}\n")
    print(f"Compelement DNA: {revc}\n")
    print(f"Base Content\n")
    print(f"Adenine  (A): {a} --> %{a / len(dna)* 100:.2f}")
    print(f"Thymine  (T): {t} --> %{t / len(dna)* 100:.2f}")
    print(f"Guanine  (G): {g} --> %{g / len(dna)* 100:.2f}")
    print(f"Cytosine (C): {c} --> %{c / len(dna)* 100:.2f}")
    print(f"GC Rate: %{gc:.2f}")
    print("\n=====================================================\n")
    print(f"RNA: {rna}")

dna = random_dna(100, 250)

report(dna)