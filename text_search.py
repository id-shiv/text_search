# Import packages
from elasticsearch import Elasticsearch
import tensorflow as tf
import tensorflow_hub as hub

import json
import pandas as pd
import numpy as np
from tqdm import tqdm

#region CONSTANTS

## DATA
DATA_PATH = '/Users/shiv/Documents/gitRepositories/iutils/input/data/IMDB Dataset.csv'
TEXT_COLUMN = 'review'

## DATABASE
DB_HOST_NAME = 'localhost'
DB_PORT = 9201

## ENCODER
ENCODER_PATH = '/Users/shiv/Documents/gitRepositories/text_search/encoders/universal-sentence-encoder-large_5'
ENCODER = hub.load(ENCODER_PATH)  # Load the encoder

#endregion

def get_data(data_path: str, text_column: str):
    # Read the dataset and retrieve texts
    data = pd.read_csv(data_path)
    # Let's use only the first text of the review for our project
    data[text_column] = data[text_column].apply(lambda x: x.split('.')[0])

    return data

def db_setup(hostname: str, port: int):
    # connect to ES
    db = Elasticsearch([{'host': hostname, 'port': port}])
    if db.ping():
        print('Connected to ES!')
    else:
        print('Could not connect!')
        
    # Refer: https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html
    # Mapping: Structure of the index
    # Property/Field: name and type  
    b = {"mappings": {
            "properties": {
                    "title": {
                        "type": "text"
                    },
                    "title_vector": {
                        "type": "dense_vector",
                        "dims": 512
                }
            }
        }
    }

    ret = db.indices.create(index='texts', ignore=400, body=b) # 400 caused by IndexAlreadyExistsException, 
    print(json.dumps(ret,indent=4))

    # TRY this in browser: http://localhost:9200/texts

def db_connect(hostname: str, port: int):
    print(f'Connecting to ES {hostname} at {str(port)}')
    db = Elasticsearch([{'host': hostname, 'port': port}])
    if db.ping():
        print('Connected to ES!')
    else:
        print('Could not connect!')
    return db

def db_insert(database: Elasticsearch(), text_id: int, text: str, text_vector: list()):
    b = {
            "title":text,
		    "title_vector":text_vector
	}
    database.index(index="texts", id=text_id, body=b)
    # View details: http://localhost:9200/texts/_stats?pretty
    # View a document: http://localhost:9200/texts/_doc/1

def encode(encoder, text: str):
    # Encode and convert the encode tensor to list
    embeddings = tf.make_ndarray(tf.make_tensor_proto(ENCODER([text]))).tolist()[0]

    # Return a vector of 512 dimensions as a list
    return embeddings

def insert_encoded_data_to_db(database: Elasticsearch(), encoder, data: pd.DataFrame(), text_column: str):
    # Encode and insert text ID, text and it's vector in Database
    for index, row in tqdm(data.iterrows()):
        text = row[text_column]
        text_vector = encode(encoder, text)
        text_id = index
        db_insert(database, text_id, text, text_vector)

def search_by_vector(database: Elasticsearch(), query_vector: list()):
    search_results = list()

    # Search by Vector Similarity
    b = {
            "query": {
                "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'title_vector') + 1.0",
                    "params": {"query_vector": query_vector}
                }
            }
        }
    }

    # print(json.dumps(b,indent=4))
    res= database.search(index='texts', body=b)

    for hit in res['hits']['hits']:
        search_result = {
            'score': hit['_score'],
            'text': hit['_source']['title']
        }
        search_results.append(search_result)

    return search_results
   
def normalize_scores(scores: list()): 
    return [score/np.max(scores) for score in scores]

def search(database: Elasticsearch, text: str, text_vector: list()):
    search_results = list()

    search_results = search_by_vector(database, text_vector)
    
    # Convert score to percentage match
    search_results = [{'percentage_match': round((search_result['score']/2) * 100), 
                                'text': search_result['text']
                            } for search_result in search_results]

    return search_results

if __name__=='__main__':
    # Load the data (with only 100 samples)
    data = get_data(DATA_PATH, TEXT_COLUMN)[:100]

    # Setup Database
    db_setup(hostname=DB_HOST_NAME, port=DB_PORT)

    # Connect Database
    db = db_connect(hostname=DB_HOST_NAME, port=DB_PORT)

    # Insert text and encoded text to Database
    insert_encoded_data_to_db(db, ENCODER, data, TEXT_COLUMN)
    
    # Search new text
    text_to_search = 'horror movies not my type'
    results = search(db, text_to_search, encode(ENCODER, text_to_search))
    for result in results:
        print(result)