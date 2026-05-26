import random
random.seed(0)

def random_dna(min_len, max_len):
    bases = "ATGC"
    len = random.randint(min_len, max_len)
    return ''.join(random.choices(bases, k=len))

def reverse_c(dna):
    
    revc = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return ''.join(revc[base] for base in dna)[::-1]

def base_count(dna):
    a = t = g = c = 0
    for base in dna:
        if base == "A":
            a += 1
        if base == "T":
            t += 1
        if base == "G":
            g += 1
        if base == "C":
            c += 1

    return a, t, g, c

def transcription(dna):
    
    return dna.replace("T", "U")

def report(dna):
    
    a, t, g, c = base_count(dna)
    rna = transcription(dna)
    revc = reverse_c(dna)

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

dna = random_dna(50, 250)

report(dna)