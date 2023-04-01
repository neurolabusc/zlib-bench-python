# zlib-bench for Python

## Introduction

Evaluation and validation of [zlib](https://github.com/dougallj/zlib-dougallj) decompression optimizations described by [dougallj](https://dougallj.wordpress.com/2022/08/20/faster-zlib-deflate-decompression-on-the-apple-m1-and-x86/). Note that some of these optimizations have already been incorporated into [CloudFlare](https://github.com/cloudflare/zlib/pull/40) zlib.


To run this script, you would run the following commands:

```
git clone --branch dougallj git@github.com:neurolabusc/zlib-bench-python.git
cd zlib-bench-python 
python a_compile.py
python b_speed_test.py
```

Sample performance for a M2 Pro:

| DecompressMethod | Min   | Mean  | Max   | mb/s   |
|------------------|-------|-------|-------|--------|
| zlibCF           | 17393 | 17820 | 18546 | 438.68 |
| zlibDJ           | 13578 | 13590 | 13613 | 561.94 |
| zlibMadler       | 46714 | 46798 | 46905 | 163.33 |
| zlibNG           | 14924 | 14965 | 15010 | 511.25 |
