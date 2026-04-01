# largest_orf.py
# Find the longest Open Reading Frame (ORF) in a given RNA sequence

# Define the RNA sequence as a string
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# Initialize variables to store the longest ORF found
longest_orf_length = 0
longest_orf_seq = ""

# Loop over every possible start position (0 to len(seq)-3)
for i in range(len(seq) - 2):
    # Check if the triplet at position i is the start codon AUG
    if seq[i:i+3] == "AUG":
        start = i
        # Scan forward in steps of 3 (reading frame)
        for j in range(start + 3, len(seq) - 2, 3):
            codon = seq[j:j+3]
            # If a stop codon is found, this ORF ends
            if codon in ["UAA", "UAG", "UGA"]:
                orf_len = j + 3 - start
                # Update longest ORF if this one is longer
                if orf_len > longest_orf_length:
                    longest_orf_length = orf_len
                    longest_orf_seq = seq[start:j+3]
                break  # Stop scanning after the first in-frame stop codon

# Output the result
print("Longest ORF sequence:", longest_orf_seq)
print("The length of the largest ORF in nucleotides is", longest_orf_length)
