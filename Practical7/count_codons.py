# Practical7 Task3
import matplotlib.pyplot as plt

# Define input FASTA file
input_fa = "stop_genes.fa"
valid_stops = ["TAA", "TAG", "TGA"]
start_codon = "ATG"

# Step 1. Ask user to input a stop codon (only accept TAA/TAG/TGA)
print("Please choose a stop codon: TAA, TAG, TGA")
user_stop = input("Enter your choice: ").strip().upper()

# validate input
while user_stop not in ['TAA', 'TAG', 'TGA']:
    print("Invalid input. Please enter TAA, TAG, or TGA")
    user_stop = input("Enter your choice: ").strip().upper()

# Step 2.  Get upstream codons from the longest ORF for a given stop codon
def get_longest_upstream_codons(seq, target_stop):
    all_upstream = []
    max_codon_count = 0
    best_codons = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            current_codons = []
            found = False
            for j in range(i + 3, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon == target_stop:
                    all_upstream.append(current_codons)
                    found = True
                    break
                current_codons.append(codon)
            if found:
                if len(current_codons) > max_codon_count:
                    max_codon_count = len(current_codons)
                    best_codons = current_codons.copy()
    return best_codons

# Step 3. Read the file and collect proper codons
total_codons = []
with open(input_fa, "r") as f:
    gene_seq = ""
    for line in f:
        line_clean = line.rstrip()
        if line_clean.startswith(">"):
            if gene_seq:
                codons = get_longest_upstream_codons(gene_seq, user_stop)
                total_codons.extend(codons)
            gene_seq = ""
        else:
            gene_seq += line_clean
    if gene_seq:
        codons = get_longest_upstream_codons(gene_seq, user_stop)
        total_codons.extend(codons)

# Step 4. Count codon frequency
codon_count = {}
for codon in total_codons:
    if codon in codon_count:
        codon_count[codon] += 1
    else:
        codon_count[codon] = 1

# Step 5. Print frequency results
print(f"\n=== Codon Frequency Upstream of {user_stop} ===")
total = sum(codon_count.values())
# show the total number
print(f"Total in-frame codons counted: **{total}**")
for codon, cnt in codon_count.items():
    pct = (cnt / total) * 100
    print(f"{codon}: {cnt} ({pct:.1f}%)")

# 6. Generate and save pie chart
if codon_count:
    labels = list(codon_count.keys())
    sizes = list(codon_count.values())

    plt.figure(figsize=(12, 12))
    wedges, texts, autotexts = plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=0.85,
        labeldistance=1.05,
        textprops={'fontsize': 9},
        rotatelabels=False
    )

    plt.title(f"Codon Frequency Upstream of Stop Codon {user_stop}", fontsize=16, pad=20)
    plt.tight_layout()

    # save
    pie_file = f"codon_frequency_{user_stop}.png"
    plt.savefig(pie_file, dpi=300, bbox_inches='tight')
    plt.close()
    # count as total codons and print
    print(f"\n--Total codons used for pie chart: {total}--")
    print(f"Pie chart saved as: {pie_file}")
else:
    print(f"\nNo {user_stop} found in sequences, no pie chart generated.")
    # output as Total=0
    print(f"**Total codons counted: 0**")