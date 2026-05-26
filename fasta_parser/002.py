"""
FASTA Project Parser
Date: 03.05.2026

Reads a multi-FASTA file and returns a dictionary:
{header: sequence}
"""

import os


def parse_fasta(file_path):

    try:

        sequences = {}  # Dictionary to store results
        header = None   # Current sequence header
        seq_list = []   # Temporary list to collect sequence lines

        with open(file_path, "r") as f:  # Open FASTA file for reading

            for line in f:  # Read file line by line
                line = line.strip()  # Remove spaces and \n

                if not line:  # Skip empty lines
                    continue

                if line.startswith(">"):  # Header line

                    # Save previous sequence before new header
                    if header:
                        sequences[header] = "".join(seq_list)

                    header = line[1:]  # Remove ">"
                    seq_list = []  # Reset sequence collector

                else:
                    seq_list.append(line)  # Add DNA/protein line

            # Save last sequence after loop ends
            if header:
                sequences[header] = "".join(seq_list)

        return sequences

    except FileNotFoundError:
        print("File not found!")
        return None


# Get current script directory
BASE_DIR = os.path.dirname(__file__)

# Build FASTA file path
fasta_path = os.path.join(BASE_DIR, "multiple_seq.fasta")

# Parse FASTA file
data = parse_fasta(fasta_path)

# Print results safely
if data is not None:

    for header, seq in data.items():

        print("=" * 50)
        print("HEADER:", header)
        print("LENGTH:", len(seq))
        print("SEQUENCE:", seq)