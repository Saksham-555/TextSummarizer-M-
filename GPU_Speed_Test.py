"""
GPU vs CPU Speed Test
This will show you the exact speedup from using GPU
"""

import torch
import time

print("="*60)
print("GPU vs CPU SPEED TEST")
print("="*60)

# Test parameters
matrix_size = 5000
iterations = 10

# ==========================================
# CPU Test
# ==========================================
print("\n🔵 Testing CPU performance...")
device_cpu = torch.device("cpu")

start_time = time.time()
for i in range(iterations):
    a = torch.randn(matrix_size, matrix_size, device=device_cpu)
    b = torch.randn(matrix_size, matrix_size, device=device_cpu)
    c = torch.matmul(a, b)
    
cpu_time = time.time() - start_time
print(f"   CPU Time: {cpu_time:.2f} seconds")

# ==========================================
# GPU Test
# ==========================================
if torch.cuda.is_available():
    print("\n🟢 Testing GPU performance...")
    device_gpu = torch.device("cuda")
    
    # Warmup
    a = torch.randn(matrix_size, matrix_size, device=device_gpu)
    b = torch.randn(matrix_size, matrix_size, device=device_gpu)
    c = torch.matmul(a, b)
    torch.cuda.synchronize()  # Wait for GPU to finish
    
    # Actual test
    start_time = time.time()
    for i in range(iterations):
        a = torch.randn(matrix_size, matrix_size, device=device_gpu)
        b = torch.randn(matrix_size, matrix_size, device=device_gpu)
        c = torch.matmul(a, b)
        torch.cuda.synchronize()
    
    gpu_time = time.time() - start_time
    print(f"   GPU Time: {gpu_time:.2f} seconds")
    
    # ==========================================
    # Results
    # ==========================================
    speedup = cpu_time / gpu_time
    print("\n" + "="*60)
    print("RESULTS:")
    print(f"  CPU: {cpu_time:.2f}s")
    print(f"  GPU: {gpu_time:.2f}s")
    print(f"  🚀 Speedup: {speedup:.1f}x faster on GPU")
    print("="*60)
    
    if speedup < 2:
        print("\n⚠️  WARNING: GPU is not much faster than CPU!")
        print("   Possible issues:")
        print("   1. Data transfer overhead")
        print("   2. Small batch size")
        print("   3. GPU not being used properly")
    elif speedup > 10:
        print("\n✅ EXCELLENT! GPU is significantly faster.")
        print("   Your training should see similar speedup.")
    else:
        print("\n✅ GOOD! GPU is faster than CPU.")
        print("   Training should be noticeably faster.")
else:
    print("\n❌ GPU not available - cannot run GPU test")
    print("   Install CUDA-enabled PyTorch to use GPU")

print("\n" + "="*60)