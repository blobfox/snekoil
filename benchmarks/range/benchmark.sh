#!/bin/sh

echo "conventional.py: "
time python3 ./benchmarks/range/conventional.py > /dev/null

echo
echo
echo "with_snekoil.py: "
time python3 ./benchmarks/range/with_snekoil.py > /dev/null
