#!/bin/bash

#cd K8s_no_PAL
chmod +x workload_generator.sh
chmod +x metrics_client.sh
chmod +x hfu_lv_withpal.sh
chmod +x workload_generator.sh
chmod +x K8s_with_PAL_GetMetrics.py
chmod +x K8s_with_PAL_TestApp.py

xterm -e ./metrics_client.sh & xterm -e ./hfu_lv_withpal.sh
