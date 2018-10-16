#!/usr/bin/env bash

head -n 6066 ./a/data1_final_t.txt > ./b/train3.txt
head -n 6066 ./a/data1_final_f.txt > cat>>./b/train3.txt
tail -n 2022 ./a/data1_final_t.txt > ./b/test3.txt
tail -n 2022 ./a/data1_final_f.txt > cat>>./b/test3.txt