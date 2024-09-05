import matplotlib.pyplot as plt

# Sample data: 30 tree heights in inches
tree_heights = [
    35, 42, 50, 48, 55, 60, 45, 51, 53, 47,
    58, 49, 41, 67, 52, 57, 62, 46, 54, 59,
    64, 66, 40, 61, 63, 70, 72, 43, 69, 65
]

# Define the bin size
bin_size = 5

# Calculate the range of the bins
min_height = min(tree_heights)
max_height = max(tree_heights)
bins = range(min_height, max_height + bin_size, bin_size)

# Plot the histogram
plt.hist(tree_heights, bins=bins, edgecolor='black')

# Add titles and labels
plt.title('Histogram of Tree Heights')
plt.xlabel('Height (inches)')
plt.ylabel('Number of Trees')

# Show the plot
plt.show()
