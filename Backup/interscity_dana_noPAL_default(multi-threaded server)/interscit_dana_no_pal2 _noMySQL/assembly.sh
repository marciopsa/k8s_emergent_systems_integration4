#!/bin/bash

service mysql start

sleep 30

dana DCScheme.o

dana -sp ../dc/ ServerPerception.o ../../dana/components/ws/core.o -p 2020
#dana -sp ../dc/ InteractiveAssembly.o ../../dana/components/ws/core.o -p 2020
