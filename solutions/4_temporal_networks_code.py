#%% In [1]
import pathpy as pp

t = pp.TemporalNetwork()
print(t)

#%% In [2]
t.add_edge('a', 'b', 1)
t.add_edge('b', 'a', 3)
t.add_edge('b', 'c', 3)
t.add_edge('d', 'c', 4)
t.add_edge('c', 'd', 5)
t.add_edge('c', 'b', 6)
print(t)

#%% In [3]
t_realtime = pp.TemporalNetwork()
t_realtime.add_edge('a', 'b', '2018-08-22 09:30:22')
t_realtime.add_edge('b', 'c', '2018-08-22 09:30:25')
t_realtime.add_edge('c', 'a', '2018-08-22 10:30:25')
print(t_realtime)

for e in t_realtime.tedges:
    print(e)

#%% In [4]
t

#%% In [6]
style = {    
    'ts_per_frame': 1, 
    'ms_per_frame': 2000,
    'look_ahead': 2, 
    'look_behind': 2, 
    'node_size': 15, 
    'inactive_edge_width': 2,
    'active_edge_width': 4, 
    'label_color' : '#ffffff',
    'label_size' : '24px',
    'label_offset': [0,5]
    }
pp.visualisation.plot(t, **style)

#%% In [7]
pp.visualisation.export_html(t, 'visualisations/4_temporal_network.html', **style)

#%% In [8]
causal_paths = pp.path_extraction.temporal_paths.paths_from_temporal_network_dag(t, delta=1)
print(causal_paths)

for l in causal_paths.paths:
    for p in causal_paths.paths[l]:
        if causal_paths.paths[l][p][1]>0:
            print('{0} -> {1}'.format(p, causal_paths.paths[l][p][1]))

#%% In [9]
causal_paths = pp.path_extraction.paths_from_temporal_network_dag(t, delta=2)
print(causal_paths)

for l in causal_paths.paths:
    for p in causal_paths.paths[l]:
        if causal_paths.paths[l][p][1]>0:
            print('{0} -> {1}'.format(p, causal_paths.paths[l][p][1]))

#%% In [10]
dag, node_map = pp.DAG.from_temporal_network(t, delta=2)

color_map = {'a': 'red',
             'b': 'green',
             'c': 'blue',
             'd': 'red'}

style = { 
    'width': 400, 
    'height': 300, 
    'node_color': { v: color_map[node_map[v]] for v in dag.nodes }, 
    'node_size': { v: 8 if v in dag.roots else 5 for v in dag.nodes }
}

pp.visualisation.plot(dag, **style)

#%% In [11]
import sqlite3
con = sqlite3.connect('data/temporal_networks.db')
con.row_factory = sqlite3.Row

#%% In [12]
t_ho = pp.TemporalNetwork.from_sqlite(con.execute('SELECT source, target, time FROM sociopatterns_hospital'),
                                      directed=False)
print(t_ho)

#%% In [13]
t_ho = pp.TemporalNetwork.from_sqlite(con.execute('SELECT source, target, time FROM sociopatterns_hospital'),
                                      directed=False, time_rescale=20)
print(t_ho)

#%% In [14]
causal_paths = pp.path_extraction.paths_from_temporal_network_dag(t_ho, delta=3)
print(causal_paths)

#%% In [15]
causal_paths = pp.path_extraction.sample_paths_from_temporal_network_dag(t_ho, delta=3, num_roots=50)
print(causal_paths)

#%% In [16]
t = pp.TemporalNetwork.read_file('data/temporal_clusters.tedges')
style = {
    'max_time': 250,
    'ms_per_frame': 10,
    'ts_per_frame': 1
}
pp.visualisation.plot(t, **style)

#%% In [17]
walk = pp.algorithms.temporal_walk.generate_walk(t, 500)
style['ms_per_frame'] = 250
pp.visualisation.plot_walk(pp.Network.from_temporal_network(t), walk, **style)

#%% In [18]
p = pp.path_extraction.paths_from_temporal_network_dag(t)
hon_2 = pp.HigherOrderNetwork(p, k=2)

clusters = { v: 'red' if len(v)<2 else ('green' if v.startswith('1') else 'blue') for v in p.nodes}

pp.visualisation.plot(hon_2, plot_higher_order_nodes=False, node_color = clusters)

#%% In [19]
pp.visualisation.plot_walk(hon_2, walk, **style, plot_higher_order_nodes=False)

#%% In [20]
hon_3 = pp.HigherOrderNetwork(p, k=3)
pp.visualisation.plot(hon_3, plot_higher_order_nodes=False, node_color = clusters)

#%% In [21]
print('Second-order model: {0}'.format(pp.algorithms.spectral.algebraic_connectivity(hon_2)))

print('Second-order null model: {0}'.format(pp.algorithms.spectral.algebraic_connectivity(pp.HigherOrderNetwork(p, k=2, null_model=True))))
print('First-order model: {0}'.format(pp.algorithms.spectral.algebraic_connectivity(pp.HigherOrderNetwork(p, k=1))))

#%% In [22]
%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

plt.ylim(-.15, .15)
plt.title('Fiedler vector (second-order model)')
plt.scatter(range(hon_2.ncount()), np.real(pp.algorithms.spectral.fiedler_vector_dense(hon_2)))
plt.show()

plt.title('Fiedler vector (second-order null model)')
plt.ylim(-.15, .15)
plt.scatter(range(hon_2.ncount()), np.real(pp.algorithms.spectral.fiedler_vector_dense(pp.HigherOrderNetwork(p, k=2, null_model=True))))
plt.show()

#%% In [23]
import json

t_lotr = pp.TemporalNetwork.from_sqlite(
    con.execute('SELECT source, target, time FROM lotr'))
print(t)

# Load chapter marks from JSON file
with open('data/lotr_chapters.json', 'r') as f:
    chapters = json.load(f)

# Load character classes from JSON file
with open('data/lotr_characters.json', 'r') as f:
    characters = json.load(f)

style = {
    # some default parameters
    'width': 1200,
    'height': 1000,
    'look_ahead': 500,
    'look_behind': 1500,
    'ts_per_frame': 20, 
    'ms_per_frame': 50,
    'inactive_edge_width': 4.0,
    'active_edge_width': 6.0,
    'label_offset': [0,-16],    
    'node_size': 10,
    'label_size': '14px',
    
     # tell pathpy to use a user-provided custom template
    'template': 'data/custom_template.html',
    
    # add custom parameters defined in our custom template
    'chapter_data': chapters, 
    'character_classes': characters,    
}

# generate HTML based on our custom template
pp.visualisation.export_html(t_lotr, filename='visualisations/4_demo_lotr.html', **style)

