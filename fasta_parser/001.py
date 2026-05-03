# Open FASTA File
def read_fasta(file_path):

    try:
        with open(file_path) as f: 
            lines = f.readlines()   # Read all lines
        
        if not lines:            # İf file is empty printing None 
            return None, None
        
        header = lines[0].strip()[1:] # First line is header line
        sequence = "".join(line.strip() for line in lines[1:]) # Other lines include sequence data 

        return header, sequence
    
    except FileNotFoundError:   # İf file does not exist print none
        print("File Not Found!")
        return None, None

print(read_fasta("single_seq.fasta"))