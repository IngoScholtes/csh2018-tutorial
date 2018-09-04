#%% In [1]
import pathpy as pp
import sqlite3

con = sqlite3.connect('data/temporal_networks.db',)
con.row_factory = sqlite3.Row

for row in con.execute('SELECT * from metadata'):
    print('{0} \t\t {1}'.format(row['tag'], row['name']))

#%% In [2]
table = 'manufacturing_email'

# Check whether network is directed or not
directed_network = bool(con.execute("SELECT directed FROM metadata WHERE tag='{0}'".format(table)).fetchone()['directed'])
t = pp.TemporalNetwork.from_sqlite(con.execute('SELECT source, target, time FROM ' + table), 
                                   directed=directed_network)
print(t)

