def remove_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    clean_content = ''
    i = 0
    while i < len(content):
        start_comment = content.find('//', i)
        if start_comment == -1:
            clean_content += content[i:]
            break

        clean_content += content[i:start_comment]
        end_comment = content.find('//', start_comment + 2)
        if end_comment == -1:
            break

        newline_index = content.find('\n', start_comment + 2)
        if newline_index == -1 or newline_index > end_comment:
            i = end_comment + 2
        else:
            i = content.find('\n', end_comment + 2)
            if i == -1:
                break
            i += 1

    return clean_content.strip()


def remove_blank_lines(text):
    lines = text.split('\n')
    non_blank_lines = [line for line in lines if line.strip() != '']
    return '\n'.join(non_blank_lines)

def normalize_spaces(text):
    lines = text.split('\n')
    normalized_lines = []
    for line in lines:
        for operator in ['=', '+', '-', '*', '/', '(', ')', ';']:
            line = line.replace(operator, f' {operator} ')
        normalized_lines.append(' '.join(line.split()))
    return '\n'.join(normalized_lines)


input_file_path = 'finalv1.txt'
output_file_path = 'final24.txt'

clean_content = remove_comments(input_file_path)
cleaner_content = remove_blank_lines(clean_content)
normalized_content = normalize_spaces(cleaner_content)

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(normalized_content)