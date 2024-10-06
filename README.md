# Semantic Search Engine

A semantic search engine is a type of search engine that understands the meaning behind the words used in a query, rather than just matching keywords. Unlike traditional search engines that rely on exact word matches, semantic search looks at the context and relationships between words to provide more accurate results. It helps to find more relevant information even if the search query doesn't exactly match the text in the documents.

This project, aims to built a semantic search engine using BERT  and Elasticsearch (a search engine for indexing and querying data). This system can better understand the intent behind a query, improving the search experience by providing more meaningful results.

## Installation Guide

To Run the Semantic Search Engine, follow these steps:
```bash
git clone https://github.com/puzancozzu/sematic_search_engine.git
cd semantic_search_engine
pip install -r requirements.txt
```

To run sreamlit app:
```bash
streamlit run searchApp.py
```
For more detailed explanations and guidance, please refer to my_help.txt

## Workflow

1. **Data Processing**: The dataset, which has already been cleaned, undergoes an additional check for NA values. Any NA values are replaced with `None` to ensure data consistency.

2. **Embedding Creation**: Using a pretrained BERT model (available at [SBERT](https://sbert.net/docs/sentence_transformer/pretrained_models.html)), embeddings are generated for the relevant fields of the dataset. This process converts the textual data into vector representations.

3. **Index Creation**: An index space is created in Elasticsearch to store the vector embeddings along with the associated data. The tabular data is transformed into JSON format, which is the desired format for ingestion into Elasticsearch.

4. **Query Processing**: When a user inputs a keyword, the query is converted into an embedding. This query embedding is then compared with the document embeddings using distance metrics to generate search results. Documents with similarity scores above a specified threshold are returned as the output of the search.

