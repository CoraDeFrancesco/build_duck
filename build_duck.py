#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:44:28 2022

@author: user1
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from svgpathtools import svg2paths
from svgpath2mpl import parse_path

duck_path, attributes = svg2paths('rubber_duck.svg')
duck_marker = parse_path(attributes[0]['d'])
duck_marker.vertices -= duck_marker.vertices.mean(axis=0)

duck_marker = duck_marker.transformed(mpl.transforms.Affine2D().scale(-1,1))

x = np.arange(0.0, 50.0, 2.0)
y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
s = np.random.rand(*x.shape) * 800 + 500

plt.plot(x, y, "bo", alpha=0.5, marker=duck_marker, markersize=26)
plt.xlabel("Corn")
plt.ylabel("Ducks")
plt.show()