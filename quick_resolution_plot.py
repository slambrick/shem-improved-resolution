# -*- coding: utf-8 -*-
"""
Sam Lambrick

Creates a simple plot demonstrating the depth of field of the Cambridge and Portland type SHeM.
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 7})

x = np.arange(0, 1000, 0.1)
y_Cambridge = 470/np.sqrt(2) + 0.668*x
y_Portland = 200 + 2*x


f, ax = plt.subplots(figsize = (2.25,1.5))
ax.plot(x/1000, y_Cambridge/1000, color = '#2aa198', label='Cambridge')
ax.plot(x/1000, y_Portland/1000, color = '#cb4b16', label='Portland')
ax.set_xlabel('$f$')
ax.set_ylabel('FWHM')
ax.grid
ax.set_yticks(np.arange(0, 2.1, 0.5))
ax.set_ylim(0, 2)
ax.set_xlim(0, 1)
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig('resolution_WD.pdf')