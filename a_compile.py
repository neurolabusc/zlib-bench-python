#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import stat
import shutil
import subprocess
import platform
import zipfile
from distutils.dir_util import copy_tree

def rmtree(top):
    """Delete folder and contents: shutil.rmtree has issues with read-only files on Windows"""

    for (root, dirs, files) in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            if(os.path.isdir(filename)):
                os.rmdir(filename)
            else:
                os.unlink(filename)
            #os.chmod(filename, stat.S_IWUSR)
            #os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)

def install_silesia_corpus():
    """Install popular Silesia corpus"""

    basedir = os.getcwd()
    corpusdir = os.path.join(basedir, 'silesia')
    if os.path.isdir(corpusdir):
        rmtree(corpusdir)
    try:
        os.mkdir(corpusdir)
    except OSError:
        print('Creation of the directory {} failed' .format(corpusdir) )
    cmd = 'git clone https://github.com/MiloszKrajewski/SilesiaCorpus silesia'
    print("Installing "+corpusdir);
    subprocess.call(cmd, shell=True)
    os.chdir(corpusdir)
    fnm = 'README.md'
    if os.path.isfile(fnm):
        os.remove(fnm)
    ext = '.zip'
    for item in os.listdir(corpusdir):  # loop through items in dir
        print("+"+item)
        if item.endswith(ext):  # check for ".zip" extension
            file_name = os.path.abspath(item)  # get full path of files
            print(file_name)
            zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
            zip_ref.extractall(corpusdir)  # extract file to dir
            zip_ref.close()  # close file
            os.remove(file_name)  # delete zipped file
    os.chdir(basedir)

def compile_libdeflate():
    """compile libdeflate"""

    method = 'libdeflate'
    if platform.system() == 'Windows':
        print('Warning unable to build libdeflate for Windows')
    basedir = os.getcwd()
    exedir = os.path.join(basedir, 'exe')
    try:
        os.mkdir(exedir)
    except OSError:
        print ("Creation of the directory {} failed" .format(exedir) )
    gzdir = os.path.join(basedir, method)
    if os.path.isdir(gzdir):
        rmtree(gzdir)
    cmd = 'git clone https://github.com/ebiggers/libdeflate.git '+gzdir
    subprocess.call(cmd, shell=True)
    os.chdir(gzdir)
    cmd = 'cmake -B build && cmake --build build'
    subprocess.call(cmd, shell=True)
    ext = ''
    if platform.system() == 'Windows':
        ext = '.exe'
    gzexe = os.path.join(gzdir, 'build','programs', 'libdeflate-gzip'+ ext)
    outnm = os.path.join(exedir, method + ext)
    print (gzexe + '->' + outnm)
    shutil.move(gzexe, outnm)
    st = os.stat(outnm)
    os.chmod(outnm, st.st_mode | stat.S_IEXEC)
    os.chdir(basedir)

def cmake_zlib(title, repo, ccompiler):
    """compile CloudFlare zlib executable
    
    title: name for executable, e.g. 'CloudFlare'
    repo: source of Github repository, e.g. "rordenlab/zlib.git"
    ccompiler: names of compilers, "['gcc', 'clang']" or default "[]"
    """

    basedir = os.getcwd()
    exedir = os.path.join(basedir, 'exe')
    #if os.path.isdir(exedir):
    #    rmtree(exedir)
    try:
        os.mkdir(exedir)
    except OSError:
        print ("Creation of the directory {} failed" .format(exedir) )
    gzdir = os.path.join(basedir, 'gz')
    if os.path.isdir(gzdir):
        rmtree(gzdir)
    cmd = 'git clone https://github.com/' + repo + ' ' + gzdir
    subprocess.call(cmd, shell=True)
    gzdir = os.path.join(gzdir,'build')
    gzexe = os.path.join(gzdir, 'minigzip')
    ext = ''
    if platform.system() == 'Windows':
        ext = '.exe'
    gzexe = gzexe + ext
    m = 0;
    while True:
    #for m in range(len(ccompiler)):
        method = title
        compiler = '';
        if (len(ccompiler) > 0):
            compiler = '-DCMAKE_C_COMPILER=' + ccompiler[m]
            method = method+ccompiler[m];
        os.chdir(basedir)
        if os.path.isdir(gzdir):
            rmtree(gzdir)
        os.mkdir(gzdir)
        os.chdir(gzdir)
        cmd = 'cmake '+compiler+' -DBUILD_EXAMPLES=ON  -DZLIB_COMPAT=ON -DUSE_STATIC_RUNTIME=ON  ..'
        subprocess.call(cmd, shell=True)
        cmd = 'cmake --build .'
        subprocess.call(cmd, shell=True)
        outnm = os.path.join(exedir, method + ext)
        print (gzexe + '->' + outnm)
        shutil.move(gzexe, outnm)
        st = os.stat(outnm)
        os.chmod(outnm, st.st_mode | stat.S_IEXEC)
        os.chdir(basedir)
        m = m + 1
        if (m >= len(ccompiler)):
            break

def make_zlib(title, repo, ccompiler):
    """compile CloudFlare zlib executable
    
    title: name for executable, e.g. 'CloudFlare'
    repo: source of Github repository, e.g. "rordenlab/zlib.git"
    ccompiler: ignored
    """

    basedir = os.getcwd()
    exedir = os.path.join(basedir, 'exe')
    try:
        os.mkdir(exedir)
    except OSError:
        print ("Creation of the directory {} failed" .format(exedir) )
    gzdir = os.path.join(basedir, 'gz')
    if os.path.isdir(gzdir):
        rmtree(gzdir)
    cmd = 'git clone https://github.com/' + repo + ' ' + gzdir
    subprocess.call(cmd, shell=True)
    gzexe = os.path.join(gzdir, 'minigzip')
    ext = ''
    if platform.system() == 'Windows':
        ext = '.exe'
    gzexe = gzexe + ext
    method = title
    os.chdir(gzdir)
    cmd = './configure  --static'
    subprocess.call(cmd, shell=True)
    cmd = 'make'
    subprocess.call(cmd, shell=True)
    outnm = os.path.join(exedir, method + ext)
    print (gzexe + '->' + outnm)
    shutil.move(gzexe, outnm)
    st = os.stat(outnm)
    os.chmod(outnm, st.st_mode | stat.S_IEXEC)
    os.chdir(basedir)

if __name__ == '__main__':
    """compile variants of zlib and sample compression corpus"""

    install_silesia_corpus()
    compile_libdeflate()
    ccompiler = []
    if (platform.system() == 'Linux') and shutil.which('gcc') and shutil.which('clang'):
        ccompiler = ['gcc', 'clang']
    cmake_zlib('zlibDJ', 'dougallj/zlib-dougallj.git', ccompiler)
    cmake_zlib('zlibCF', 'rordenlab/zlib.git', ccompiler)
    cmake_zlib('zlibNG', 'zlib-ng/zlib-ng.git', ccompiler) 
    make_zlib('zlibMadler', 'neurolabusc/zlib', ccompiler)
