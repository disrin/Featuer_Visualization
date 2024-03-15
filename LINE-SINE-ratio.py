###Making LINE/SINE ratio - Make a plot with LINE/SINE ratio and align it with inter-homolog contacts on specified chromosome. This allows you to visualize contact 
enrichment at LINE and SINE locations.

import matplotlib.pyplot as plt
import pandas as pd


###make output file with LINE/SINE ratio
def merge_files(file1_path, file2_path, output_path):
    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2, open(output_path, 'w') as output:
        for line1, line2 in zip(f1, f2):
            # Use tab-separated files. If they are separated by another character, change to '\t'.
            parts1 = line1.strip().split('\t')
            parts2 = line2.strip().split('\t')

    
            col3_file1 = float(parts1[2])  #converting col3 to floats if you haven't done so already
            col3_file2 = float(parts2[2])

            # Avoid division by zero
            if col3_file2 != 0:
                ratio = col3_file1 / col3_file2
            else:
                ratio = 0

            # Write to output file
            output.write(f"{parts1[0]}\t{parts1[1]}\t{ratio}\n")

# change paths
LINE_path = "/path/to/LINE.bedgraph"
SINE_path = "/path/to/SINE.bedgraph"
ratio_path = "/path/to/LINE-SINEratio.txt"

merge_files(LINE_path, SINE_path, output_path)



#Make plot comparing feature and interhomolog-contact frequency

# File paths
ratio_path = "/path/to/LINE-SINEratio.txt"
contact_path = "/path/to/chr/interhomolog/frequency.txt"

# Read data from the first file
df1 = pd.read_csv(ratio_path, header=None, names=['col1', 'bin', 'ratio'])

# Read data from the second file
df2 = pd.read_csv(contact_path, header=None, names=['col1', 'bin', 'frequency'])

# Merge the two dataframes on the 'bin' column
merged_df = pd.merge(df1, df2, on='bin')

# Create a scatter plot for the first plot
plt.scatter(merged_df['bin'], merged_df['ratio'], label='Ratio', alpha=0.7, color='blue', marker='o')

# Create a bar plot for the second plot
plt.bar(merged_df['bin'], merged_df['frequency'], label='Frequency', alpha=0.7, color='orange')

# Add labels and title
plt.xlabel('Bin Numbers')
plt.ylabel('Values')
plt.title('Comparison of Ratio and Frequency for each Bin')
plt.legend()

# Show the plot
plt.show()

