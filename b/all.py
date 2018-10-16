import os


os.system('head -n 6066 ../a/data1_final_t.txt > train2.txt')
os.system("-n 6066 ../a/data1_final_f.txt > cat>> train2.txt")
os.system("tail -n 2022 ../a/data1_final_t.txt > test2.txt")
os.system("tail -n 2022 ../a/data1_final_f.txt > cat>> test2.txt")