#!/bin/bash

# Homework 1
homework_1() {
    local remote_dir="/home/acs_5293/homework/lesson_4/homework_1"
    local local_main_cpp_path="/home/acs/homework/lesson_4/homework_1/main.cpp"
    local local_dir_path="/home/acs/homework/lesson_4/homework_1/dir"
    local remote_file="/etc/lsb-release"

    ssh myserver "mkdir -p $remote_dir && rm -rf $remote_dir/*"
    scp -r $local_main_cpp_path myserver:$remote_dir/
    mkdir -p $local_dir_path
    scp -r myserver:$remote_file $local_dir_path/
}

# Homework 2
homework_2() {
    local remote_dir="/home/acs_5293/homework/lesson_4/homework_2"
    local local_dir_path="/home/acs/homework/lesson_4/homework_2/dir"

    ssh myserver "mkdir -p $remote_dir && rm -rf $remote_dir/*"
    scp -r $local_dir_path myserver:$remote_dir/
}

# Homework 3
homework_3() {
    local local_dir_path="/home/acs/homework/lesson_4/homework_3/dir"
    local remote_dir="/var/lib/locales/supported.d"

    mkdir -p $local_dir_path
    scp -r myserver:$remote_dir/ $local_dir_path/
}

# Homework 4
homework_4() {
    local remote_dir="/home/acs_5293/homework/lesson_4/homework_4"
    # 创建远程目录
    ssh myserver "mkdir -p $remote_dir && rm -rf $remote_dir/*"

    # 创建 remote_mkdir.sh 脚本
    remote_mkdir="/home/acs/homework/lesson_4/homework_4/remote_mkdir.sh"
    echo '#!/bin/bash' > $remote_mkdir
    echo 'ssh myserver mkdir -p homework/lesson_4/homework_4/\"$1\"' >> $remote_mkdir

    # 创建 remote_rmdir.sh 脚本
    remote_rmdir="/home/acs/homework/lesson_4/homework_4/remote_rmdir.sh"
    echo '#!/bin/bash' > $remote_rmdir
    echo 'ssh myserver rm -r homework/lesson_4/homework_4/\"$1\"' >> $remote_rmdir

    # 赋予新创建的脚本执行权限
    chmod +x $remote_mkdir $remote_rmdir
}

homework_1
homework_2
homework_3
homework_4
