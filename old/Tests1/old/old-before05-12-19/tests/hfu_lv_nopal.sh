#!/bin/bash

#cd HFU_LV/K8s_no_PAL
#chmod +x workload_generator.sh
#chmod +x sonda_client.sh

#./sonda_client.sh

./workload_generator.sh && pkill -f dana


#xterm -e dana K8s_no_PAL_App.o 

#xterm -e dana K8s_no_PAL_App.o & xterm -e ./K8s_no_PAL_TestApp.py

# & workload_generator.sh && fg

#workload_generator.sh || exit 0


