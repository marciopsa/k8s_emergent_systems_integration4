#!/bin/bash

#cd HFU_LV/K8s_no_PAL
chmod +x workload_generator.sh
chmod +x sonda_client.sh
xterm -e ./sonda_client.sh & xterm -e ./hfu_lv_nopal.sh
