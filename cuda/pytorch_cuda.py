import os
import time

import torch


os.environ["TORCH_CUDA_ARCH_LIST"] = "5.0"
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print(f"using {device} device")
print("Supported GPU Architectures:", torch.cuda.get_arch_list())

matrix_size = 32 * 256
x = torch.randn(matrix_size, matrix_size)
y = torch.randn(matrix_size, matrix_size)

print("*********** CPU SPEED ***********")
start = time.time()
result = torch.matmul(x, y)

print(time.time() - start)
print(f"verify device: {result.device}")

print("*********** GPU SPEED ***********")

start = time.time()
x_gpu = x.to(device)
y_gpu = x.to(device)
torch.cuda.synchronize()
cuda_init_time = time.time() - start

for i in range(3):
    print(">>>>>>>> GPU SPEED <<<<<<<<<<")
    start = time.time()
    result_gpu = torch.matmul(x_gpu, y_gpu)
    torch.cuda.synchronize()
    print(time.time() - start + cuda_init_time)
    print(f"verify device: {result_gpu.device}")



