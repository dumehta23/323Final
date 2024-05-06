import re

with open('final24.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

def remove_keywords(lines):
    keywords = ["program", "var", "begin", "end.", "integer"]
    filtered_lines = []
    for line in lines:
        if not any(keyword in line for keyword in keywords):
            filtered_lines.append(line)
    return filtered_lines

def remove_semicolons(lines):
    for i, line in enumerate(lines):
        if ';' in line:
            lines[i] = line.replace(';', '')
    return lines

def fix_parentheses(line):
    return line.replace('( ', '(').replace(' )', ')')


def write_to_print(line):
    return line.replace('write', 'print')

def fix_quotes(line):
    return line.replace('“', '"').replace('”', '"')

# Call the function to filter out unwanted lines
extracted_lines = remove_keywords(lines)
extracted_lines = remove_semicolons(extracted_lines)
extracted_lines = [fix_parentheses(line) for line in extracted_lines]
extracted_lines = [write_to_print(line) for line in extracted_lines]
extracted_lines = [fix_quotes(line) for line in extracted_lines]

# Write the filtered lines to the output file
with open('output.py', 'w', encoding='utf-8') as output_file:
    for line in extracted_lines:
        output_file.write(line)
