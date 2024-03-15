#!/bin/bash

# Check number of arguments
if [ $# -ne 5 ]; then
    echo "Usage: $0 <interactions.bedpe> <prdm9.bedgraph> <ctcf.bedgraph> <genome_region> <output.png>"
    exit 1
fi

# input and output path variables
INTERACTIONS_FILE=$1
PRDM9_FILE=$2
CTCF_FILE=$3
GENOME_REGION=$4
OUTPUT_FILE=$5

# Generate tracks.ini configuration file
python prepare_config.py "$INTERACTIONS_FILE" "$PRDM9_FILE" "$CTCF_FILE" tracks.ini

# Run PyGenomeTracks
pyGenomeTracks --tracks tracks.ini --region $GENOME_REGION -o $OUTPUT_FILE

echo "Visualization generated: $OUTPUT_FILE"

