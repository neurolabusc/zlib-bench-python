# zlib-bench for Python

## Introduction

These simple Python scripts benchmark different zlib compression libraries. The  graph below shows the performance of [zlib-ng](https://github.com/zlib-ng/zlib-ng) variants:

![alt tag](https://github.com/neurolabusc/zlib-bench-python/blob/master/silesia_speed_size.png)

To run this script, you would run the following commands:

```
a_compile.py
b_speed_test.py
```


The script `a_compile.py` downloads the [silesia corpus](http://sun.aei.polsl.pl/~sdeor/index.php?page=silesia) and compiles the versions of zlib to be tested. By default it will compile zlib-ng using the gcc and clang compilers. This assumes you have both compilers installed and they are named `gcc` and `clang`. You may need to edit this for your system. for example on MacOS `gcc` is actually an alias for `clang`, so you will have to provide an explicit name for gcc (e.g. `gcc-9` and `g++-9` for the c and c++ compilers).

The script `a_compile.py` optionally allows you to test the [CloudFlare variant of zlib](https://github.com/cloudflare/zlib). To enable this you must use a text editor to uncomment the line
```
    #compile_cloudflare()
```
To read
```
    compile_cloudflare()
```

The script `b_speed_test.py` allows us to compare speed of compression and decompression. 

```
CompressMethod	Level	Min	Mean	Max	mb/s	%
gzip	2	2704	2709	2714	78	35.44
gzip	3	3287	3307	3327	64	34.46
gzip	4	3485	3493	3500	61	33.52
gzip	5	4450	4520	4590	48	32.62
gzip	6	6405	6426	6447	33	32.19
gzip	7	7818	7859	7901	27	32.05
gzip	8	11292	11308	11325	19	31.93
gzip	9	14168	14199	14229	15	31.91
minigzgcc	2	1839	1839	1839	115	35.54
minigzgcc	3	2153	2158	2163	98	34.22
minigzgcc	4	2415	2426	2437	88	32.95
minigzgcc	5	2599	2614	2629	82	32.67
minigzgcc	6	3065	3076	3086	69	32.51
minigzgcc	7	4481	4499	4517	47	33.61
minigzgcc	8	6283	6331	6378	34	33.52
minigzgcc	9	8263	8360	8458	26	33.51
minigzclang	2	1719	1721	1723	123	35.54
minigzclang	3	2012	2021	2031	105	34.22
minigzclang	4	2199	2215	2232	96	32.95
minigzclang	5	2465	2471	2478	86	32.67
minigzclang	6	2920	2945	2971	73	32.51
minigzclang	7	4462	4492	4522	47	33.61
minigzclang	8	6409	6446	6482	33	33.52
minigzclang	9	8565	8655	8744	25	33.51
DecompressMethod	Min	Mean	Max	mb/s
gzip	26661	26830	26999	190.79
minigzgcc	18845	19070	19294	269.91
minigzclang	18274	18689	19105	278.35
```

Be warned that this script will use a huge amount of disk space. The Silesia coprpus is large, and for the decomrpression test each compression tool contributes a compressed version of this corpus at each compression level (1..9).

## Alternatives

 - [zlib-bench](https://github.com/jsnell/zlib-bench) is a perl script.
 - [pigz-bench-python](https://github.com/neurolabusc/pigz-bench-python) tests the parallel compressor pigz.
 
 

