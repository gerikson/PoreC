import h5py

def check_haplotype(file_path):
    with h5py.File(file_path, 'r') as f:
        # Print the file structure
        def print_structure(name, obj):
            print(name)
            if isinstance(obj, h5py.Group):
                for key, value in obj.attrs.items():
                    print(f"  Attribute: {key} = {value}")
            elif isinstance(obj, h5py.Dataset):
                for key, value in obj.attrs.items():
                    print(f"  Attribute: {key} = {value}")

        f.visititems(print_structure)

        # Check for haplotype-related attributes or datasets
        haplotype_tags = ["haplotype", "HP", "H1"]
        haplotyped = False

        def check_haplotype_info(name, obj):
            nonlocal haplotyped
            if isinstance(obj, h5py.Group) or isinstance(obj, h5py.Dataset):
                for key in obj.attrs.keys():
                    if any(tag in key for tag in haplotype_tags):
                        haplotyped = True
                        break

        f.visititems(check_haplotype_info)

        if haplotyped:
            print("The HiC mcool file is haplotyped.")
        else:
            print("The HiC mcool file is not haplotyped.")

# Example usage
file_path = "/data/processing3/erikson_pipegrp/24L004897_PnM3_snakePipe/Pore-C-Snakemake/results/matrix/NlaIII_PnM3_dm6_JJg14.matrix.mcool"
check_haplotype(file_path)