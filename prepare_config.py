import sys

def generate_config(interactions_path, prdm9_path, ctcf_path, genomic_region, output_config="tracks.ini"):
    with open(output_config, 'w') as config_file:
        config_file.write(f"""
[x-axis]
where = top

[interactions]
file = {interactions_path}
title = Interactions in {genomic_region}
type = links
color = red
line_width = 2
show_half = true

[PRDM9 ChIP-seq]
file = {prdm9_path}
title = PRDM9 ChIP-seq in {genomic_region}
color = blue
type = line
min_value = 0
max_value = auto

[CTCF ChIP-seq]
file = {ctcf_path}
title = CTCF ChIP-seq in {genomic_region}
color = green
type = line
min_value = 0
max_value = auto
""".strip())

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python prepare_config.py <interactions.bedpe> <prdm9.bedgraph> <ctcf.bedgraph> <genomic_region> <output_config.ini>")
        sys.exit(1)
    generate_config(*sys.argv[1:])

