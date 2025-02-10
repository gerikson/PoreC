import pysam

# Open the input VCF file
input_vcf = pysam.VariantFile("/data/processing4/erikson_pipegrp/Jumana/JJg14_hybrid_forSP.vcf", "r")

# Create a new header for the output VCF file
new_header = input_vcf.header.copy()
#new_header.samples.clear()
#new_header.samples.remove("JJg14_057")
#new_header.samples.remove("JJg14_439")
new_header.samples.add("JJg14")

# Create an output VCF file
output_vcf = pysam.VariantFile("/data/processing4/erikson_pipegrp/Jumana/JJg14_hybrid_forSP.merged.vcf", "w", header=input_vcf.header)

# Iterate over each record in the input VCF
for record in input_vcf:
    # Assuming maternal and paternal genotypes are stored in separate samples
    maternal_gt = record.samples["JJg14_057"]['GT']
    paternal_gt = record.samples["JJg14_439"]['GT']
    
    # Merge the genotypes (this is a simple example, adjust as needed)
    merged_gt = tuple(set(maternal_gt + paternal_gt))
    
    # Update the genotype in the record
    #record.samples["JJg14_057"] = {'GT': merged_gt}
    # Remove the original genotypes
    #del record.samples["JJg14_057"]
    #del record.samples["JJg14_439"]
    
    record.samples["JJg14_057"]["GT"] = merged_gt
    
    # Write the updated record to the output VCF
    output_vcf.write(record)

# Close the files
input_vcf.close()
output_vcf.close()