#!/bin/bash
> ./victim.list
for param in "$@"; do
    echo "$param" >> ./victim.list
done