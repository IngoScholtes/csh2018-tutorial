---
title: Hands-on Tutorial on Higher-Order Data Analytics
permalink: /pathpy
---

# Higher-order Analytics with pathpy

This tutorial gives an in-depth introduction to the python Open Source data analytics package `pathpy`.

`pathpy` provides a new approach to analyse and visualise time-series data on complex networks. Examples include time-stamped social networks, traces on flow processes in networks, passenger itineraries in transportation networks, user clickstreams in the Web, citation networks, or biological pathway data. Building on the higher- and multi-order statistical modelling framework introduced in [[1]](http://www.nature.com/ncomms/2014/140924/ncomms6024/full/ncomms6024.html) and [[2]](http://dl.acm.org/citation.cfm?id=3098145), `pathpy` offers machine learning techniques to select optimal, higher-order network models for your data. It then uses these models to detect, model, and visualise higher-order dependencies and patterns discarded by state-of-the-art data analytics methods that focus on dyadic links.

The following video gives a high-level explanation of the science behind `pathpy`:

[![Watch promotional video](https://img.youtube.com/vi/CxJkVrD2ZlM/0.jpg)](https://www.youtube.com/watch?v=CxJkVrD2ZlM)

Details of the scientific background can be found in the following published works:

1. I Scholtes: [When is a network a network? Multi-Order Graphical Model Selection in Pathways and Temporal Networks](http://dl.acm.org/citation.cfm?id=3098145), In KDD'17 - Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Halifax, Nova Scotia, Canada, August 13-17, 2017
2. I Scholtes, N Wider, A Garas: [Higher-Order Aggregate Networks in the Analysis of Temporal Networks: Path structures and centralities](http://dx.doi.org/10.1140/epjb/e2016-60663-0), The European Physical Journal B, 89:61, March 2016
3. I Scholtes, N Wider, R Pfitzner, A Garas, CJ Tessone, F Schweitzer: [Causality-driven slow-down and speed-up of diffusion in non-Markovian temporal networks](http://www.nature.com/ncomms/2014/140924/ncomms6024/full/ncomms6024.html), Nature Communications, 5, September 2014
4. R Pfitzner, I Scholtes, A Garas, CJ Tessone, F Schweitzer: [Betweenness preference: Quantifying correlations in the topological dynamics of temporal networks](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.110.198701), Phys Rev Lett, 110(19), 198701, May 2013

This hands-on tutorial introduces the theoretical foundations of `pathpy` and uses empirical and synthetic data to show how they can be practically applied in `python`. The latest release of `pathpy` is available via the [python package index](https://pypi.org/project/pathpy2/). In python 3.x, you can install it by typing:

```
pip install pathpy2
```

`pathpy` is fully integrated with `jupyter`, providing in-line, interactive and dynamic visualisations of graphs, temporal networks, as well as higher- and multi-order network models. This teaser highlights some of its features:

[![Watch promotional video](https://img.youtube.com/vi/QIPqFaR2Z5c/0.jpg)](https://www.youtube.com/watch?v=QIPqFaR2Z5c)

A description of the [recommended setup](https://ingoscholtes.github.io/csh2018-tutorial/setup) to complete this tutorial is available [online](https://ingoscholtes.github.io/csh2018-tutorial/setup). A brief introduction to interactive data science with `python`, `Visual Studio Code`, and `jupyter` is given in [unit 1](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/code/1_vscode_jupyter.py).

The remaining seven units (approx. 30 minutes each) introduce `pathpy`'s approach to the modeling and analysis of time series data on complex networks. For each unit we provide a stand-alone HTML file, as well as a juypter notebook that you can download and run on your machine. In units 5 and 8 we invite you to use `pathpy` to explore higher- and multi-order models on your own.

Unit | Topic | jupyter notebook  
------|-----|-----
Lecture | [Understanding Complex Systems - From Networks to Optimal Higher-order Models](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/docs/slides.pdf) | [pdf](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/docs/slides.pdf)
1 | [Data Science with python, jupyter, and VSCode](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_vscode_jupyter.py) | [py](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/1_vscode_jupyter.py)
2 | [Introducing `pathpy`](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/2_pathpy.html) | [html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/2_pathpy.html) [ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/2_pathpy.ipynb)  
3 | [Higher-order analysis of path data](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/3_higher_order.html) | [html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/3_higher_order.html) [ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/3_higher_order.ipynb)  
4 | [Temporal Network Analysis and Visualisation](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/4_temporal_networks.html) | [html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/4_temporal_networks.html) [ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/4_temporal_networks.ipynb)  
5 | [Exploration: Higher-order analysis of time series data](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/5_exploration.html) | [html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/5_exploration.html) [ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/5_exploration.ipynb)  
6 | [Multi-order Representation Learning](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/6_multi_order.html) | [html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/6_multi_order.html) [ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/6_multi_order.ipynb)  
7 | [Optimal higher-order analysis of temporal data](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/7_optimal_analysis.html)| [html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/7_optimal_analysis.html) [ipnyb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/7_optimal_analysis.ipynb)  
8 | [Exploration: Representation learning in time series data](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/8_exploration.html) | [html](https://htmlpreview.github.io/?https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/8_exploration.html) [ipynb](https://github.com/IngoScholtes/csh2018-tutorial/blob/master/solutions/8_exploration.ipynb)  

`pathpy` is brought to you by the [Data Analytics Group](http://www.ifi.uzh.ch/dag) at the [Department of Informatics](http://www.ifi.uzh.ch) of [University of Zurich](http://www.uzh.ch).

Feel free to [get in touch](http://www.ifi.uzh.ch/en/dag/people/scholtes.html) if you want to host an interaction hands-on tutorial in your research group, institute, or company.