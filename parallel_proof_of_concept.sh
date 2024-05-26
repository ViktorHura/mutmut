#!/bin/sh

# a copy of the project for each parallel process
cp -R ./benchmark_pacman ./benchmark_pacman%1
cp -R ./benchmark_pacman ./benchmark_pacman%2
cp -R ./benchmark_pacman ./benchmark_pacman%3

# start each parallel process
(cd ./benchmark_pacman%1; mutmut run --paths-to-mutate "./pacman" --tests-dir "./tests" --parallel "1,3" | tail -n 1 > /tmp/job1.ret)&
(cd ./benchmark_pacman%2; mutmut run --paths-to-mutate "./pacman" --tests-dir "./tests" --parallel "2,3" | tail -n 1 > /tmp/job2.ret)&
(cd ./benchmark_pacman%3; mutmut run --paths-to-mutate "./pacman" --tests-dir "./tests" --parallel "3,3" | tail -n 1 > /tmp/job3.ret)&

wait

# fetch results of each process (can be also in xml or other format)
OUT1=$(cat /tmp/job1.ret)
OUT2=$(cat /tmp/job2.ret)
OUT3=$(cat /tmp/job3.ret)

# concatenate them in some way
echo "$OUT1\n$OUT2\n$OUT3"

# delete temporary directories and files ...
rm -r ./benchmark_pacman%1
rm -r ./benchmark_pacman%2
rm -r ./benchmark_pacman%3
rm /tmp/job1.ret
rm /tmp/job2.ret
rm /tmp/job3.ret