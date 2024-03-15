# Genome and Feature Track Visualization

This repository contains scripts for generating visualizations of genomic data -
1.Interaction frequency with direct comparison to LINE or SINE enrichment - this can be extended to any other genomic feature such as UCEs, and other recurring DNA motifs. 
2.Generating ChIP-seq data (bedgraph files) tracks along with genomic data tracks 


## Prerequisites

- Python 3
- PyGenomeTracks

You can install PyGenomeTracks using pip:

```bash
pip install pygenometracks
```

## USAGE

```bash
./generate_tracks.sh path/to/interactions.bedpe path/to/prdm9.bedgraph path/to/ctcf.bedgraph chr1:1000000-2000000 output.png
```

### References

1. Luo, Z., Wang, X., Jiang, H., Wang, R., Chen, J., Chen, Y., Xu, Q., Cao, J., Gong, X., Wu, J., Yang, Y., Li, W., Han, C., Cheng, C. Y., Rosenfeld, M. G., Sun, F., & 
Song, X. (2020). Reorganized 3D Genome Structures Support Transcriptional Regulation in Mouse Spermatogenesis. iScience, 23(4), 101034. 
https://doi.org/10.1016/j.isci.2020.101034
2. Smagulova, F., Brick, K., Pu, Y., Camerini-Otero, R. D., & Petukhova, G. V. (2016). The evolutionary turnover of recombination hot spots contributes to speciation in 
mice. Genes & development, 30(3), 266–280. https://doi.org/10.1101/gad.270009.115
3. Baker, C. L., Kajita, S., Walker, M., Saxl, R. L., Raghupathy, N., Choi, K., Petkov, P. M., & Paigen, K. (2015). PRDM9 drives evolutionary erosion of hotspots in Mus 
musculus through haplotype-specific initiation of meiotic recombination. PLoS genetics, 11(1), e1004916. https://doi.org/10.1371/journal.pgen.1004916
