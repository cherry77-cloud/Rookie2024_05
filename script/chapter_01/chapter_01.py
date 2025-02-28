import os
import shutil
import glob


def homework_0_task(base_path):
    for dir_name in ['dir_a', 'dir_b', 'dir_c']:
        os.makedirs(os.path.join(base_path, 'homework_0', dir_name), exist_ok=True)


def homework_1_task(base_path):
    for file_name in ['a.txt', 'b.txt', 'c.txt']:
        shutil.copy(os.path.join(base_path, 'homework_1', file_name),
                    os.path.join(base_path, 'homework_1', f"{file_name}.bak"))


def homework_2_task(base_path):
    for old_name, new_name in [('a.txt', 'a_new.txt'), ('b.txt', 'b_new.txt'), ('c.txt', 'c_new.txt')]:
        os.rename(os.path.join(base_path, 'homework_2', old_name),
                  os.path.join(base_path, 'homework_2', new_name))


def homework_3_task(base_path):
    for file_name in ['a.txt', 'b.txt', 'c.txt']:
        shutil.move(os.path.join(base_path, 'homework_3', 'dir_a', file_name),
                    os.path.join(base_path, 'homework_3', 'dir_b', file_name))


def homework_4_task(base_path):
    for file_name in ['a.txt', 'b.txt', 'c.txt']:
        file_path = os.path.join(base_path, 'homework_4', file_name)
        if os.path.exists(file_path):
            os.remove(file_path)


def homework_5_task(base_path):
    for dir_name in ['dir_a', 'dir_b', 'dir_c']:
        dir_path = os.path.join(base_path, 'homework_5', dir_name)
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)


def homework_6_task(base_path):
    os.rename(os.path.join(base_path, 'homework_6', 'task.txt'),
              os.path.join(base_path, 'homework_6', 'done.txt'))
    os.makedirs(os.path.join(base_path, 'homework_6', 'dir_a'), exist_ok=True)
    shutil.move(os.path.join(base_path, 'homework_6', 'done.txt'),
                os.path.join(base_path, 'homework_6', 'dir_a', 'done.txt'))


def homework_7_task(base_path):
    for i in range(3):
        dir_path = os.path.join(base_path, 'homework_7', f'dir_{i}')
        os.makedirs(dir_path, exist_ok=True)
        for file_name in ['a.txt', 'b.txt', 'c.txt']:
            shutil.copy(os.path.join(base_path, 'homework_7', file_name),
                        os.path.join(dir_path, f"{file_name[0]}{i}.txt"))


def homework_8_task(base_path):
    a_txt_path = os.path.join(base_path, 'homework_8', 'dir_a', 'a.txt')
    if os.path.exists(a_txt_path):
        os.remove(a_txt_path)

    b_txt_path = os.path.join(base_path, 'homework_8', 'dir_b', 'b.txt')
    b_new_txt_path = os.path.join(base_path, 'homework_8', 'dir_b', 'b_new.txt')
    if os.path.exists(b_txt_path):
        os.rename(b_txt_path, b_new_txt_path)

    c_txt_path = os.path.join(base_path, 'homework_8', 'dir_c', 'c.txt')
    c_txt_bak_path = os.path.join(base_path, 'homework_8', 'dir_c', 'c.txt.bak')
    if os.path.exists(c_txt_path):
        shutil.copy(c_txt_path, c_txt_bak_path)


def homework_9_task(base_path):
    for txt_file in glob.glob(os.path.join(base_path, 'homework_9', '*.txt')):
        os.remove(txt_file)


def execute_all_homework(base_path):
    homework_0_task(base_path)  # Creates directories.
    homework_1_task(base_path)  # Copies files to a specific location.
    homework_2_task(base_path)  # Renames files according to a defined pattern.
    homework_3_task(base_path)  # Moves files to a new location.
    homework_4_task(base_path)  # Deletes specific files.
    homework_5_task(base_path)  # Deletes specific directories.
    homework_6_task(base_path)  # Renames and then moves files.
    homework_7_task(base_path)  # Copies and renames files.
    homework_8_task(base_path)  # Performs various file operations.
    homework_9_task(base_path)  # Deletes all .txt files in a specific directory.


if __name__ == "__main__":
    base_path = '/home/acs/homework/lesson_1'
    execute_all_homework(base_path)
