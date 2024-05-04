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
        # Insert spaces around operators and parentheses
        for operator in ['=', '+', '-', '*', '/', '(', ')', ';']:
            line = line.replace(operator, f' {operator} ')

        # Clean up extra spaces and standardize spacing
        line = ' '.join(line.split())

        # Specific replacement for "value = " inside the write function
        line = line.replace('“value = ”,', '“value=” ,')

        # Remove space between function name and opening parenthesis
        line = line.replace('write (', 'write(')

        normalized_lines.append(line)

    return '\n'.join(normalized_lines)


input_file_path = 'finalv1.txt'
output_file_path = 'final24.txt'

clean_content = remove_comments(input_file_path)
cleaner_content = remove_blank_lines(clean_content)
normalized_content = normalize_spaces(cleaner_content)

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(normalized_content)

############# PART 2 ###################
parsing_table = {
    'P': {'program': 'program I ; var DL begin SL end.'},
    'I': {'p': 'Le PI', 'q': 'Le PI', 'r': 'Le PI', 's': 'Le PI'},
    'PI': {'0': 'Di PI', '1': 'Di PI', '2': 'Di PI', '3': 'Di PI', '4': 'Di PI',
           '5': 'Di PI', '6': 'Di PI', '7': 'Di PI', '8': 'Di PI', '9': 'Di PI',
           'p': 'Di PI', 'q': 'Di PI', 'r': 'Di PI', 's': 'Di PI', ')': 'λ', '*': 'λ',
           '/': 'λ', '+': 'λ', '-': 'λ', '=': 'λ', ';': 'λ', ':': 'λ', ',': 'λ'},
    'DL': {'p': 'D : T ;', 'q': 'D : T ;', 'r': 'D : T ;', 's': 'D : T ;'},
    'D': {'p': 'I , D', 'q': 'I , D', 'r': 'I , D', 's': 'I , D'},
    'T': {'integer': 'integer'},
    'SL': {'p': 'S SL', 'q': 'S SL', 'r': 'S SL', 's': 'S SL', 'write': 'S SL'},
    'S': {'p': 'A', 'q': 'A', 'r': 'A', 's': 'A', 'write': 'W'},
    'W': {'write': 'write ( St I ) ;'},
    'St': {'p': 'λ', 'q': 'λ', 'r': 'λ', 's': 'λ', '"value="': '"value=" ,'},
    'A': {'p': 'I = E ;', 'q': 'I = E ;', 'r': 'I = E ;', 's': 'I = E ;'},
    'E': {'0': 'Te PE', '1': 'Te PE', '2': 'Te PE', '3': 'Te PE', '4': 'Te PE',
          '5': 'Te PE', '6': 'Te PE', '7': 'Te PE', '8': 'Te PE', '9': 'Te PE',
          'p': 'Te PE', 'q': 'Te PE', 'r': 'Te PE', 's': 'Te PE', '(': 'Te PE', '+': 'Te PE', '-': 'Te PE'},
    'PE': {')': 'λ', '+': '+ Te PE', '-': '- Te PE'},
    'Te': {'0': 'F PT', '1': 'F PT', '2': 'F PT', '3': 'F PT', '4': 'F PT', '5': 'F PT',
           '6': 'F PT', '7': 'F PT', '8': 'F PT', '9': 'F PT', 'p': 'F PT', 'q': 'F PT',
           'r': 'F PT', 's': 'F PT', '(': 'F PT', '+': 'F PT', '-': 'F PT'},
    'PT': {')': 'λ', '*': '* F PT', '/': '/ F PT', '+': 'λ', '-': 'λ', ';': 'λ'},
    'F': {'0': 'N', '1': 'N', '2': 'N', '3': 'N', '4': 'N', '5': 'N', '6': 'N', '7': 'N', '8': 'N', '9': 'N',
          'p': 'I', 'q': 'I', 'r': 'I', 's': 'I', '(': '( E )', '+': 'N', '-': 'N'},
    'N': {'+': 'Sn Di PN', '-': 'Sn Di PN'},
    'PN': {'0': 'Di PN', '1': 'Di PN', '2': 'Di PN', '3': 'Di PN', '4': 'Di PN', '5': 'Di PN',
           '6': 'Di PN', '7': 'Di PN', '8': 'Di PN', '9': 'Di PN',
           ')': 'λ', '*': 'λ', '/': 'λ', '+': 'λ', '-': 'λ', ';': 'λ'},
    'Sn': {'0': 'λ', '1': 'λ', '2': 'λ', '3': 'λ', '4': 'λ', '5': 'λ', '6': 'λ', '7': 'λ',
           '8': 'λ', '9': 'λ', ')': 'λ', '*': 'λ', '/': 'λ', '+': 'λ', '-': 'λ', ';': 'λ'},
    'Di': {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'},
    'Le': {'p': 'p', 'q': 'q', 'r': 'r', 's': 's'},
}
