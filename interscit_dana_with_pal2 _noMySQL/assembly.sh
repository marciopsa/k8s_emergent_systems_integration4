#!/bin/bash

service mysql start

sleep 30

dana DCScheme.o

dana -sp ../dc/ EmergentSys.o ../../dana/components/ws/core.o -p 2020
