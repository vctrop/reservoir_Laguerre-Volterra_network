#!python3

# MIT License
# Copyright (c) 2020 Victor O. Costa
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
import matplotlib.pyplot as plt
import ant_colony_for_continuous_domains
import optimization_utilities

# Structural parameters  
Fs = 25  
L = 5;   H = 3;    Q = 4;

# Parameters to be optimized
alpha_min   = 0;    alpha_max   = 0.9   # approx lag with 0.9 is 263
weight_min  = -1;  weight_max  = 1
coef_min    = -1;  coef_max    = 1  
offset_min  = -1;  offset_max  = 1
    
# Setup ACOr and optimize
num_iterations = 50
ranges = []
ranges.append([alpha_min,alpha_max])
for _ in range(L * H): 
    ranges.append([weight_min, weight_max])
for _ in range(Q * H):
    ranges.append([coef_min,coef_max])
ranges.append([offset_min, offset_max])

colony = ant_colony_for_continuous_domains.ACOr()
colony.set_cost(optimization_utilities.define_cost(L, H, Q, Fs))
colony.set_parameters(num_iterations, 5, 50, 0.01, 0.85)
colony.set_variables(ranges)
solution = colony.optimize()
print(solution)