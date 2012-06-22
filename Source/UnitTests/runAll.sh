#!/bin/bash

cd $PWD

echo ======================================================================
echo *- Running all unit test in the curent directory --------------------*
echo ======================================================================


for f in $(ls *.py)
do
  echo ----------------------------------------------------------------------
  echo "Running Test in $f"
  echo ----------------------------------------------------------------------
  python $f
done

rm ../*.pyc
rm ./*.pyc