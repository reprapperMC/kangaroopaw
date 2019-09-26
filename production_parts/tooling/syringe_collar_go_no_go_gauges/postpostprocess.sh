#!/bin/bash

sed -i 's/M6 T\([0-9.-]*\)/M6 T\1 G43 H\1/g' "$1" 
