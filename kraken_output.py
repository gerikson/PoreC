from collections import Counter
# Read the Kraken2 output file
with open('/data/processing4/erikson_pipegrp/deepseq/kraken-results/mock10.kraken.out', 'r') as file:
    lines = file.readlines()


# Extract unique taxonomic IDs from classified lines
taxonomic_ids = set()
taxonomic_id_counts = Counter()
for line in lines:
    if line.startswith('C'):
        parts = line.split('\t')
        taxonomic_id = parts[2]
        taxonomic_id_counts[taxonomic_id] += 1

# Print the unique taxonomic IDs, each on a new line
#for taxonomic_id in taxonomic_ids:
    #print(taxonomic_id)

# Get the top 5 most frequent taxonomic IDs
top_5_taxonomic_ids = taxonomic_id_counts.most_common(5)


# Print the top 5 taxonomic IDs with their counts
for taxonomic_id, count in top_5_taxonomic_ids:
    print(f"{taxonomic_id}: {count}")