import torch
# install
# https://developer.nvidia.com/cuda-downloads
# https://pytorch.org/get-started/locally/
# pip uninstall torch torchvision torchaudio        
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Print PyTorch version
print("PyTorch Version:", torch.__version__)

# Print GPU availability
print("GPU Available:", torch.cuda.is_available())

# Print supported GPU architectures
print("Supported GPU Architectures:")
print(torch.cuda.get_arch_list())