# Dissertation for part II of the Computer Science Tripos at the University of Cambridge

This repository contains the LaTeX for my dissertation as well as the final PDFs.

## Project structure

The dissertation folder is split into:
 - `data` (contains simulation output and python scripts for generating graphs)
 - `figures` (contains figures)
 - `tex` (contains the LaTeX source)

## LaTeX stuff

 - I used [subfiles](https://www.ctan.org/pkg/subfiles?lang=en) to split my project into separate files for each chapter, each of which could be compiled independently.
 - The preamble is in `style.sty` and each part is commented
 - By keeping the LaTeX simple, compilation of the entire dissertation completes in 3 seconds on my laptop.
 - The word count can be computed by running `texcount -total -template={sum} *.tex` from inside the `tex` directory
