# The path to your text file
file_path = "About/journal.txt"

# Step 1: Read the file
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Step 2: Split the string into sections
sections = content.split("\n\n")

# Step 3: Reverse the list
reversed_sections = sections[::-1]

# Step 4: Join the reversed list back into a string
reversed_content = "\n\n".join(reversed_sections)

# Print the reversed content
# Path for the output file (can be the same as the original to overwrite it)
output_file_path = "reversed_file.txt"

# Write the reversed content back to a new file
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(reversed_content)
