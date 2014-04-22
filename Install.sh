#!/bin/bash
mkdir -p ~/texmf/tex/latex/tikzcivil
cp tikzcivil.sty ~/texmf/tex/latex/tikzcivil
cp tikzcivil-structural.tex ~/texmf/tex/latex/tikzcivil
cp tikzcivil-geomechanics.tex ~/texmf/tex/latex/tikzcivil

texhash ~/texmf
