# zlib-bench for Python

## Introduction

These simple Python scripts benchmark different zlib compression libraries. The  graph below shows the performance of methods to compress files into the popular gzip format. Options include Mark Adler's popular [zlib](https://github.com/madler/zlib), the [zlib-ng](https://github.com/zlib-ng/zlib-ng), the [CloudFlare zlib](https://github.com/cloudflare/zlib), the classic [gzip](https://www.gzip.org) and [libdeflate](https://github.com/ebiggers/libdeflate). Note that libdeflate has outstanding performance, but does not work with streams, so it fills a different niche than the zlib libraries. The simplicity of gzip and its early introduction mean it remains extremely popular. However, for context the graph also shows the performance of the modern [zstd](https://github.com/facebook/zstd) compression format, which leverages hardware and concepts that were not available when gz was developed.

![alt tag](https://github.com/neurolabusc/zlib-bench-python/blob/master/silesia_speed_size.png)

To run this script, you would run the following commands:

```
a_compile.py
b_speed_test.py
```


The script `a_compile.py` downloads the [silesia corpus](http://sun.aei.polsl.pl/~sdeor/index.php?page=silesia) and compiles the versions of zlib to be tested. For Linux uses, it will compile zlib-ng and CloudFlare using both the gcc and clang compilers. This assumes you have both compilers installed and they are named `gcc` and `clang`. 


The script `b_speed_test.py` allows us to compare speed of compression and decompression. Here is the output for the default Silesia corpus. 

```
CompressMethod	Level	Min	Mean	Max	mb/s	%
zstd	1	618	624	632	343	34.69
zstd	2	721	729	739	294	32.86
zstd	3	956	962	972	222	31.47
zstd	4	1015	1032	1044	209	30.93
zstd	5	1756	1783	1806	121	30.22
zstd	6	2164	2176	2187	98	29.70
zstd	7	2857	2872	2900	74	28.97
zstd	8	3505	3531	3564	60	28.69
zstd	9	4495	4527	4571	47	28.42
zstd	10	5613	5672	5756	38	28.11
zstd	11	7328	7392	7460	29	27.97
zstd	12	9949	10156	10341	21	27.75
zstd	13	13986	14156	14289	15	27.43
zstd	14	17630	18024	18434	12	27.19
zstd	15	23370	23495	23818	9	27.01
zstd	16	30708	30861	31009	7	26.29
zstd	17	38423	38641	38906	6	25.78
zstd	18	47952	48761	49395	4	25.34
zstd	19	62927	63382	63904	3	25.13
gzip	1	2509	2522	2548	84	36.50
gzip	2	2681	2690	2707	79	35.44
gzip	3	3288	3328	3344	64	34.46
gzip	4	3436	3462	3480	62	33.52
gzip	5	4478	4508	4546	47	32.62
gzip	6	6353	6400	6491	33	32.19
gzip	7	7588	7652	7710	28	32.05
gzip	8	11244	11285	11352	19	31.93
gzip	9	14047	14095	14173	15	31.91
libdeflate	1	1238	1248	1267	171	34.59
libdeflate	2	1329	1337	1343	159	33.77
libdeflate	3	1452	1467	1484	146	33.34
libdeflate	4	1625	1634	1649	130	32.94
libdeflate	5	1817	1829	1846	117	32.32
libdeflate	6	2138	2164	2197	99	32.05
libdeflate	7	2764	2784	2823	77	31.90
libdeflate	8	8888	8937	8985	24	31.55
libdeflate	9	12344	12447	12534	17	31.01
zlibCFclang	1	1716	1733	1761	124	35.80
zlibCFclang	2	1797	1818	1840	118	35.00
zlibCFclang	3	2035	2043	2050	104	34.37
zlibCFclang	4	2594	2617	2638	82	34.63
zlibCFclang	5	3047	3062	3091	70	34.00
zlibCFclang	6	3790	3815	3841	56	33.72
zlibCFclang	7	4351	4375	4402	49	33.61
zlibCFclang	8	6210	6302	6367	34	33.52
zlibCFclang	9	8338	8392	8424	25	33.51
zlibCFgcc	1	1577	1595	1614	134	35.80
zlibCFgcc	2	1662	1671	1692	128	35.00
zlibCFgcc	3	1889	1908	1924	112	34.37
zlibCFgcc	4	2393	2420	2435	89	34.63
zlibCFgcc	5	2806	2836	2867	76	34.00
zlibCFgcc	6	3591	3623	3646	59	33.72
zlibCFgcc	7	4105	4163	4247	52	33.61
zlibCFgcc	8	5937	5992	6027	36	33.52
zlibCFgcc	9	7873	7906	7924	27	33.51
zlibMadler	1	2535	2560	2595	84	36.45
zlibMadler	2	2726	2762	2792	78	35.39
zlibMadler	3	3349	3373	3391	63	34.43
zlibMadler	4	4139	4185	4216	51	35.08
zlibMadler	5	5179	5225	5259	41	34.30
zlibMadler	6	7383	7428	7503	29	33.81
zlibMadler	7	8725	8847	8900	24	33.66
zlibMadler	8	12558	12712	12883	17	33.53
zlibMadler	9	15814	16027	16249	13	33.51
zlibNGclang	1	1019	1032	1041	208	47.70
zlibNGclang	2	1647	1665	1681	129	35.54
zlibNGclang	3	1975	1991	2004	107	34.22
zlibNGclang	4	2225	2243	2276	95	32.95
zlibNGclang	5	2417	2434	2457	88	32.67
zlibNGclang	6	2963	2980	2993	72	32.51
zlibNGclang	7	4534	4551	4567	47	33.61
zlibNGclang	8	6695	6760	6834	32	33.52
zlibNGclang	9	9146	9224	9355	23	33.51
zlibNGgcc	1	1082	1093	1103	196	47.70
zlibNGgcc	2	1793	1805	1811	118	35.54
zlibNGgcc	3	2137	2143	2156	99	34.22
zlibNGgcc	4	2373	2399	2429	89	32.95
zlibNGgcc	5	2611	2633	2664	81	32.67
zlibNGgcc	6	3068	3113	3159	69	32.51
zlibNGgcc	7	4631	4669	4740	46	33.61
zlibNGgcc	8	6858	6898	6957	31	33.52
zlibNGgcc	9	9278	9369	9463	23	33.51

DecompressMethod	Min	Mean	Max	mb/s
zstd	7643	7889	7994	526.86
gzip	70063	70527	70756	190.57
libdeflate	32336	32477	32630	412.92
zlibCFclang	48796	49065	49470	273.63
zlibCFgcc	49240	49328	49369	271.17
zlibMadler	56574	56746	56918	236.01
zlibNGclang	47293	47366	47423	282.33
zlibNGgcc	48661	48738	48804	274.39
```

You can also test compression of files in any folder you want. Some compression methods are tuned for certain types of data (e.g. English text) and may be relatively worse than other methods for other types of data (e.g. medical images). For example, you can download and test the [Canterbury corpus](https://corpus.canterbury.ac.nz/purpose.html) or the [Calgary corpus](http://www.data-compression.info/Corpora/CalgaryCorpus/). To test the compression of all the files in a folder, provide the folder name as an argument from the command line:

```
b_speed_test.py ./MyFolder
```
For decompression testing, all gz tools are decompressing the same data (addressing a concern by [Sebastian Pop](https://github.com/zlib-ng/zlib-ng/issues/326) that different gzip compressors create different file sizes, and smaller files might be more complicated and therefore slower to extract). In contrast, since zstd is creating files in a different format, it is only decompressing its own files.

Be warned that this script will use a huge amount of disk space. The Silesia coprpus is large, and for the decomrpression test each compression tool contributes a compressed version of this corpus at each compression level (1..9).

## Alternatives

 - [zlib-bench](https://github.com/jsnell/zlib-bench) is a perl script.
 - [pigz-bench-python](https://github.com/neurolabusc/pigz-bench-python) tests the parallel compressor pigz.
 
 

