import csv

def convert_csv_to_utf8(input_file, output_file):
    # Read the original CSV file
    with open(input_file, 'r', encoding='utf-8-sig') as infile:  # 'utf-8-sig' handles UTF-8 with BOM
        reader = csv.reader(infile)
        rows = list(reader)

    # Write to a new CSV file with UTF-8 encoding
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

    print(f"File '{input_file}' has been converted to UTF-8 and saved as '{output_file}'")

if __name__ == "__main__":
    input_file = 'scraped_data.csv'  # Replace with your input file name
    output_file = 'scraped_data_utf8_final.csv'  # Replace with your desired output file name
    convert_csv_to_utf8(input_file, output_file)
