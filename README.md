# Text Search

## Problem Statement  

- For a given text, pair a most relavent text.

## References  

- <https://www.youtube.com/watch?v=3pRgZfjTb0c>
- <https://drive.google.com/file/d/1ZzM3uVmR6td0JQ9QfLs7Z0zYR2F4dCln/view>

## Approach

- For this project, let's use IMDB dataset of movie reviews and generate search results of review.
- Our problem seeks a similarity function for given text against dataset (all reviews). This problem is called as `Nearest Neighbour Search` problem (latest version of ElasticSearch has already implemented Nearest Neighbour Search)
- For vectorizer, let's use Google\Tensorflow's Universal Sentence Encoder (USE) with 512 dimensions.

## Requirements

- ElasticSearch database installed and running.
- Installs:  
`pip3 install --upgrade pip`  
`pip3 install elasticsearch`  
`pip3 install pandas`  
`pip3 install --upgrade --no-cache-dir tensorflow`  
`pip3 install --upgrade tensorflow-hub`  