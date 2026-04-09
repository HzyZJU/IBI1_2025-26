# Practical8 Task1
def calculate_protein_mass(sequence):
    """Calculate the mass of a protein sequence.

    Args:
        sequence (str): A string representing the amino acid sequence of the protein.

    Returns:
        float: The calculated mass of the protein.
    """
    # Define the mass of each amino acid
    aa_mass = {
        'G': 57.02,  # Glycine
        'A': 71.04,  # Alanine
        'S': 87.03,  # Serine
        'P': 97.05,  # Proline
        'V': 99.07,  # Valine
        'T': 101.05, # Threonine
        'C': 103.01, # Cysteine
        'I': 113.08, # Isoleucine
        'L': 113.08, # Leucine
        'N': 114.04, # Asparagine
        'D': 115.03, # Aspartic Acid
        'Q': 128.06, # Glutamine
        'K': 128.09, # Lysine
        'E': 129.04, # Glutamic Acid
        'M': 131.04, # Methionine
        'H': 137.06, # Histidine
        'F': 147.07, # Phenylalanine
        'R': 156.10, # Arginine
        'Y': 163.06, # Tyrosine
        'W': 186.08  # Tryptophan
    }

    total_mass = 0.0

    for aa in sequence:
        if aa in aa_mass:
            total_mass += aa_mass[aa]
        else:
            raise ValueError(f"Invalid amino acid '{aa}' in sequence.")

    return total_mass

# example shown
if __name__ == "__main__":
    example_seq = "GASPV"
    mass = calculate_protein_mass(example_seq)
    print(f"Mass of {example_seq}: {mass:.2f} amu")