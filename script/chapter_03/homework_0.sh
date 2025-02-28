#! /bin/bash

dir_0=/home/acs/homework/lesson_1/homework_0
dir_1=/home/acs/homework/lesson_1/homework_1
dir_2=/home/acs/homework/lesson_1/homework_2
dir_3=/home/acs/homework/lesson_1/homework_3
dir_4=/home/acs/homework/lesson_1/homework_4
dir_5=/home/acs/homework/lesson_1/homework_5
dir_6=/home/acs/homework/lesson_1/homework_6
dir_7=/home/acs/homework/lesson_1/homework_7
dir_8=/home/acs/homework/lesson_1/homework_8
dir_9=/home/acs/homework/lesson_1/homework_9

# ************* homework_0 **********************

for i in dir_a dir_b dir_c
do
    mkdir ${dir_0}/$i
done

# ************* homework_1 **********************

for i in a.txt b.txt c.txt
do
    cp ${dir_1}/${i} ${dir_1}/${i}.bak
done

# ************* homework_2 **********************

for i in a b c
do
    mv ${dir_2}/${i}.txt ${dir_2}/${i}_new.txt
done

# ************ homework_3 ***********************

for i in a.txt b.txt c.txt
do
    mv ${dir_3}/dir_a/${i} ${dir_3}/dir_b
done

# *********** homework_4 ************************

for i in a.txt b.txt c.txt
do
    rm ${dir_4}/${i}
done

# *********** homework_5 ************************

for i in dir_a dir_b dir_c
do
    rm ${dir_5}/${i} -r
done

# ********** homework_6 *************************

mv ${dir_6}/task.txt "${dir_6}/done.txt"
mkdir ${dir_6}/dir_a
mv "${dir_6}/done.txt" ${dir_6}/dir_a

# ********** homework_7 *************************

for i in 0 1 2
do
    mkdir ${dir_7}/dir_${i}
    for j in a b c
    do
        cp ${dir_7}/${j}.txt ${dir_7}/dir_${i}/${j}${i}.txt
    done
done

# ********** homework_8 *************************

rm ${dir_8}/dir_a/a.txt
mv ${dir_8}/dir_b/b.txt ${dir_8}/dir_b/b_new.txt
cp ${dir_8}/dir_c/c.txt ${dir_8}/dir_c/c.txt.bak

# ********* homework_9 **************************

rm ${dir_9}/*.txt

# *********** finish ****************************
