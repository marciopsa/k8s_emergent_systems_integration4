#!/bin/bash

service mysql start

sleep 30

dana DCScheme.o

dana -sp ../dc/ InteractiveAssembly.o ../../dana/components/ws/core.o -p 2022


