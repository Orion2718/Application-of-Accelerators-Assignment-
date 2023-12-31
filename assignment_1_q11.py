# -*- coding: utf-8 -*-
"""Assignment_1-Q11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RncfHBCezUYMoV-qhtlpI89MJXuzjHRC

\\
Q11 - [2 point] Warmup computational exersize: *Create a GitHUB account.*

Write a function in Python code that multiples 2 (two) 3x3 Matrices (ndarray) and returns the result.

    Call this function using two randomly generated 3 by 3 matrices and print the results.\\
    Place your code in your GitHUB repository and submit the link in your exercise document. The code can also be in the form of a Jupiter-Notebook on your GitHUB account.

Hint: if you have no previous experience with python: it is easy! Hint: if you don't have time to learn python: it doesn't take time!

Python code in GitHub, links for the:
"""

import random
import numpy as np

def RandMat():
  M = np.random.randint(low=0, high=9, size=(3, 3))
  print(M,"\n")
  return M

M1 = RandMat()
M2 = RandMat()
ma=np.dot(M1,M2)
print(ma)

# Alternative code I made (Just an extra)


import numpy as np

def RandMat():
  M = np.random.randint(low=0, high=50, size=(3, 3))
  print(M,"\n")
  return M

ma = np.dot(RandMat(),RandMat())
print(ma)