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
- Universal Sentence Encoder (USE) model downloaded locally - <https://tfhub.dev/google/universal-sentence-encoder-large/5>
- Installs:  
`pip3 install --upgrade pip`  
`pip3 install elasticsearch`  
`pip3 install pandas`  
`pip3 install --upgrade --no-cache-dir tensorflow`  
`pip3 install --upgrade tensorflow-hub`  

## Results

`NOTE: Results depend on # of samples in dataset, current project could be improved with some pre-processing of text`

Search Text = 'horror movies are not my type'

Results:  
{'percentage_match': 78, 'text': "Well, I like to watch bad horror B-Movies, cause I think it's interesting to see stupidity and unability of creators to shoot seriously good movie"}  
{'percentage_match': 71, 'text': 'Oh noes one of these attack of the Japanese ghost girl movies'}  
{'percentage_match': 69, 'text': "Average (and surprisingly tame) Fulci giallo which means it's still quite bad by normal standards, but redeemed by its solid build-up and some nice touches such as a neat time twist on the issues of visions and clairvoyance"}  
{'percentage_match': 69, 'text': 'This IS the worst movie I have ever seen, as well as, the worst that I will probably EVER see'}  
{'percentage_match': 68, 'text': 'Honestly - this short film sucks'}  
{'percentage_match': 68, 'text': 'This movie made it into one of my top 10 most awful movies'}  
{'percentage_match': 67, 'text': 'The Hills Have Eyes II is what you would expect it to be and nothing more'}  
{'percentage_match': 67, 'text': 'Some films just simply should not be remade'}  
{'percentage_match': 67, 'text': 'It had all the clichés of movies of this type and no substance'}  
{'percentage_match': 66, 'text': 'I remember this film,it was the first film i had watched at the cinema the picture was dark in places i was very nervous it was back in 74/75 my Dad took me my brother & sister to Newbury cinema in Newbury Berkshire England'}  