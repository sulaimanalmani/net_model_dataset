# Extract all zip files in the current directory
for file in *.zip; do
    unzip "$file"
done
