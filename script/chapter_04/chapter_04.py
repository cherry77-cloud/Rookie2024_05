import os
import paramiko
import subprocess


def create_ssh_client(host, port, username, key_file):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=username, key_filename=key_file)
    return client


def homework_1(ssh_client):
    local_main_cpp_path = "/home/acs/homework/lesson_4/homework_1/main.cpp"
    local_dir_path = "/home/acs/homework/lesson_4/homework_1/dir"
    remote_dir_path = "/home/acs_5293/homework/lesson_4/homework_1"
    stdin, stdout, stderr = ssh_client.exec_command(f"mkdir -p {remote_dir_path} && rm -rf {remote_dir_path}/*")
    if stderr.read():
        print("Error in creating and emptying remote directory.")

    try:
        sftp = ssh_client.open_sftp()
        sftp.put(local_main_cpp_path, os.path.join(remote_dir_path, 'main.cpp'))
    except FileNotFoundError:
        print(f"Local file not found: {local_main_cpp_path}")
        return
    except Exception as e:
        print(f"Error during file upload: {e}")
        return

    try:
        os.makedirs(local_dir_path, exist_ok=True)
        sftp.get('/etc/lsb-release', os.path.join(local_dir_path, 'lsb-release'))
    except FileNotFoundError:
        print("Remote file not found: /etc/lsb-release")
        return
    except Exception as e:
        print(f"Error during file download: {e}")
        return
    finally:
        sftp.close()


def homework_2(ssh_client):
    local_dir_path = "/home/acs/homework/lesson_4/homework_2/dir"
    remote_dir_path = "/home/acs_5293/homework/lesson_4/homework_2"
    try:
        stdin, stdout, stderr = ssh_client.exec_command(f"mkdir -p {remote_dir_path} && rm -rf {remote_dir_path}/*")
        error_msg = stderr.read().decode()
        if error_msg:
            print(f"Error in creating and emptying remote directory: {error_msg}")
            return
        scp_command = f"scp -r {local_dir_path} myserver:{remote_dir_path}"
        subprocess.run(scp_command, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error during scp command execution: {e}")
    except FileNotFoundError:
        print(f"Local file or directory not found: {local_dir_path}")
    except paramiko.SSHException as e:
        print(f"SSH error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def homework_3(host, username):
    local_dir_path = "/home/acs/homework/lesson_4/homework_3/dir"
    remote_dir_path = "/var/lib/locales/supported.d"
    os.makedirs(local_dir_path, exist_ok=True)
    scp_command = f"scp -r {username}@{host}:{remote_dir_path}/ {local_dir_path}"
    try:
        subprocess.run(scp_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during scp command execution: {e}")


def create_bash_script(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    os.chmod(file_path, 0o755)


def homework_4(ssh_client):
    remote_dir_path = "/home/acs_5293/homework/lesson_4/homework_4"
    stdin, stdout, stderr = ssh_client.exec_command(f"mkdir -p {remote_dir_path} && rm -rf {remote_dir_path}/*")
    if stderr.read():
        print("Error in creating and emptying remote directory.")

    # remote_mkdir.sh 脚本内容
    remote_mkdir_content = (
        '#! /bin/bash\n\n'
        'ssh myserver mkdir -p homework/lesson_4/homework_4/\\"$1\\"\n'
    )

    # remote_rmdir.sh 脚本内容
    remote_rmdir_content = (
        '#! /bin/bash\n\n'
        'ssh myserver rm -r homework/lesson_4/homework_4/\\"$1\\"\n'
    )

    # 创建脚本文件
    create_bash_script('/home/acs/homework/lesson_4/homework_4/remote_mkdir.sh', remote_mkdir_content)
    create_bash_script('/home/acs/homework/lesson_4/homework_4/remote_rmdir.sh', remote_rmdir_content)


if __name__ == "__main__":
    host = "**.**.**.**"
    port = 22
    username = "acs_5293"
    key_file = "/home/acs/.ssh/id_rsa"

    ssh_client = create_ssh_client(host, port, username, key_file)

    homework_1(ssh_client)
    homework_2(ssh_client)
    homework_3(host=host, username=username)
    homework_4(ssh_client)
    ssh_client.close()
