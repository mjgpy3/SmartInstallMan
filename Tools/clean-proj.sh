#!/bin/bash

find .. -name *.pyc | xargs rm

for i in ../Source/smartinst.conf  ../Source/smartpack.lst
do
  rm $i
done

