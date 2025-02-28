#!/bin/bash


# Enter the homework_0 directory and create folders
# ------------------------------------------------
cd /home/acs/homework/lesson_1/homework_0
mkdir dir_a dir_b dir_c


# Enter the homework_1 directory and copy files
# ------------------------------------------------
cd ../homework_1
cp a.txt a.txt.bak
cp b.txt b.txt.bak
cp c.txt c.txt.bak


# Enter the homework_2 directory and rename files
# ------------------------------------------------
cd ../homework_2
mv a.txt a_new.txt
mv b.txt b_new.txt
mv c.txt c_new.txt


# Enter the homework_3 directory and move files
# ------------------------------------------------
cd ../homework_3
mv dir_a/a.txt dir_a/b.txt dir_a/c.txt dir_b/


# Enter the homework_4 directory and delete files
# ------------------------------------------------
cd ../homework_4
rm a.txt b.txt c.txt


# Enter the homework_5 directory and delete directories
# ------------------------------------------------
cd ../homework_5
rm -r dir_a dir_b dir_c


# Enter the homework_6 directory, rename and move file
# ------------------------------------------------
cd ../homework_6
mv task.txt done.txt
mkdir dir_a
mv done.txt dir_a/


# Enter the homework_7 directory and manipulate files
# ------------------------------------------------
cd ../homework_7
mkdir dir_0 dir_1 dir_2
for i in 0 1 2; do
    cp a.txt b.txt c.txt dir_$i/
    mv dir_$i/a.txt dir_$i/a${i}.txt
    mv dir_$i/b.txt dir_$i/b${i}.txt
    mv dir_$i/c.txt dir_$i/c${i}.txt
done


# Enter the homework_8 directory and execute operations
# ------------------------------------------------
cd ../homework_8
rm dir_a/a.txt
mv dir_b/b.txt dir_b/b_new.txt
cp dir_c/c.txt dir_c/c.txt.bak


# Enter the homework_9 directory and delete all .txt files
# ------------------------------------------------
cd ../homework_9
find . -type f -name "*.txt" -delete
