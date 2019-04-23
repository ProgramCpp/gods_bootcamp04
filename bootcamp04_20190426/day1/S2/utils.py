
from sklearn import datasets
import pandas as pd
import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import plotly

def get_boston_data(): 
    raw = datasets.load_boston()
    df = pd.DataFrame(raw['data'],columns=raw['feature_names'])
    df['target'] = raw['target']
    return df




def get_ligreg_interactive(X,y):
    '''
    get_linreg_interactive(X,y)
    X: variable on x-axis 
    y: variable on y-axis 

    y = a+bX
    '''
    [b_est,a_est] = np.polyfit(X,y,1)

    b_min = b_est-.2*np.abs(b_est); b_max = b_est+.2*np.abs(b_est);
    a_min = a_est-.2*np.abs(a_est); a_max = a_est+.2*np.abs(a_est); 

    b = widgets.FloatSlider(description='b',min=b_min,max=b_max,step=.2*np.abs(b_est)/6)
    a = widgets.FloatSlider(description='a',min=a_min,max=a_max,step=.2*np.abs(a_est)/6)
    e = widgets.FloatText(description='error')

    def plotme(a , b ):
        fig = plt.figure(figsize=(10,6))
        x_min = np.min(X); x_max = np.max(X);
        x_min_ = x_min - .1*np.abs(x_min); x_max_ = x_max + .1*np.abs(x_max)
        x = np.array([x_min_,x_max_])
        err = np.mean((y-(a+b*X))**2)
        e.value = err 
        plt.plot(x, a+b * x )
        plt.scatter(X,y,c='r')
        plt.ylim(0, 1.1*np.max(y))
        plt.xlim(0,1.1*np.max(X))
        plt.show()

    out = widgets.VBox([widgets.VBox([a, b,e]), widgets.interactive_output(plotme, {'b': b, 'a': a})])

    return out


def plot_surface(x,y,z):
    '''
    Plot a surface based using xyz-coordinates as inputs
    
    x,y,z are in 2x2 arrays format
    
    requirements: 
        - plotly 
        - numpy
    '''
    
    trace = plotly.graph_objs.Surface(x=x,y=y,z=z)

    plotly.offline.init_notebook_mode()
    
    layout = plotly.graph_objs.Layout(
    autosize=False,
    width=800,
    height=600
    )

    fig = plotly.graph_objs.Figure(data = [trace],layout = layout)
    plotly.offline.iplot(fig)

    
def test_plot_surface(): 
    nobs = 100
    a = 2; b = 3; std = 1

    x = np.random.normal(size=nobs)
    err = np.random.normal(size=nobs)*std

    y = a + b*x + err 

    f = lambda a,b: np.mean( (a+b*x - y)**2 )
    # plt.plot(x,y,'o')

    A = np.linspace(0,4,20)
    B = np.linspace(0,5,20)
    aa,bb = np.meshgrid(A,B)
    zz = np.vectorize(f)(aa,bb)/10

    plot_surface(aa,bb,zz)

