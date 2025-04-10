<h1 align="center"> LAB 8:  Graph Analytics in Python</h1>
<div>
<td> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Logo_Universit%C3%A9_de_Lausanne.svg/2000px-Logo_Universit%C3%A9_de_Lausanne.svg.png" style="padding-right:10px;width:240px;float:left"/></td>
<h2 style="white-space: nowrap">Cloud and Advanced Analytics </h2></td>
<hr style="clear:both">
<p style="font-size:0.85em; margin:2px; text-align:justify">
<br>
<br>
</div>

This week we will have a look at a Python library called NetworkX, which is used to build and analyze networks (Graphs). NetworkX is a very powerful tool that can be used to analyze the structure of social networks (who is connected to whom), biological networks (how proteins interact), technological networks (how the internet is connected) and many more.

## Introduction
A network is a collection of nodes and edges. Nodes are the entities of the network, and edges are the connections between them. For example, in a social network, nodes would be people, and edges would be friendship connections between them. In a biological network, nodes would be proteins, and edges would be physical interactions between them.

In this tutorial, we will learn the basics of NetworkX and how to use it to analyze real-world networks. We will also learn how to visualize networks using Matplotlib library.


## Learning Goals
In this lab, you'll:
- Understand the basic structure of networks and the concepts of nodes and edges.
- Gain familiarity with NetworkX and learn how to use it for network analysis.
- Practice loading and analyzing real-world network data.
- Explore various network characteristics such as the number of nodes, edges, average degree, shortest paths, and diameter of the graph.
- Gain hands-on experience with network visualization using NetworkX and Matplotlib.
- Learn how to compute and interpret various centrality measures, including degree centrality, betweenness centrality, and closeness centrality.
- Understand the concept of clustering coefficient and how to compute it.
- Develop skills in community detection within networks and learn how to visualize communities.

By the end of this lab, you will be well-equipped to apply NetworkX to analyze and visualize complex networks, whether they are social, biological, technological or any other kind of network.

## Exercise
- Load from [here](http://snap.stanford.edu/data/ego-Facebook.html) the dataset facebook_combined.txt.gz. This dataset contains the network of facebook users at the University of California, Berkeley. The network was collected using the Facebook Graph API. Nodes represent facebook users and edges represent friendships between them. The dataset contains 4039 nodes and 88234 edges.
  * Each node represents an anonymized facebook user that belongs to one of those ten friends lists.
  * Each edge corresponds to the friendship of two facebook users that belong to this network. In other words, two users must become friends on facebook in order for them to be connected in the particular network.

### Answer the following questions exploring the dataset with NetworkX:
- Visualize the dataset using networkX (consider using nx.spring_layout)
- What’s the number of nodes? and edges?
- What’s the average degree?
- What’s the length of shortest path between nodes 0 and 42?
- The [diameter](https://en.wikipedia.org/wiki/Distance_(graph_theory)#:~:text=To%20find%20the%20diameter%20of,the%20diameter%20of%20the%20graph.) of a graphs is the maximum number of nodes you need to traverse to connect from one node to any other one. Compute the diameter of the graph ([Curiosity: 6 degrees of separation theory](https://en.wikipedia.org/wiki/Six_degrees_of_separation)). 
- Compute the average path length.
- Plot an histogram of the distribution of shortest path lengths.
- Compute the density of the graph.
- Compute the number of connected components.
- Compute the nodes with the highest degree centralities. How many neighbors do they have?
- Plot the histogram of degrees centralities
- Draw the network using networkX, with the size of the nodes depending on their degree centrality
- Compute the nodes with the highest betweeness centrality, plot the histogram, and the graph with the sizes proportional to their values of betweeness centrality
- Do the same with closeness centrality
- The clustering coefficient of a node v is defined as the probability that two randomly selected friends of v are friends with each other. As a result, the average clustering coefficient is the average of clustering coefficients of all the nodes. The closer the average clustering coefficient is to 1, the more complete the graph will be because there’s just one giant component. Compute the average clustering coefficient and plot the histogram. 
- Choose a method for community detection, apply it to the graph and plot the nodes of each community with a different color. 
