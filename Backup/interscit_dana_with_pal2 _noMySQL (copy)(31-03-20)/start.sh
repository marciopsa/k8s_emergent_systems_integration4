#!/bin/bash

# turn on bash's job control
set -m

# start the primary process and put it in the background
./assembly.sh & 

sleep 60

# start the secundary process
./learner.sh
