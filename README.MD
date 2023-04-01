# zlib-bench for Python

## Introduction

Evaluation and validation of [zlib](https://github.com/dougallj/zlib-dougallj) decompression optimizations described by [dougallj](https://dougallj.wordpress.com/2022/08/20/faster-zlib-deflate-decompression-on-the-apple-m1-and-x86/). Note that some of these optimizations have already been incorporated into [CloudFlare](https://github.com/cloudflare/zlib/pull/40) zlib.

This script evaluates the performance benefit of bringing one more dougallj optimization to CloudFlare: the `zlibUDOT` library adds the [dot product](https://developer.arm.com/architectures/instruction-sets/intrinsics/vdotq_u32) instruction that is supported by all Apple Silicon (e.g. M1, M2) CPUs. As noted by [dougallj](https://dougallj.wordpress.com/2022/08/20/faster-zlib-deflate-decompression-on-the-apple-m1-and-x86/) the benefit of this single modification is small, but adds to the incremental gains.

To run this script, you would run the following commands:

```
git clone --branch udot git@github.com:neurolabusc/zlib-bench-python.git
cd zlib-bench-python 
python a_compile.py
python b_speed_test.py
```

Sample performance for a M2 Pro:

| DecompressMethod | mb/s   |
|------------------|--------|
| zlibMadler       | 165.25 |
| zlibCF           | 446.46 |
| zlibUDOT         | 449.34 |
| zlibDJ           | 578.29 |
