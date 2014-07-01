# -*- coding: utf-8 -*-
import os
import shutil
import tempfile
from subprocess import call

def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)

def main():
    #Files to be installed
    files = ['tikzcivil-geomechanics.tex',
            'tikzcivil-structural.tex',
            'tikzcivil.sty']

    #Create texmf folder if it doesn't exists
    texdir = os.path.expanduser('~texmf/tex/latex/tikzcivil')
    ensure_dir(texdir)

    for i in range(3):
        dstdir = os.path.expanduser(os.path.join('~texmf/tex/latex/tikzcivil', files[i]))
        shutil.copy(files[i], dstdir)
        print(files[i] + ' copied to ' + texdir)

    call(["initexmf", "--update-fndb"])

if __name__ == '__main__':
    main()
