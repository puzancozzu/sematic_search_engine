import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

indexName = "laptop_products"

try:
    es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "iiGa0a1_zTfj8ijJPksW"),
    ca_certs= "E:\\DLytica_train\\semantic_search_engine\\elasticsearch-8.15.2\\config\\certs\\http_ca.crt"           
)
except ConnectionError as e:
    print("Connection Error:", e)
    
if es.ping():
    print("Succesfully connected to ElasticSearch!!")
else:
    print("Oops!! Can not connect to Elasticsearch!")




def search(input_keyword):
    model = SentenceTransformer('all-mpnet-base-v2')
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
        "field": "DecriptionVector",
        "query_vector": vector_of_input_keyword,
        "k": 10,
        "num_candidates": 600
    }
    res = es.knn_search(index="laptop_products"
                        , knn=query 
                        , source=["link","product_title", "price"]
                        )
    results = res["hits"]["hits"]

    return results

def main():
    st.title("Search Daraz Laptop Products")

    ### Input: User enters search query
    search_query = st.text_input("Enter your search query")

    ### Button: User triggers the search
    if st.button("Search"):
        if search_query:
            ### Perform the search and get results
            results = search(search_query)

            ### Display search results
            st.subheader("Results Found")
            for result in results:
                with st.container():
                    if result['_score'] <= 0.41:
                        print(result['_score'])
                        continue

                    else:
                        ##we have data in key : "source"
                        if '_source' in result:
                            
                            try:
                                st.header(f"Description: {result['_source']['product_title']}")
                            except Exception as e:
                                print(e)

                            try:
                                st.write(f"Price: {result['_source']['price']}")
                            except Exception as e:
                                print(e)

                            try:
                                st.write(f"Similarity_score: {result['_score']}")
                            except Exception as e:
                                print(e)
                            
                            try:
                                st.write(f"Link: {result['_source']['link']}")
                            except Exception as e:
                                print(e)
                            st.divider()

                    
if __name__ == "__main__":
    main()
