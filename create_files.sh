#!/bin/bash
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 YEAR" >&2
    exit 1
fi
year="$1"
echo "Creating directories and files for Advent of Code $year"
mkdir -p "AdventOfCode${year}"
cd "AdventOfCode${year}"

for i in $(seq 1 12); do
  A=$(printf "%02d" "$i")
  echo "$A"
  mkdir -p "$dir"
  touch "$dir/Day${A}IN.txt" "$dir/Day${A}INtest.txt" "$dir/Day${A}P1.py" "$dir/Day${A}P2.py"
done