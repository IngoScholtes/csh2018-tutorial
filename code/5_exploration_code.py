#%% In [1]
import pathpy as pp

# Flight data  
flight_paths = pp.Paths.read_file('data/US_flights.ngram', frequency=False)

# Clickstreams, ignore single path with more than 400 clicks
clickstreams = pp.Paths.read_file('data/wikipedia_clickstreams.ngram', frequency=False, max_ngram_length=100)

# London Tube trips based on Oyster card checkin-checkouts
tube_net  = pp.Network.read_file('data/tube.edges', separator=';')
od_stats = pp.path_extraction.read_origin_destination('data/tube_od.csv', separator=';')
tube_trips = pp.path_extraction.paths_from_origin_destination(od_stats, tube_net)

