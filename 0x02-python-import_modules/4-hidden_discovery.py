#!/usr/bin/python3
import dis

def extract_names():
    code = open('hidden_4.pyc', 'rb').read()
    names = set()

    # Disassemble the code and extract names
    instructions = dis.get_instructions(code)
    for instruction in instructions:
        if instruction.opname == 'LOAD_NAME' and not instruction.argrepr.startswith('<'):
            names.add(instruction.argrepr)

    return sorted(name for name in names if not name.startswith('__'))

if __name__ == "__main__":
    names = extract_names()
    for name in names:
        print(name)
