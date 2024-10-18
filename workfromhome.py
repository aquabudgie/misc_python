import os

def extract_work_from_home_status(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i].strip() == "# Work from home?":
                if i + 1 < len(lines):
                    return lines[i + 1].strip()
    return "NA"

# Directory containing the markdown files
directory = "/Users/2279508/Documents/Obsidian Vault/Daily Notes"

# Output file
output_file = "work_from_home_status.txt"

# List to store the results
results = []

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        file_path = os.path.join(directory, filename)
        date = filename.split('.')[0]
        status = extract_work_from_home_status(file_path)
        results.append(f"{date} {status}")

# Write the results to the output file
with open(output_file, 'w') as file:
    for result in results:
        file.write(result + "\n")

print(f"Work from home status has been written to {output_file}.")