import torch
if torch.cuda.is_available():
    print("CUDA GPU is available.")
    print("GPU Name:", torch.cuda.get_device_name(0))
    print("Total Memory:", torch.cuda.get_device_properties(0).total_memory / 1024**3, "GB")
else:
    print("CUDA GPU is not available.")



print(torch.version.cuda)
print(torch.__version__)
import torch
print(torch.__file__)

import apex
from apex import amp

print("Apex AMP is available")

