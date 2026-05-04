"""
Date: 03.05.2026

Reads a FASTA file and extracts the header and DNA sequence.

- Removes '>' from header
- Merges multi-line sequences into a single string

Returns:
    tuple: (header, sequence)
"""

# Open FASTA File
def read_fasta(file_path):

    try:
        with open(file_path) as f:
            lines = f.readlines()   # Read all lines

        if not lines:  # If file is empty
            return None, None

        header = lines[0].strip()[1:]  # First line is header
        sequence = "".join(line.strip() for line in lines[1:])  # Sequence lines

        return header, sequence

    except FileNotFoundError:
        print("File not found.")
        return None, None


print(read_fasta("single_seq.fasta"))