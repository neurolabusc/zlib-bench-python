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


def compile_minigzip():
    """compile variants of gz"""

    methods = ['gcc', 'clang']
    ccompiler = ['gcc', 'clang']
    cppcompiler = ['g++', 'clang++']
    if platform.system() == 'Windows':
        methods = ['Cloudflare', 'ng']
    basedir = os.getcwd()
    exedir = os.path.join(basedir, 'exe')
    if os.path.isdir(exedir):
        rmtree(exedir)
    try:
        os.mkdir(exedir)
    except OSError:
        print ("Creation of the directory {} failed" .format(exedir) )
    gzdir = os.path.join(basedir, 'gz')
    if os.path.isdir(gzdir):
        rmtree(gzdir)
    cmd = 'git clone https://github.com/zlib-ng/zlib-ng.git '+gzdir
    subprocess.call(cmd, shell=True)
    gzdir = os.path.join(gzdir,'build')
    gzexe = os.path.join(gzdir, 'minigzip')
    ext = ''
    if platform.system() == 'Windows':
        ext = '.exe'
    gzexe = gzexe + ext
    for m in range(len(methods)):
        method = methods[m]
        os.chdir(basedir)
        if os.path.isdir(gzdir):
            rmtree(gzdir)
        os.mkdir(gzdir)
        os.chdir(gzdir)
        #cmd = 'cmake -DZLIB_IMPLEMENTATION=' + method + ' ..'
        #cmd = 'cmake --zlib-compat  ..'
        
        cmd = 'cmake -D CMAKE_C_COMPILER='+ccompiler[m]+' -D CMAKE_CXX_COMPILER='+cppcompiler[m]+' --zlib-compat  ..'
        subprocess.call(cmd, shell=True)
        #cmd = 'make'
        #if platform.system() == 'Windows':
        cmd = 'cmake --build . --config Release'
        subprocess.call(cmd, shell=True)
        outnm = os.path.join(exedir, 'minigz' + method + ext)
        print (gzexe + '->' + outnm)
        shutil.move(gzexe, outnm)
        st = os.stat(outnm)
        os.chmod(outnm, st.st_mode | stat.S_IEXEC)


if __name__ == '__main__':
    """compile variants of zlib and sample compression corpus"""

    install_silesia_corpus()
    compile_minigzip()
