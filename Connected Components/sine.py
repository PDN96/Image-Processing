from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi

t = arange(-1.0, 1.0, 0.01)

fig = figure(1)

a = 1
f = 1
th = 0
ax1 = fig.add_subplot(221)
ax1.plot(t, sin(2*pi*f*t + th))
ax1.grid(True)
ax1.set_ylim((-2, 2))
ax1.set_ylabel('y(t)')
ax1.set_xlabel('t')
ax1.set_title('a = 1, f = 1, th = 0')

a = 2
f = 1
th = 0
ax2 = fig.add_subplot(222)
ax2.plot(t, sin(2*pi*f*t + th))
ax2.grid(True)
ax2.set_ylim((-1.25, 1.25))
ax2.set_ylabel('y(t)')
ax2.set_xlabel('t')
ax2.set_title('a = 2, f = 1, th = 0')

a = 1
f = 2
th = 0
ax3 = fig.add_subplot(223)
ax3.plot(t, sin(2*pi*f*t + th))
ax3.grid(True)
ax3.set_ylim((-1.25, 1.25))
ax3.set_ylabel('y(t)')
ax3.set_xlabel('t')
ax3.set_title('a = 2, f = 1, th = 0')

a = 1
f = 1
th = pi/2
ax4 = fig.add_subplot(224)
ax4.plot(t, sin(2*pi*f*t + th))
ax4.grid(True)
ax4.set_ylim((-1.25, 1.25))
ax4.set_ylabel('y(t)')
ax4.set_xlabel('t')
ax4.set_title('a = 1, f = 1, th = pi/2')

show()