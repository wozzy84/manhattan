import matplotlib.pyplot as plt
import numpy as np

XS_LN = np.linspace(0.001, 9, 256, endpoint=False)
XS_EXP = np.linspace(-8, 2, 256, endpoint=True)
YS_LN, YS_EXP = np.log(XS_LN), np.exp(XS_EXP)
plt.figure(figsize=(15, 15), dpi=80)

plt.plot(XS_EXP, YS_EXP, color='blue', linewidth=3, linestyle='-', label=r'$e^{x}$')
plt.plot(XS_LN, YS_LN, color='red', linewidth=3, linestyle='-', label=r'$ln(x)$')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.xticks(np.arange(-8, 8, 1))
plt.yticks(np.arange(-7, 8, 1))

plt.legend(loc=2, prop={'size': 25})
plt.show()
