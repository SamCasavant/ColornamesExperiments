# Colornames Experiments

## Introduction

This is a repo of some work I've done with visualizing the Colornames.org project. The code runs on the data available here: https://colornames.org/download/, stored as colornames.txt in the main directory. 

In its current state, this will output the following visualization

![Color Space](Figure_1.png?raw=true "A 3d map of some color names")
## Installation

```
pip install matplotlib pillow mplcursors numpy
git clone https://github.com/SamCasavant/ColornamesExperiments.git
cd ColornamesExperiments
curl https://colornames.org/download/colornames.zip colornames.zip > colornames.zip
unzip colornames.zip
rm colornames.zip
python colornames.py
```

## Purpose

This is an experiment towards the goal of filling out the gaps in the colornames project with AI. In the future, each word might be converted into a vector, (eg. 'dark' is a vector with moderate magnitude in the negative of r, g, and b), and the vectors might be used to produce 