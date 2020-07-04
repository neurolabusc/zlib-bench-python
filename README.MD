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
zstd	1	624	628	633	340	34.69
zstd	2	719	729	735	295	32.86
zstd	3	944	951	957	225	31.47
zstd	4	1020	1028	1033	208	30.93
zstd	5	1735	1750	1759	122	30.22
zstd	6	2116	2127	2146	100	29.70
zstd	7	2824	2841	2872	75	28.97
zstd	8	3448	3501	3532	61	28.69
zstd	9	4397	4442	4481	48	28.42
zstd	10	5387	5446	5498	39	28.11
zstd	11	7233	7250	7267	29	27.97
zstd	12	9495	9751	9906	22	27.75
zstd	13	13751	13842	13930	15	27.43
zstd	14	17115	17228	17329	12	27.19
zstd	15	22535	22687	22926	9	27.01
zstd	16	29581	29904	30080	7	26.29
zstd	17	37803	38170	38403	6	25.78
zstd	18	47500	47928	48446	4	25.34
zstd	19	61459	61742	62495	3	25.13
gzip	1	2511	2539	2569	84	36.50
gzip	2	2679	2711	2736	79	35.44
gzip	3	3310	3332	3347	64	34.46
gzip	4	3431	3469	3506	62	33.52
gzip	5	4465	4508	4537	47	32.62
gzip	6	6365	6420	6476	33	32.19
gzip	7	7610	7704	7773	28	32.05
gzip	8	11146	11209	11344	19	31.93
gzip	9	13990	14169	14345	15	31.91
libdeflate	1	1231	1242	1249	172	34.59
libdeflate	2	1320	1331	1335	161	33.77
libdeflate	3	1449	1468	1481	146	33.34
libdeflate	4	1640	1657	1675	129	32.94
libdeflate	5	1804	1818	1828	117	32.32
libdeflate	6	2174	2207	2231	97	32.05
libdeflate	7	2799	2834	2856	76	31.90
libdeflate	8	8955	8997	9048	24	31.55
libdeflate	9	12273	12390	12463	17	31.01
zlibCFclang	1	1723	1735	1763	123	35.80
zlibCFclang	2	1814	1819	1826	117	35.00
zlibCFclang	3	2047	2064	2074	104	34.37
zlibCFclang	4	2211	2250	2299	96	33.46
zlibCFclang	5	2815	2857	2900	75	32.61
zlibCFclang	6	3595	3626	3651	59	32.35
zlibCFclang	7	4155	4185	4216	51	32.25
zlibCFclang	8	6045	6101	6147	35	32.17
zlibCFclang	9	7987	8085	8168	27	32.15
zlibCFgcc	1	1576	1597	1609	134	35.80
zlibCFgcc	2	1661	1676	1692	128	35.00
zlibCFgcc	3	1896	1907	1918	112	34.37
zlibCFgcc	4	2084	2132	2175	102	33.46
zlibCFgcc	5	2626	2654	2669	81	32.61
zlibCFgcc	6	3366	3431	3467	63	32.35
zlibCFgcc	7	3997	4020	4039	53	32.25
zlibCFgcc	8	5847	5881	5922	36	32.17
zlibCFgcc	9	7842	7919	7964	27	32.15
zlibMadler	1	2584	2607	2641	82	36.45
zlibMadler	2	2779	2794	2816	76	35.39
zlibMadler	3	3359	3389	3419	63	34.43
zlibMadler	4	3485	3518	3560	61	33.50
zlibMadler	5	4665	4702	4717	45	32.63
zlibMadler	6	6603	6680	6724	32	32.19
zlibMadler	7	7953	8053	8138	27	32.05
zlibMadler	8	11823	11893	11991	18	31.94
zlibMadler	9	14943	15091	15301	14	31.92
zlibNGclang	1	972	989	998	218	47.69
zlibNGclang	2	1622	1627	1632	131	35.54
zlibNGclang	3	1954	1961	1968	108	34.22
zlibNGclang	4	2191	2232	2262	97	32.95
zlibNGclang	5	2425	2446	2476	87	32.67
zlibNGclang	6	2919	2948	2970	73	32.51
zlibNGclang	7	4365	4396	4434	49	32.25
zlibNGclang	8	6614	6698	6762	32	32.17
zlibNGclang	9	9017	9132	9214	24	32.15
zlibNGgcc	1	1078	1099	1112	197	47.69
zlibNGgcc	2	1720	1731	1741	123	35.54
zlibNGgcc	3	2043	2061	2067	104	34.22
zlibNGgcc	4	2385	2410	2429	89	32.95
zlibNGgcc	5	2610	2637	2673	81	32.67
zlibNGgcc	6	3101	3117	3150	68	32.51
zlibNGgcc	7	4409	4452	4555	48	32.25
zlibNGgcc	8	6595	6667	6742	32	32.17
zlibNGgcc	9	9139	9239	9365	23	32.15

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
 - [deflatebench](https://github.com/zlib-ng/deflatebench) is a Python script for testing gz compression. It attempts to control low level CPU features (like turbo modes that can boost performance for short bursts) that can lead to variability in benchmark timing.
 
 

