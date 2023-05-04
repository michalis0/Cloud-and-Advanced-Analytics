## NetworkX Tutorial
This week we will have a look at a Python library called NetworkX, which is used to work with networks. NetworkX is a very powerful tool that can be used to analyze the structure of social networks (who is connected to whom), biological networks (how proteins interact), technological networks (how the internet is connected) and many more.

In this tutorial, we will learn the basics of NetworkX and how to use it to analyze real-world networks. We will also learn how to visualize networks using a library called Matplotlib.

## What is a network?

A network is a collection of nodes and edges. Nodes are the entities of the network, and edges are the connections between them. For example, in a social network, nodes would be people, and edges would be friendship connections between them. In a biological network, nodes would be proteins, and edges would be physical interactions between them.


## Plan

1. Introduction to NetworkX: walkthough of basic NetworkX functionality
2. Exercises

## Exercise
- Load from [here](http://snap.stanford.edu/data/ego-Facebook.html) the dataset facebook_combined.txt.gz

  * Each node represents an anonymized facebook user that belongs to one of those ten friends lists.
  * Each edge corresponds to the friendship of two facebook users that belong to this network. In other words, two users must become friends on facebook in order for them to be connected in the particular network.

- Visualize the dataset using networkX (consider using nx.spring_layout)
- What’s the number of nodes? and edges?
- What’s the average degree?
- What’s the length of shortest path between nodes 0 and 42?
- The diameter of a graphs is the maximum number of nodes you need to traverse to connect from one node to any other one. Compute the diameter of the graph ([Curiosity: 6 degrees of separation theory](https://en.wikipedia.org/wiki/Six_degrees_of_separation)) 
- Compute the average path lenght
- Plot an histogram of the distribution of shortest path lengths
- Compute the density of the graph
- Compute the number of connected components
- Compute the nodes with the highest degree centralities. How many neighbors do they have?
- Plot the histogram of degrees centralities
- Draw the network using networkX, with the size of the nodes depending on their degree centrality
- Compute the nodes with the highest betweeness centrality, plot the histogram, and the graph with the sizes proportional to their values of betweeness centrality
- Do the same with closeness centrality
- The clustering coefficient of a node v is defined as the probability that two randomly selected friends of v are friends with each other. As a result, the average clustering coefficient is the average of clustering coefficients of all the nodes. The closer the average clustering coefficient is to 1, the more complete the graph will be because there’s just one giant component. Compute the average clustering coefficient and plot the histogram. 
- Choose a method for community detection, apply it to the graph and plot the nodes of each community with a different color. 


