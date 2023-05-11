import numpy as np
import pandas as pd
import bnlearn as bn
import graphviz as gr
import networkx as nx
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures

def create_table(df):

    wrap = lambda s, tag, option="": "<" + tag + " " + option + ">" + s + "</" + tag + ">"
    wrap_list = lambda lst, tag: "".join(map(lambda s: wrap(str(s), tag), lst))

    table = ""

    table += wrap(wrap("group", "th") + 
                  wrap("treatment=0","th","colspan='2'") +
                  wrap("treatment=1","th","colspan='2'"), "tr")



    for group in sorted(df.group.unique()):
        d = df[df.group == group].set_index(["treatment", "recovery"])["count"].to_dict()

        n0 = int(d[(0,0)] + d[(0,1)])
        p0 = d[(0,1)] / n0 if n0 != 0 else 0
        n1 = int(d[(1,0)] + d[(1,1)])
        p1 = d[(1,1)] / n1 if n1 != 0 else 0
        
        f0 = "{}/{}".format(int(d[(0,1)]), n0) 
        f1 = "{}/{}".format(int(d[(1,1)]), n1)
        p0s = "{:.2f}".format(p0)
        p1s = "{:.2f}".format(p1) 
        
        if p0 >= p1:
            f0 = wrap(f0, "b")
            p0s = wrap(p0s, "b")
        else:
            f1 = wrap(f1, "b")
            p1s = wrap(p1s, "b")

        table += wrap(wrap_list([group, f0, p0s, f1, p1s], "td"), "tr")

    d = df.groupby(["treatment", "recovery"])["count"].sum().to_dict()

    n0 = int(d[(0,0)] + d[(0,1)])
    p0 = d[(0,1)] / n0 if n0 != 0 else 0
    n1 = int(d[(1,0)] + d[(1,1)])
    p1 = d[(1,1)] / n1 if n1 != 0 else 0

    f0 = "{}/{}".format(int(d[(0,1)]), n0) 
    f1 = "{}/{}".format(int(d[(1,1)]), n1)
    p0s = "{:.2f}".format(p0)
    p1s = "{:.2f}".format(p1) 

    if p0 >= p1:
        f0 = wrap(f0, "b")
        p0s = wrap(p0s, "b")
    else:
        f1 = wrap(f1, "b")
        p1s = wrap(p1s, "b")

    table += wrap(wrap_list(["total:", f0, p0s, f1, p1s], "td"), "tr")
    table = wrap(table, "table")

    return table





def generate_dataset_0(n_samples=500, set_X=None, show_z=False):
    """
    Generate samples from the CSM:
    Nodes: (X,Y,Z)
    Edges: (Z -> X, Z-> Y, X -> Y)
    
    All variables are binary. 
    
    Designed to generate simpson's paradox.
    
    Args
    ----
    n_samples: int, the number of samples to generate
    
    set_X: array, values to set x

    Returns
    -------
    samples: pandas.DateFrame
    
    """
    p_z = 0.5
    p_x_z = [0.9, 0.1]
    p_y_xz = [0.2, 0.4, 0.6, 0.8]
    
    z = np.random.binomial(n=1, p=p_z, size=n_samples)
    
    if set_X is not None:
        assert(len(set_X) == n_samples)
        x = set_X
    else:
        p_x = np.choose(z, p_x_z)
        x = np.random.binomial(n=1, p=p_x, size=n_samples)
        
    p_y = np.choose(x+2*z, p_y_xz)
    y = np.random.binomial(n=1, p=p_y, size=n_samples)
    
    if show_z:
        return pd.DataFrame({"x":x, "y":y, "z":z})
    
    return pd.DataFrame({"x":x, "y":y})


def generate_dataset_1(n_samples=500, set_X=None):
    """
    Generate samples from the CSM:
    Nodes: (X,Y,Z)
    Edges: (Z -> X, Z-> Y, X -> Y)
    
    X is binary, Z and Y are continuous. 
    
    Args
    ----
    n_samples: int, the number of samples to generate
    
    set_X: array, values to set x
                
    Returns
    -------
    samples: pandas.DateFrame
    
    """
   
    z = np.random.uniform(size=n_samples)
    
    if set_X is not None:
        assert(len(set_X) == n_samples)
        x = set_X
    else:
        p_x = np.minimum(np.maximum(z,0.1), 0.9)
        x = np.random.binomial(n=1, p=p_x, size=n_samples)
        
    y0 = 2 * z
    y1 = y0 - 0.5

    y = np.where(x == 0, y0, y1) + 0.3 * np.random.normal(size=n_samples)
        
    return pd.DataFrame({"x":x, "y":y, "z":z})



def generate_dataset_2(n_samples=500, set_X=None):
    """
    Generate samples from the CSM:
    Nodes: (X,Y,Z)
    Edges: (Z -> X, Z-> Y, X -> Y)
    
    X is binary, Z and Y are continuous. 
    
    Args
    ----
    n_samples: int, the number of samples to generate
    
    set_X: array, values to set x
                
    Returns
    -------
    samples: pandas.DateFrame
    
    """
   
    z = np.random.uniform(size=n_samples)
    
    if set_X is not None:
        assert(len(set_X) == n_samples)
        x = set_X
    else:
        p_x = np.minimum(np.maximum(z,0.1), 0.8)
        x = np.random.binomial(n=1, p=p_x, size=n_samples)
        
    y0 =  2 * z
    y1 =  np.where(z < 0.2, 3, y0)

    y = np.where(x == 0, y0, y1) + 0.3 * np.random.normal(size=n_samples)
        
    return pd.DataFrame({"x":x, "y":y, "z":z})


def generate_dataset_3(n_samples=500, set_X=None):
    """
    Generate samples from the CSM:
    Nodes: (X,Y,Z)
    Edges: (Z -> X, Z-> Y, X -> Y)
    
    X is binary, Z and Y are continuous. 
    
    Args
    ----
    n_samples: int, the number of samples to generate
    
    set_X: array, values to set x
                
    Returns
    -------
    samples: pandas.DateFrame
    
    """
   
    z = np.random.uniform(size=n_samples)
    
    if set_X is not None:
        assert(len(set_X) == n_samples)
        x = set_X
    else:
        p_x = np.where(z < 0.3, 0, np.where(z > 0.7, 1, 0.7))
        x = np.random.binomial(n=1, p=p_x, size=n_samples)
        
    y0 =  np.where(z >= 0.4, -4*(z - 0.4), 0)
    y1 =  np.where(z < 0.6,  -4*(z - 0.6), 0) + 1

    y = np.where(x == 0, y0, y1) + 0.3 * np.random.normal(size=n_samples)
        
    return pd.DataFrame({"x":x, "y":y, "z":z})


def generate_exercise_dataset_0(n_samples=500, set_X=None):
    """
    Generate samples from the CSM:
    Nodes: (X,Y,Z)
    Edges: (Z -> X, Z-> Y, X -> Y)
    
    X is binary, Z and Y are continuous. 
    
    Args
    ----
    n_samples: int, the number of samples to generate
    
    set_X: array, values to set x
                
    Returns
    -------
    samples: pandas.DateFrame
    
    """
   
    z = np.random.normal(size=(n_samples, 5))
    beta_treatment = np.array([0,1,2,0,0])
    beta_effect = np.array([1,1,2,0,0])
    
    if set_X is not None:
        assert(len(set_X) == n_samples)
        x = set_X
    else:
        p_x = _sigma(np.dot(z, beta_treatment))
        x = np.random.binomial(n=1, p=p_x, size=n_samples)
        
    y0 = np.dot(z, beta_effect)
    y1 = np.dot(z, beta_effect) + 1

    y = np.where(x == 0, y0, y1) + 0.3 * np.random.normal(size=n_samples)
        
    df = pd.DataFrame({"x":x, "y":y})
    
    for i in range(z.shape[1]):
        df["z_{}".format(i)] = z[:, i]

    return df


def generate_exercise_dataset_1(n_samples=500, set_X=None):
    """
    Generate samples from the CSM:
    Nodes: (X,Y,Z)
    Edges: (Z -> X, Z-> Y, X -> Y)
    
    X is binary, Z and Y are continuous. 
    
    Args
    ----
    n_samples: int, the number of samples to generate
    
    set_X: array, values to set x
                
    Returns
    -------
    samples: pandas.DateFrame
    
    """
   
    z = np.random.normal(size=(n_samples, 5))
    beta_treatment = np.array([-1,-1,-2,0,0])
    beta_effect = np.array([-1,-1,-2,0, 0.5])

    p_x = _sigma(np.dot(z, beta_treatment))
    
    if set_X is not None:
        assert(len(set_X) == n_samples)
        x = set_X
    else:
        x = np.random.binomial(n=1, p=p_x, size=n_samples)
        
    y0 = np.dot(z, beta_effect)
    y1 = np.dot(z, beta_effect) * (1 + p_x)

    y = np.where(x == 0, y0, y1) + 0.3 * np.random.normal(size=n_samples)
        
    df = pd.DataFrame({"x":x, "y":y})
    
    for i in range(z.shape[1]):
        df["z_{}".format(i)] = z[:, i]

    return df



def generate_exercise_dataset_2(n_samples=500, set_X=None):
    """
    Generate samples from the CSM:
    Nodes: (X,Y,Z)
    Edges: (Z -> X, Z-> Y, X -> Y)
    
    X is binary, Z and Y are continuous. 
    
    Args
    ----
    n_samples: int, the number of samples to generate
    
    set_X: array, values to set x
                
    Returns
    -------
    samples: pandas.DateFrame
    
    """
    beta_treatment = np.array([ 0.15207176, -0.11653175, -0.34068517,  0.64009405, -0.7243722 ,
       -2.7122607 ,  2.3021001 ,  0.04638091,  1.4096595 , -0.88538833,
       -1.27773486,  1.59597409, -1.27020399,  2.07570976,  0.99324477,
       -0.53702672, -0.10555752,  1.45058372, -1.80245312, -1.92714373,
        1.65904829])
    beta_effect_y0 = np.array([ 0.33313179, -0.04529036,  0.0294476 , -1.57207538, -0.00679557,
        0.87759851, -1.78974391, -0.78558499, -1.50506646, -0.17133791,
        0.7489653 , -0.74583104,  0.79613557, -0.28718545, -1.194678  ,
        0.3952664 , -0.32922775,  0.57037979,  1.19875008,  0.89582566,
       -1.34180865])
    beta_effect_y1 = np.array([-0.8001777 ,  1.16531638, -0.82150055, -0.27853936,  1.74561238,
        0.50031182, -1.74396855, -0.86928906,  0.26423181,  0.01572352,
        1.22709648, -0.08222703, -0.91403023,  0.05014785, -1.34730904,
        0.01790165, -0.60325542,  0.47473682,  0.40199847,  0.49554447,
       -0.13907751])
    
    Z = np.random.normal(size=(n_samples, 5))
    Z2 = PolynomialFeatures().fit_transform(Z)
        
    if set_X is not None:
        assert(len(set_X) == n_samples)
        x = set_X
    else:
        p_x = _sigma(np.dot(Z2, beta_treatment))
        x = np.random.binomial(n=1, p=p_x, size=n_samples)
        
    y0 = np.dot(Z2, beta_effect_y0)
    y1 = np.dot(Z2, beta_effect_y1) + 5
    
    y = np.where(x == 0, y0, y1) + np.random.normal(size=n_samples)
        
    df =  pd.DataFrame({"x":x, "y":y})
    
    for i in range(Z.shape[1]):
        df["z_{}".format(i)] = Z[:, i]
        
    return df



def _sigma(x):
    return 1 / (1 + np.exp(-x))




""" Generate a pandas DataFrame sampled from the 'dyspnoea' dataset """
def generate_dyspnoea_dataset():
    """ Generates the dyspnea dataset. It load the data from https://www.bnlearn.com/bnrepository/
    but it dropes the 'either' node, which is confusing 
    """
    # Original dataset. We are not using that
    # DAG = bn.import_DAG('asia')
    
    # Define the network structure
    edges = [('asia', 'tub'),
             ('tub', 'dysp'),
             ('tub', 'xray'),
              ('lung', 'xray'),
              ('lung', 'dysp'),
              ('smoke', 'lung'),
              ('smoke', 'bronc'),
              ('bronc', 'dysp')]
    
    DAG = bn.make_DAG(edges)
    df = bn.import_example('asia')
    DAG = bn.parameter_learning.fit(DAG, df, methodtype='bayes', verbose = 0)
    df = bn.sampling(DAG, n=20000)
    
    df = df.rename(columns = {'asia' : 'tuberculosis_area', 
                                'tub' : 'tuberculosis', 
                                'lung' : 'lung_cancer',
                                'bronc' : 'bronchitis',
                                'dysp' : 'dyspnea'})
        
    return df



# %% PLOT functions

def plot_from_edges(edges):
    """ 'edges' is a Python list describing the directions of arrows  
    """
    g = gr.Digraph()
    for i in range(0, len(edges)):
        g.edge(*edges[i])
    return g


def plot_dyspnoea_dataset(mode = "graphviz"):
    # plot ground truth using bnlearn
    # plt.figure();
    # params_static = {
    #     'layout' : 'graphvix_layout'
    #     }   
    
    # G = bn.plot(DAG, node_color='red', node_size=5000, params_static = params_static)

    # plot using nx
    # plt.figure();
    
    edges = [('tuberculosis_area', 'tuberculosis'),
             ('tuberculosis', 'dyspnea'),
             ('tuberculosis', 'xray'),
              ('lung_cancer', 'xray'),
              ('lung_cancer', 'dyspnea'),
              ('smoke', 'lung_cancer'),
              ('smoke', 'bronchitis'),
              ('bronchitis', 'dyspnea')]
    
    if mode == "networkx":
        DAG = bn.make_DAG(edges)
        graph = nx.DiGraph(DAG['adjmat'])
        pos = nx.nx_agraph.graphviz_layout(graph, prog="neato")
        options = {
            'node_color': 'red',
            'node_size': 1000,
            'width': 1,
            'arrowstyle': '-|>',
            'arrowsize': 12,
            }
        nx.draw(graph, pos, with_labels=True, **options)
    
    elif mode == "graphviz":
        g =  plot_from_edges(edges)
        return g



def plot_from_model_bnlearn(model):
    # plot
    g = gr.Digraph()
    
    for i in range(0, len(model['model_edges'])):
        g.edge(*model['model_edges'][i])
    return g


def plot_from_model_pgmpy(edges):
    # plot
    edges = [el for el in edges] #unpack
    g = gr.Digraph()
    
    for i in range(0, len(edges)):
        g.edge(edges[i][0],edges[i][1])
    return g