import re

def clean_text(rgx_list, text):
    new_text = text
    for rgx_match in rgx_list:
        new_text = re.sub(rgx_match, '', new_text)
    return new_text

def remove_comments(program_content):
    text_reg = ['\/\/.*', '\/\*(\*(?!\/)|[^*])*\*\/']
    return clean_text(text_reg, program_content)

def count_instructions(program_content):
    instructions = {'if': 0, 'while': 0, 'for': 0, 'else': 0, 'case': 0, 'else if': 0}
    for key, val in instructions.items():
        instructions[key] = program_content.count(key)
    if instructions['else if'] != 0:
        instructions['if'] -= instructions['else if']
        instructions['else'] -= instructions['else if']
    return instructions

def count_mccabe(instructions):
    mccabe = 0
    for key, val in instructions.items():
        mccabe += val
    return mccabe

def main(file_name):
    print(f'======================{file_name}===================')
    with open(file_name) as f:
        program_content = f.read()
    program_content = remove_comments(program_content)
    # print(program_content)
    instructions = count_instructions(program_content)
    print(instructions)
    mccabe = count_mccabe(instructions)
    print(f"Miara McCabe'a: {mccabe}")
    
if __name__ == "__main__":
    main('programy\\Program1.c')
    main('programy\\Program2.c')
    main('programy\\Program3.c')