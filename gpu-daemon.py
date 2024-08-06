import os
import pynvml
import time


n_gpus = 8
threshold = 0.05
time = 86200

pynvml.nvmlInit()
restart = True
for i in range(n_gpus):
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
    if threshold < meminfo.used / meminfo.total:
        restart = False
        break

if restart:
    os.system(f"docker run --rm --gpus all gpu_burn ./gpu_burn {time}")
else:
    time.sleep(7200)