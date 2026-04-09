# Input and output file names 
input_fa = '/Users/wuhanddmm/Desktop/shell_data/IBI1_2025-26/Practical7_desktop/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
# It doesn’t matter if you use the absolute or relative path - we can update this for our own computers so long as your code is accessing the same file supplied on Learn.
output_fa = "stop_genes.fa"

# Start and stop codons
start_codon = "ATG"
stop_codons = ["TAA", "TAG", "TGA"]

def check_in_frame_stop(seq):
    """Return True and list of stop codons if in-frame stop exists after ATG"""
    found_stops = []

    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            for j in range(i + 3, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    found_stops.append(codon)

    unique_stops = sorted(list(set(found_stops)))
    return len(unique_stops) > 0, unique_stops


total_genes = 0  

with open(input_fa, "r") as f_in, open(output_fa, "w") as f_out:
    gene_header = ""
    gene_seq = ""

    for line in f_in:
        line_clean = line.rstrip()

        if line_clean.startswith(">"):
            if gene_seq:
                has_stop, stops = check_in_frame_stop(gene_seq)

                if has_stop:
                    total_genes += 1   # count

                    gene_name = gene_header.split()[0][1:]
                    stop_str = stops[0]

                    f_out.write(f">{gene_name};{stop_str}\n")

                    for i in range(0, len(gene_seq), 60):
                        f_out.write(gene_seq[i:i+60] + "\n")

            gene_header = line_clean
            gene_seq = ""

        else:
            gene_seq += line_clean

    # Process last gene
    if gene_seq:
        has_stop, stops = check_in_frame_stop(gene_seq)

        if has_stop:
            total_genes += 1   # count

            gene_name = gene_header.split()[0][1:]
            stop_str = stops[0]

            f_out.write(f">{gene_name};{stop_str}\n")

            for i in range(0, len(gene_seq), 60):
                f_out.write(gene_seq[i:i+60] + "\n")


print("Task is finished! Output file: stop_genes.fa")
print(f"Total genes with in-frame stop codons: {total_genes}")
