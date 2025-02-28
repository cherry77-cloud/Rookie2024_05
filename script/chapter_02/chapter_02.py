import os
from textwrap import dedent

base_path = "/home/acs/homework/lesson_2/"

  
def homework_0_task():
    with open(os.path.join(base_path, "homework_0", "names.txt"), "w") as file:
        file.writelines(["AcWing\n", "yxc\n", "Bob\n", "张强\n", "李明\n", "Alice\n"])


def homework_1_task():
    filepath = os.path.join(base_path, "homework_1", "problem.txt")
    with open(filepath, "r") as file:
        lines = file.readlines()

    lines[-1] = lines[-1][:100] + lines[-1][101:]
    lines[2] = lines[2][:7] + lines[2][8:]
    lines[0] = lines[0][:29] + lines[0][30:]
    lines[15] = lines[15][:54] + lines[15][55:]
    lines[8] = lines[8][:79] + lines[8][80:]

    with open(filepath, "w") as file:
        file.writelines(lines)


def homework_2_task():
    filepath = os.path.join(base_path, "homework_2", "problem.txt")
    with open(filepath, 'r') as file:
        lines = file.readlines()

    two_count = 0
    new_lines = []
    for line in lines:
        if 'two' in line:
            two_count += line.count('two')
            if two_count == 1:
                line = line.replace('two', 'twoabc', 1)
            elif two_count == 2:
                line = line.replace('two', 'deftwo', 1)
            elif two_count == 3:
                start_index = line.find('two') + 3
                line = line[:start_index] + line[start_index + 12:]
            elif two_count == 4:
                continue  # Skip this line
        new_lines.append(line)

    with open(filepath, 'w') as file:
        file.writelines(new_lines)


def homework_3_task():
    filepath = os.path.join(base_path, "homework_3", "problem.txt")
    with open(filepath, "r") as file:
        lines = file.readlines()

    for i in range(4, 15):
        lines[i] = lines[i].replace('of', 'OF')

    lines = [line.replace('the', 'THE') for line in lines]

    is_counter = 0
    for i, line in enumerate(lines):
        new_line = ""
        for word in line.split():
            if word == 'is':
                is_counter += 1
                if is_counter % 2 == 0:
                    word = 'IS'
            new_line += word + " "
        lines[i] = new_line.rstrip() + "\n"

    with open(filepath, "w") as file:
        file.writelines(lines)


def homework_4_task():
    filepath = os.path.join(base_path, "homework_4", "problem.txt")
    with open(filepath, "r") as file:
        lines = file.readlines()

    deleted_line = lines.pop(10)
    lines.append(deleted_line)
    copied_line = lines[4]
    lines.append(copied_line)

    with open(filepath, "w") as file:
        file.writelines(lines)


def homework_5_task():
    filepath = os.path.join(base_path, "homework_5", "problem.txt")
    with open(filepath, 'r') as file:
        lines = file.readlines()

    if len(lines) < 13 or len(lines[10]) < 15 or len(lines[4]) < 88 or len(lines[6]) < 6:
        raise ValueError("File does not have enough lines or specified characters.")

    deleted_content = lines[10][14:] + lines[11] + lines[12][:5]
    copied_content = lines[4][87:] + lines[5] + lines[6][:6]

    lines[10] = lines[10][:14]
    lines[12] = lines[12][5:]

    del lines[11]

    if lines[-1].endswith('\n'):
        lines[-1] = lines[-1].rstrip('\n') + deleted_content + copied_content + '\n'
    else:
        lines[-1] = lines[-1] + deleted_content + copied_content

    with open(filepath, 'w') as file:
        file.writelines(lines)


def homework_6_task():
    source0_path = os.path.join(base_path, "homework_6", "source0.cpp")
    source1_path = os.path.join(base_path, "homework_6", "source1.cpp")

    open(source0_path, 'w').close()

    with open(source1_path, 'r') as file:
        lines = file.readlines()

    content_to_copy = ''.join(lines[:3]) + ''.join(lines[11:24])

    with open(source0_path, 'w') as file:
        file.write(content_to_copy)


def homework_7_task():
    filepath = os.path.join(base_path, "homework_7", "source.cpp")
    leading_spaces = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 8, 8, 8, 12, 4, 4, 4, 0]
    with open(filepath, 'r') as file:
        lines = file.readlines()

    if len(leading_spaces) != len(lines):
        raise ValueError("The number of lines in the file does not match the number of leading spaces provided.")

    formatted_lines = []
    for space, line in zip(leading_spaces, lines):
        if line.strip():  # Check if the line is not an empty line
            formatted_line = ' ' * space + line.lstrip()
        else:  # If it's an empty line, keep it as is
            formatted_line = line
        formatted_lines.append(formatted_line)

    with open(filepath, 'w') as file:
        file.writelines(formatted_lines)


def homework_8_task():
    filepath = os.path.join(base_path, "homework_8", "source.cpp")

    with open(filepath, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if 15 <= i + 1 <= 21:
            lines[i] = '    ' * 2 + lines[i]
        elif 22 <= i + 1 <= 23:
            lines[i] = lines[i][4:] if lines[i].startswith('    ') else lines[i]

    with open(filepath, 'w') as file:
        file.writelines(lines)


def homework_9_task():
    cpp_code = dedent("""
            #include <iostream>

            using namespace std;

            int main()
            {
                int a, b;
                cin >> a >> b;
                cout << a + b << endl;
                return 0;
            }
    """)
    filepath = os.path.join(base_path, "homework_9", "source.cpp")
    with open(filepath, 'w') as file:
        file.write(cpp_code)


if __name__ == "__main__":
    homework_0_task()
    homework_1_task()
    homework_2_task()
    homework_3_task()
    homework_4_task()
    homework_5_task()
    homework_6_task()
    homework_7_task()
    homework_8_task()
    homework_9_task()
