# Import required library for plotting
import matplotlib.pyplot as plt

# Step 1: Create a dictionary with initial gene expression values
gene_expression = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}

# Print the initial dictionary
print("Initial gene expression dictionary:")
print(gene_expression)
print()

# Step 2: Add MYC gene with expression value 11.6
gene_expression["MYC"] = 11.6

# Print updated dictionary to confirm MYC was added
print("Updated dictionary after adding MYC:")
print(gene_expression)
print()

# Step 3: Create a bar chart for all genes
genes = list(gene_expression.keys())
values = list(gene_expression.values())

plt.figure()
plt.bar(genes, values)

# Add labels and title
plt.xlabel("Genes")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels")

# Only when I close the chart can the subsequent processes start; 
# If the chart is not closed, the terminal will fail to display the step 4&5 output.
print ('Please close the chart and let it continues running.')
# Show the plot
plt.show()

# Step 4: Select a gene of interest
# Set the gene you want to check here (Attention! Alter if I like):
selected_gene = "TP53"   # <-- Change this value to test other genes

# Check if the gene exists and print its expression value
if selected_gene in gene_expression:
    print(f"\nExpression level of {selected_gene}: {gene_expression[selected_gene]}")
else:
    print(f"\nError: {selected_gene} is not found in the dataset.")
print()

# Step 5: Calculate and print the average gene expression
total_expression = sum(gene_expression.values())
num_genes = len(gene_expression)
average_expression = total_expression / num_genes

print(f"Average gene expression level: {average_expression:.2f}")