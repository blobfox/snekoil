#!/bin/sh

echo "conventional.py: "
time python3 ./benchmarks/range/conventional.py > /dev/null

echo
echo
echo "with_snakeoil.py: "
time python3 ./benchmarks/range/with_snakeoil.py > /dev/null
