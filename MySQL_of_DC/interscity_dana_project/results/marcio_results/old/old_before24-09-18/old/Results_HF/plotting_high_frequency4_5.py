import matplotlib
import matplotlib.pyplot as plt
import json


#var prepping
list = []


yValues3 = []
xValues3 = []
xController3 = 0

yValues4 = []
xValues4 = []
xController4 = 0

#getting data

file3 = open("Results_HF_Compression_6RemoteApps.data", "r") 
for line3 in file3: 
	j3 = json.loads(line3)
	xValues3.append(xController3)
	yValues3.append(j3['metrics'][0]['value']/j3['metrics'][0]['count'])
	xController3 = xController3 + 5

file4 = open("Results_HF_CacheAndCompression_6RemoteApps.data", "r") 
for line4 in file4: 
	j4 = json.loads(line4)
	xValues4.append(xController4)
	yValues4.append(j4['metrics'][0]['value']/j4['metrics'][0]['count'])
	xController4 = xController4 + 5


#plotting graph
fig, ax = plt.subplots()

ax.plot(xValues3, yValues3, label='Compression')
ax.plot(xValues4, yValues4, label='CacheAndCompression')
ax.legend()
ax.set(xlabel='Time (s)', ylabel='Response time (ms)', title='High-Frequency (compression-cacheAndcompression) Workload')
ax.grid()
fig.savefig("high_frequency_compression_cacheandcompression.png")
plt.show()
