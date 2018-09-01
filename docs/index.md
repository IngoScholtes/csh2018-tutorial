---
title: Hands-on Tutorial on Higher-Order Data Analytics
permalink: /
---

Network-based data mining techniques such as graph mining, (social) network analysis, link prediction and graph clustering form an important foundation for data science applications in computer science, computational social science, and the life sciences. They help to detect patterns in large data sets that capture dyadic relations between pairs of genes, species, humans, or documents and they have improved our understanding of complex networks.

While the potential of analysing graph or network representations of relational data is undisputed, we increasingly have access to data on networks that contain more than just dyadic relations. Consider, e.g., data on user click streams in the Web, time-stamped social networks, gene regulatory pathways, or time-stamped financial transactions. These are examples for time-resolved or sequential data that not only tell us who is related to whom but also when and in which order relations occur. Recent works have exposed that the timing and ordering of relations in such data can introduce higher-order, non-dyadic dependencies that are not captured by state-of-the-art graph representations. This oversimplification questions the validity of graph mining techniques in time series data and poses a threat for interdisciplinary applications of network analytics.


To address this challenge, researchers have developed advanced graph modelling and representation techniques based on higher- and variable-order Markov models, which enable us to model non-Markovian characteristics in time series data on networks. Introducing this exciting research field, the goal of this tutorial is to give an overview of cutting-edge higher-order data analytics techniques. Key takeaways for attendees will be (i) a solid understanding of higher-order network modelling and representation learning techniques, (ii) hands-on experience with state-of-the-art higher-order network analytics and visualisation packages, and (iii) a clear demonstration of the benefits of higher-order data analytics in real-world time series data on technical, social, and ecological systems.

# Tutor

[Ingo Scholtes, Head of Data Analytics Group, University of Zurich](http://ifi.uzh.ch/dag)

# Prerequisites

Participants should bring a laptop with a python 3.x environment. See [setup instructions](/csh2018-tutorial/setup). Some basic prior exposure to python is beneficial. In the first session of the tutorial we will give a brief introduction to interactive data science with python, jupyter notebook, and VS Code.

# Schedule

### Session 1: Introduction to Higher-Order Network Analytics

**Welcome Note and Tutorial Overview**

**Intro: Higher-Order Network Analytics for Time Series Data** (45 min)
- Causal paths in temporal network data
- Ordering matters in time series data
- Higher-order generative models for causal paths
- Representation learning in temporal network data

**Live Coding** (45 min)

Unit | Topic | Tasks | Solution
----|----|----|----
1 | A Primer to Data Science with `python`, `jupyter`, `git` and `VS Code` (15 min) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_1_vscode_jupyter.py) | N/A
2 | Analysis and Visualisation of Path Data in [`pathpy`](http://www.pathpy.net) (30 min) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_2_pathpy.py), [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_2_pathpy.ipynb) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_2_pathpy.py) [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_2_pathpy.ipynb) [.html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_2_pathpy.html)

### Coffee break

### Session: Higher-order Network Analysis

**Live Coding** (90 min)

Unit | Topic | Tasks | Solution
----|----|----|----
3 | Fitting and Visualising Higher-order Network Models (30 min) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_3_higher_order.py),  [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_3_higher_order.ipynb) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_3_higher_order.py) [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_3_higher_order.ipynb) [.html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_3_higher_order.html)
4 | Time-stamped Network Analysis in [`pathpy`](http://www.pathpy.net) (30 min) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_4_temporal_networks.py), [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_4_temporal_networks.ipynb) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_4_temporal_networks.py) [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_4_temporal_networks.ipynb) [.html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_4_temporal_networks.html)
5 | Exploration: Higher-order Analysis of [real-world data](https://github.com/IngoScholtes/csh2018-tutorial/tree/master/data) (30 min) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_5_exploration.py), [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_5_exploration.ipynb) | N/A

### Coffee break

### Session: Multi-order Representation Learning

**Live Coding** (90 min)

Unit | Topic | Tasks | Solution
----|----|----|----
6 | Multi-order Representation Learning (30 min) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_6_multi_order.py), [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_6_multi_order.ipynb) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_6_multi_order.py) [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_6_multi_order.ipynb) [.html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_6_multi_order.html)
7 | Optimal Higher-order Analytics for Temporal Data (30 min) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_7_optimal_analysis.py), [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_7_optimal_analysis.ipynb) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_7_optimal_analysis.py) [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_7_optimal_analysis.ipynb) [.html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_7_optimal_analysis.html)
8 | Exploration: Multi-order Analysis of [Time-stamped Social Networks](https://github.com/IngoScholtes/csh2018-tutorial/tree/master/data) (30 min) | [.py](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_8_exploration.py),  [.ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_8_exploration.ipynb) | N/A

# Data sets

A description of data sets that will be provided to participants, and which will be analysed in the tutorial is available [here](https://github.com/IngoScholtes/csh2018-tutorial/tree/master/data).

# Setting up the environment

Hands-on sessions will be completed in `python`. A detailed description on how to set up the environment can be found in the [setup instructions](/csh2018-tutorial/setup).
