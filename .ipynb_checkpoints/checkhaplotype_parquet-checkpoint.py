import pandas as pd

def check_phased(file_path):
    # Read the parquet file
    df = pd.read_parquet(file_path)
    
    # Print the columns
    print("Columns:", df.columns)
    
    # Check for phasing-related columns
    phasing_tags = ["phase", "haplotype", "HP", "H1", "H2", "h1", "h2"]
    phased = any(tag in df.columns for tag in phasing_tags)
    
    if phased:
        print("The HiC parquet file is phased.")
    else:
        print("The HiC parquet file is not phased.")

def count_haplotype_reads(file_path, haplotype_column, haplotype_value):
    # Read the parquet file
    df = pd.read_parquet(file_path)
    
    # Filter the dataframe for the specific haplotype
    haplotype_reads = df[df[haplotype_column] == haplotype_value]
    print(haplotype_reads)
    # Count the number of reads
    num_reads = len(haplotype_reads)
    
    print(f"Number of reads with {haplotype_column} = {haplotype_value}: {num_reads}")

# Example usage
#file_path = "/data/processing2/erikson_pipegrp/24L004896_PnM2_snakePipe/Pore-C-Snakemake/results/merged_contacts/NlaIII_PnM2_dm6_JJg14.concatemers.parquet"
file_path = "/data/processing4/erikson_pipegrp/Jumana/Pore-C-Snakemake/results/merged_contacts/NlaIII_PnM1_dm6_JJg14.concatemers.parquet"

check_phased(file_path)
count_haplotype_reads(file_path, "haplotype_phased_h_trans", True) 
count_haplotype_reads(file_path, "haplotype_phased_h_cis", True) 
count_haplotype_reads(file_path, "haplotype_unphased", True) 
count_haplotype_reads(file_path, "haplotype_phased_sets_differ", True) 
count_haplotype_reads(file_path, "haplotype_semi_phased", True) 
count_haplotype_reads(file_path, "total_contacts", True) 