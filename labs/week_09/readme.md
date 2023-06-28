<h1 align="center"> LAB 9 - Elastic Cloud</h1>
<div>
<td> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Logo_Universit%C3%A9_de_Lausanne.svg/2000px-Logo_Universit%C3%A9_de_Lausanne.svg.png" style="padding-right:10px;width:240px;float:left"/></td>
<h2 style="white-space: nowrap">Cloud and Advanced Analytics </h2></td>
<hr style="clear:both">
<p style="font-size:0.85em; margin:2px; text-align:justify">
<br>
<br>
</div>

This week, you will learn about Elastic Cloud, a platform which enables search and analytics for both structured and unstructured data.


## Learning Goals
* Become aware of the various components of the Elastic stack and their respective roles
* Explore the Kibana dashboard, the web interface that allows you to explore your data
* Get acquainted with the Query DSL search syntax in Elastic Search
* Leverage Elasticsearch's "Edge n-gram" tokenizer to create an autocompletion functionality.

## Introduction
Elastic Cloud is a potent suite of services built around Elasticsearch, a distributed, open-source search and analytics engine. Elasticsearch is known for its speed, scalability, and ability to index many types of content, which makes it a go-to choice for applications that require complex search features.

The Elastic Stack (also known as ELK Stack) consists of Elasticsearch for search, Logstash for centralized logging and Kibana for visualization. The Elastic Stack has a wide range of applications, including but not limited to, real-time application monitoring, analyzing business metrics, and web search.

In this lab, we will not only cover the basics of setting up Elastic Cloud but also delve into more advanced topics like data visualization, query DSL, and the creation of autocomplete functionalities


## Lab Walkthrough
1. Questions about the project
2. Create a free 2 week account, no credit card required on www.elastic.co/
3. Elastic Cloud intro: Elastic Search and Kibana
4. Walkthrough: initial exploration - visualize a sample dataset (discover page, dashboards, canvas, maps, graphs)
5. Walkthrough: upload of custom dataset
6. Walkthrough: introduction to query DSL using the Kibana Dev Tools Console: CRUD operations (credits to [this guide](https://github.com/LisaHJung/Part-1-Intro-to-Elasticsearch-and-Kibana)). Difference between PUT and POST.
7. Exercise 1: CRUD Operations
8. Walkthrough: creation an autocomplete functionality for your index using the Edge n-gram tokenizer in the Kibana Dev Tools Console
9. Exercise 2: create a kibana dashboard with a public dataset
10. Walkthrough: Python elastic API


## Exercises

### CRUD Operations 
[Credits](https://github.com/LisaHJung/Part-1-Intro-to-Elasticsearch-and-Kibana)

1. Create an index called destinations.
2. Pick five dream travel destinations. For each destination, index a document containing the name and the country.
3. Read (GET) each document to check the content of the document.
4. Update a field of a document.
5. Read (GET) the updated document to ensure that the field has been updated.
6. Delete a document of one place.
7. Copy and paste the following request to return all documents from the destinations index. This is a great way to check whether all the CRUD operations you have performed thus far have worked!

```
GET destinations/_search
{
  "query": {
    "match_all": {}
  }
}
```

### Kibana Dashboard
1. Find a public dataset (e.g., on Kaggle, data.world, etc.)
2. Add and index the data on Elasticsearch (Home > Upload a file)
3. Think of a use case: what knowledge do you want to extract from the data?
4. Create a new dashboard (Analytics > Dashboard > Create dashboard)
5. Add three panels that are relevant to your use case. Try using different types of panels!
6. Present your dashboard to the class: which dataset, which visualizations you chose and why.


## Resources
- If you want to broaden your knowledge beyond this lab, the Elastic website provides many [video tutorials](https://www.elastic.co/videos/).
- If you are unsure how to make your queries, the [Query DSL documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html) has everything, including examples.
- [Beginners crash-course](https://github.com/LisaHJung/Part-1-Intro-to-Elasticsearch-and-Kibana)
