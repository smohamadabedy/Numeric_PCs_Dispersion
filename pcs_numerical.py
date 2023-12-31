# -*- coding: utf-8 -*-
"""PCs Numerical.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H5AzBJSPMi0Zc_0S2xA2utTPuYdjX5n5

![download.png](data:image/png;base64,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qqvU29sbs7y3t1eVlZWO61RWVnpqP5Glc/ziTZ48Wbfeeqs+/vjjTHRxQnE798rKynT11Vcb6lV+W7x4ccGfexs3btTevXv13nvvqaqqKmFbvv9G83L84hX695/P59PcuXO1aNEitba2asGCBXruuecc22by3DMeRnw+nxYtWqQDBw5Elw0NDenAgQOu163q6+tj2kvS/v37XdtPZOkcv3iDg4M6efKkpk+fnqluThice+Ovo6OjYM89y7K0ceNG7dq1S++++67mzJmTdB3OwRHpHL94fP/FGhoaUjgcdvwso+femKfAjoOdO3dafr/famtrs373u99Zf/d3f2d9+9vftnp6eizLsqwHHnjA2rx5c7T9b37zG2vSpEnWv/zLv1i///3vrS1btliTJ0+2Tp48aepXMMrr8XviiSest99+2zp79qx17Ngx62//9m+tkpIS66OPPjL1KxjT19dnnThxwjpx4oQlyfr5z39unThxwurs7LQsy7I2b95sPfDAA9H2f/zjH61vfetb1o9+9CPr97//vbV161brqquust566y1Tv4JRXo/fM888Y+3evdv6n//5H+vkyZPWo48+ahUXF1vvvPOOqV/BqEceecQKBALWwYMHre7u7ujrf//3f6Nt+P5zl87x4/tvxObNm61Dhw5Z586ds/77v//b2rx5s1VUVGT9+te/tiwru+deToQRy7Ksf/3Xf7VmzZpl+Xw+a/HixdYHH3wQ/WzZsmXWunXrYtr/8pe/tK6//nrL5/NZN910k/XGG29kuce5xcvx27RpU7RtRUWF9Zd/+ZfW8ePHDfTavMitpvGvyPFat26dtWzZslHrLFy40PL5fNaf/dmfWS+//HLW+50rvB6/f/7nf7Zqa2utkpISa8qUKdby5cutd99910znc4DTsZMUc07x/ecunePH99+I73//+1ZNTY3l8/msadOmWX/xF38RDSKWld1zr8iyLGvs4ysAAADpMT5nBAAAFDbCCAAAMIowAgAAjCKMAAAAowgjAADAKMIIAAAwijACAACMIowAAACjCCMAAMAowggAADCKMAIAAIwijAAAAKP+f+0uabsk+4rUAAAAAElFTkSuQmCC)


---


# 1D PHONONIC CRYSTAL NUMERICAL SOLVER#
A comprehensive toolkit to explore phononic behaviors in metamaterials. Analyze time and spatial profiles, perform FFT, generate animations, and derive numerical dispersion curves
"""

import numpy as np
from scipy.integrate import solve_ivp
import time
import math
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from IPython.display import HTML
from IPython.display import clear_output, display
from numpy import exp,abs,abs,cos,sin,tan,exp,sinh,cosh,tanh,floor,ceil,exp,log10,log2,log
import json
from google.colab import files
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default = 'colab'
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from numpy import savetxt
import pandas as pd

"""In the next section, modify the spring relation and damping model according to your preferences. Please note that 'Fomega' represents the linear frequency and **should not be altered**"""

# Important functions for the program
# just change Spring and damping functions

def fomega(Wavenumber):
    """
    Calculates the linear frequency based on the given wavenumber.

    Args:
    - Wavenumber: Wavenumber

    Returns:
    - Linear frequency
    """
    return np.sqrt(2 - 2 * np.cos(Wavenumber))

def springModel(x1, x2, t, element):
    """
    Calculates the displacement relation (F_u) based on the given inputs.

    Args:
    - x1: Displacement at point 1
    - x2: Displacement at point 2
    - t: Time parameter
    - element: Element parameter (if used)

    Returns:
    - Displacement relation (F_u)
    """
    x = x1 - x2  # Calculate displacement
    return x  # Return the displacement relation
    # Uncomment and modify below lines for alternative calculations
    # return x + 0.001 * np.abs(x)
    # return np.exp(-1 * x) * (1 - np.exp(-1 * x))

def dampingModel(x1, x2, x1_dot, x2_dot, t, element):
    """
    Calculates the damping relation (F_udot_u) based on the given inputs.

    Args:
    - x1: Displacement at point 1
    - x2: Displacement at point 2
    - x1_dot: Velocity at point 1
    - x2_dot: Velocity at point 2
    - t: Time parameter
    - element: Element parameter (if used)

    Returns:
    - Velocity relation (F_udot_u)
    """
    return 0  # No damping effect considered in this implementation; always returns 0
    # You can add damping calculations here if required

def setInitialCondition(node,wave_number,amplitude):
  """
    Sets the initial conditions for the system based on wave number and amplitude.

    Args:
    - wave_number: Wavenumber used to set initial conditions
    - amplitude: Amplitude used to set initial conditions

    Returns:
    - Initial conditions array
    """
  init            = np.zeros((node*2));
  for i in range(0,node,1):
    init[2*i]     = amplitude*np.cos(wave_number*i);
    init[2*i+1]   = amplitude*np.sin(wave_number*i)*fomega(wave_number);
  return init;

"""This is the core class of the program. Edit only if you know what you're doing"""

class numericalPCs:

  def __init__(self,node = 100,initial_condition = np.zeros((100*2)),time_step = 50,time_end = 300):
    # number of masses
    self.node      = node;
    # Set the initial condition (including wave number and amplitude)
    self.init      = initial_condition;
    # Set the time span for the simulation; these values facilitate our study for FFT
    self.sr        = time_step;
    self.ts        = 1.0/sr;
    self.time_end  = time_end;
    self.timing    = np.arange(0,time_end,self.ts);

  #Main function solving the dynamics using Runge-Kutta
  def run(self):
    sol = solve_ivp(self.oneDimSys, [0, self.time_end],self.init, args=(self.node,2),t_eval=self.timing);
    self.results          = sol.y;
    self.transposed_data  = np.transpose(sol.y)
    return self;

  # the Great function of numerical Dispersion :)
  def DISPERSION(self,amplitude = 1,wave_numbers = np.arange(0,np.pi,.1)):
    iter      = 0;
    for k in wave_numbers:

      # First, set initial conditions with respect to wave number and amplitude
      init = setInitialCondition(node = node,wave_number = k ,amplitude = amplitude)
      # solve
      sol = solve_ivp(self.oneDimSys, [0, self.time_end],init, args=(self.node,2),t_eval=self.timing);
      transposed_data = np.transpose(sol.y);
      overHistory     = transposed_data[0:,self.node];
      # Perform FFT
      freq1,fin_Y1    = PC.FFrRaw(overHistory,self.sr);
      pos             = np.where(freq1<3.2)
      # Store the data properly
      print("Currently at : ",k)
      if(iter > 0):
          MainData[:,iter] = fin_Y1[pos[0]]
          plt.plot(MainData[:,iter])
          df.insert(iter+1, k, fin_Y1[pos[0]], True)
      else:
          df = pd.DataFrame({'x':freq1[pos[0]]})
          f1 = freq1[pos[0]];
          MainData = np.zeros((f1.shape[0],wave_numbers.shape[0]))
          MainData[:,iter] = fin_Y1[pos[0]]
          plt.plot(MainData[:,iter])
          df.insert(iter+1, k, fin_Y1[pos[0]], True)
      iter = iter+1
    # Plot the dispersion curve
    [X,Y] = np.meshgrid(f1.T,wave_numbers)
    fig   = plt.figure()
    ax    = fig.subplots()
    ax.contourf(Y,X,MainData.T)
    self.dipersionData = MainData
    return self

  # State-space
  def oneDimSys(self,t,z,node,data):
    dy = np.zeros((node*2));
    dy[0] = z[1];
    dy[1] = (-springModel(z[0],0,t,0))+ (-dampingModel(z[0],0,z[1],0,t,0)) -springModel(z[0],z[2],t,1)+  (-dampingModel(z[0],z[2],z[1],z[3],t,1)) ;
    j_iter = -1;
    for i in np.arange(3,(node*2) -1,2):
          dy[i-1] = z[i];
          dy[i] = (-springModel(z[i-1],z[i-3],t,2+j_iter)  -springModel(z[i-1],z[i+1],t,3+j_iter)  +  (-dampingModel(z[i-1],z[i-3],z[i],z[i-2],t,2+j_iter))+ (-dampingModel(z[i-1],z[i+1],z[i],z[i+2],t,2+j_iter))   )
          j_iter=j_iter+1;
          # Sometimes, we need to apply specific or special conditions
          # if(j_iter == (node/2) + 1 ):
          #    dy[i] = dy[i]*1e3
    dy[node*2-2] = z[node*2-1];
    dy[node*2-1] = (-springModel(z[node*2-2],z[node*2-4],t,node-1) + (-dampingModel(z[node*2-2],z[node*2-4],z[node*2-1],z[node*2-3],t,2+j_iter)))
    return dy

  # Animating function
  def plot_anim(self,data,node,time_sample,frames):
    x       = data[:,0:2*node:2];
    fig, ax = plt.subplots()
    def update(frame):
      ax.cla()
      if(frame == 0 ):
        cf = 0
      else:
        cf = int(np.floor(time_sample/frames)*(frame)) - 1
      contours = ax.plot(np.arange(0,node,1),x[cf,:])
    self.ani = animation.FuncAnimation(fig, update, frames=frames, interval=200)
    return self.ani;


  # FFT & Plotting
  def FFT(self,x,sr):
    freq,fin_Y = self.FFrRaw(x,sr)
    fig        = go.Figure(data=go.Scatter(x=freq, y=fin_Y, mode='lines'))
    fig.update_layout(title='Line Plot',xaxis_title='',yaxis_title='FFt',)
    fig.show()
    return fig,freq,fin_Y

  # FFT calculation
  def FFrRaw(self,x,sr):
    X     = fft(x)
    N     = len(X)
    n     = np.arange(N)
    T     = N/sr
    freq  = (n/T)*2*np.pi;
    fin_Y = np.abs(X)

    return freq,fin_Y

  # Animation generation
  def animate(self,frame = 300):
    anim = self.plot_anim(self.transposed_data,self.node,self.timing.shape[0],frame);
    return anim

  # Plot displacements
  def plotDetails(self):
    sr        = self.sr;
    ts        = self.ts;
    time_end  = self.time_end;
    t         = self.timing;
    node      = self.node;

    x     = self.transposed_data[:,0:node*2:2];
    X     = np.arange(0, node, 1)
    Y     = t/1000
    X, Y  = np.meshgrid(X, Y)

    fig   = plt.figure(figsize=(15, 10))
    gs    = fig.add_gridspec(2, 6)

    ax    = fig.add_subplot(gs[0, 0:3], projection='3d')
    surf  = ax.plot_surface(X, Y, x, cmap=cm.summer,linewidth=0);

    ax.view_init(azim=25, elev=30);
    ax.set_xlabel("Non-dimensional time (T1)")
    ax.set_ylabel("Mass number")
    ax.set_zlabel("Relative Displacment")
    ax.zaxis.labelpad=-0.7

    ax2 = fig.add_subplot(gs[0, 3:7])
    ax2.plot(t/100,x);
    ax2.set_xlabel("Non-dimensional time (T1)")
    ax2.set_ylabel("Relative Displacment")

    ax3 = fig.add_subplot(gs[1,:], projection='3d')
    for i in np.arange(1,node,20):
      ax3.plot3D(np.tile(np.array([i]), t.shape[0]), t/100, x[:,i])
    ax3.view_init(azim=45, elev=50);

    return self

  # Plots the spatial profile for a specific timestep.
  def spatialProfile(self,timestep = 1,figsize=(10,4)):
    overSpatial     = self.transposed_data[timestep,0:2*self.node:2];
    plt.figure(figsize=figsize);
    plt.plot(np.arange(0,self.node)+1,overSpatial);
    return self

  # Plots the history profile for a specific node.
  def historyProfile(self,node = 1,figsize=(10,4)):
    overHistory     = self.transposed_data[:,node];
    plt.figure(figsize=figsize);
    plt.plot(self.timing,overHistory);
    return self

  # Performs FFT (Fast Fourier Transform) on spatial data for a specific timestamp.
  def SpatialFFt(self,timestamp = 1):
    overspatial       = self.transposed_data[timestamp,0:node*2:2];
    fig1,freq1,fin_Y1 = self.FFT(overspatial,sr);
    return self

  # Performs FFT (Fast Fourier Transform) on time history data for a specific node.
  def historyFFt(self,node = 1):
    overHistory       = self.transposed_data[:,node];
    fig1,freq1,fin_Y1 = self.FFT(overHistory,sr);
    return self

"""#Implementation

We'll begin utilizing our 'numericalPCs' class.
"""

node        = 100 # @param {type:"slider", min:50, max:1000, step:1}
time_end    = 200 # @param {type: "number"}
sr          = 10 # @param {type: "slider", min: 10, max: 1000, step:1}
###############################################
# Write code manually for initial conditions
# If you encounter the variable 'k' anywhere, it represents the wave number
wave_number       = 2 # @param {type: "number"}
amplitude         = 5 # @param {type: "number"}
init              = np.zeros((node*2));
for i in range(0,node,1):
  init[2*i]       = amplitude*np.cos(wave_number*i);
  init[2*i+1]     = amplitude*np.sin(wave_number*i)*fomega(wave_number);
# or use the helper
# init = setInitialCondition(node = node,wave_number = wave_number ,amplitude = amplitude)
###############################################

# Initializing the class
PC = numericalPCs(node = node,initial_condition = init,time_step = sr,time_end = time_end)

"""In the upcoming section, we'll solve the system's dynamics and proceed to analyze both its historical and spatial profiles"""

# Running the simulation for a specific initial condition
PC.run();

# Obtaining displacement for each mass (node) and nondimensional time
PC.plotDetails();

# Animating the profile for better perception
anim = PC.animate(frame=100);
HTML(anim.to_html5_video())

# or save
# Writer = animation.FFMpegWriter(fps=10)
# anim.save('animation.mp4', writer=Writer)

# Ploting spatial profile
PC.spatialProfile(timestep=100,figsize=(5,2))

# Ploting spatial profile
PC.historyProfile(node=100,figsize=(5,2));

# FFT over time history and spatial profile
PC.historyFFt(node = 50);
# Note: You need to manually scale the Wave-number FFT with respect to the Brillouin zone
PC.SpatialFFt(timestamp = 50);

# Easily modify the problem's conditions and rerun the program
node         = 1000;
k            = 3;
amp          = 1;
PC.node      = node;
PC.init      = setInitialCondition(node = node,wave_number = k ,amplitude = amp);

PC.run().spatialProfile(timestep=100).SpatialFFt(timestamp = 100).historyFFt(node = 100);

"""# Dispersion Curve"""

## AND FINNALY, THE DISPERSION CURVE
## YOU DONT NEED to EXECUTE PC.RUN() IF ONLY WANT THE DISPERSION
PC.DISPERSION(amplitude = 1,wave_numbers = np.arange(0,np.pi,.1))

