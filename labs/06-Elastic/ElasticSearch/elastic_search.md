# Exploring data from Kibana sample data on e-commerce

Below are a number of example queries using query DSL (Domain Specific Language) that can be ran directly from the Kibana console (Management > Dev Tools).


## 1. Get search results from the ecommerce data index.


GET kibana_sample_data_ecommerce/_search

Look at the "value" of "hits" to retrieve how many observations are included.


## 2. Search for data within specific time range: 
type of query is range, retrieve orders that were placed within these two dates.

```bash
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "range": {
      "order_date": {
        "gte": "2023-04-16",
        "lte": "2023-04-17"
      }
    }
  }
}
```

## 3. Search for data that corresponds to certain criteria:
type of query is match, retrieve orders from customer with id 38

```bash
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match": {
      "customer_id": "38"
    }
  }
}
```

## 4. Aggregations: they summarize your data for example by certain categories:
this is an "aggs" request, which you need to give a name, then select the field on which to perform the aggregation

```bash
GET kibana_sample_data_ecommerce/_search
{
  "aggs": {
    "by_dayofweek": {
      "terms": {
        "field": "day_of_week"
      }
    }
  }
}
```

## 5. Combinations of query and aggs request

```bash
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match": {
      "customer_id": "38"
    }
  },
  "aggs": {
    "by_dayofweek": {
      "terms": {
        "field": "day_of_week"
      }
    }
  }
}
```

 - another option aggregate by significant text in a text field to find the most frequent terms


```bash
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match": {
      "customer_id": "38"
    }
  },
  "aggs": {
    "by_popular_terms_in_category": {
      "significant_text": {
        "field": "category"
      }
    }
  }
}
```

## 6. Full text search: query which retrieves documents that contain (match/match_prase) our search terms

- get all hits that contain any one of the search terms in any order, even if not in prximity of eachother
```bash
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match": {
      "manufacturer": {
        "query": "Tide Low"
      }
    }
  }
}
```

- get hits that contain all search terms in this exact order and next to eachother
```bash
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match_phrase": {
      "manufacturer": {
        "query": "Low Tide"
      }
    }
  }
}
```
## 7. Combined queries: bool query for retrieving documents matching a combination of search criteria

- must match all the listed criteria at the same time (AND)
```bash
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "must": [
        {
        "match": {
          "customer_first_name": "Jim"
         }
        },
        {
          "match": {
            "day_of_week": "Thursday"
          }
        }
      ]
    }
  }
}
```
- use "should" instead of "must" for a nice to have crieria, that ranks these results higher in the search results
```bash
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "must": [
        {
        "match": {
          "manufacturer": "Angeldale"
          }
         }
        ],
       "should":[
         {
          "match": {
            "customer_first_name": "Jim"
          }
        }
      ]
    }
  }
}
```
- use "filter" instead of "must" to filter only the documents that comply with some criteria (range or term)

```bash
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "must": [
        {
        "match": {
          "manufacturer": "Angeldale"
          }
         }
        ],
       "filter":{
          "range":{
             "order_id": {
               "gte": 579369,
               "lte": 589370
          }
        }
      }
    }
  }
}
```
```bash
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "must": [
        {
        "match": {
          "manufacturer": "Angeldale"
          }
         }
        ],
       "filter":{
          "term":{
             "day_of_week": "Thursday"
        }
      }
    }
  }
}
```