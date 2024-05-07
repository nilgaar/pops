#!/bin/bash


file1="./expected_result_username_combiner.list"
file2="./nil_gallego.list"
python3 ../discovery/username_combiner.py nil gallego --domain pops.cafe

sort "$file1" -o "$file1"
sort "$file2" -o "$file2"

diff_output=$(diff "$file1" "$file2")

if [ -z "$diff_output" ]; then
    echo "Files are identical"
else
    echo "Files are different"
    echo "$diff_output"
fi