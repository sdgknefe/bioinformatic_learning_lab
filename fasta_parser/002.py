"""
FASTA project Parser
Date: 03.05.2026

Reads a multi-Fasta file and returns a dictionary
{header: sequence}
"""

def parse_fasta(file_path):

    try: 
        
        sequences = {}  # Dictionary to store results
        header = None   # Current sequence header
        seq_list = []   # Temporary list to collect sequence lines

        with open(file_path, "r") as f:  # Open FASTA file for reading (r)

            for line in f:  # Read file by line (memory efficient)
                line = line.strip() # remove \n and spaces

                if not line:    # Skip empty lines
                    continue

                if line.startswith(">"):    # If line starts with ">" -> it's a header
                    if header:  # Save previous sequence before moving to next header
                        sequences[header] = "".join(seq_list)

                    header = line[1:]   # Update header (remove ">" symbol)
                    seq_list = []   # Reset sequence collector for new gene

                else:
                    seq_list.append(line)   # Add sequence line to list
            
            if header:  
                sequences[header] = "".join(seq_list)   # Save last sequence after loop ends

        return sequences    # Return final dictionary
    
    except FileNotFoundError:   
        print("File not found!")
        return None
    
data = parse_fasta("multiple_seq.fasta")

for header, seq in data.items():
    print("=" * 50)
    print("HEADER:", header)
    print("LENGTH:", len(seq))
    print("SEQUENCE:", seq)