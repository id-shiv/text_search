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
- Universal Sentence Encoder (USE) model downloaded and stored locally from <https://tfhub.dev/google/universal-sentence-encoder-large/5>
- IMDB Dataset downloaded and stored locally from <https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews>
- Installs:  
`pip3 install --upgrade pip`  
`pip3 install elasticsearch`  
`pip3 install pandas`  
`pip3 install --upgrade --no-cache-dir tensorflow`  
`pip3 install --upgrade tensorflow-hub`  

## Configurations

### DATA

DATA_PATH = '/Users/shiv/Documents/gitRepositories/iutils/input/data/IMDB Dataset.csv'  
TEXT_COLUMN = 'review'  
NUM_OF_SAMPLES = 100  

### DATABASE

DB_HOST_NAME = '127.0.0.1'  
DB_PORT = 9201  

### ENCODER

ENCODER_PATH = '/Users/shiv/Documents/gitRepositories/text_search/encoders/universal-sentence-encoder-large_5'  
_encoder = hub.load(ENCODER_PATH)  # Load the encoder

## Results

`NOTE: Results depend on # of samples in dataset, current project could be improved with some pre-processing of text`

Search Text = 'psychological thriller is what i like'

Results:  
{'percentage_match': 73, 'text': "Well, I like to watch bad horror B-Movies, cause I think it's interesting to see stupidity and unability of creators to shoot seriously good movie"}  
{'percentage_match': 70, 'text': '"The Cell" is an exotic masterpiece, a dizzying trip into not only the vast mind of a serial killer, but also into one of a very talented director'}  
{'percentage_match': 67, 'text': "Average (and surprisingly tame) Fulci giallo which means it's still quite bad by normal standards, but redeemed by its solid build-up and some nice touches such as a neat time twist on the issues of visions and clairvoyance"}  
{'percentage_match': 67, 'text': 'Taut and organically gripping, Edward Dmytryk\'s Crossfire is a distinctive suspense thriller, an unlikely "message" movie using the look and devices of the noir cycle'}  
{'percentage_match': 65, 'text': 'This movie struck home for me'}  
{'percentage_match': 65, 'text': 'How this film could be classified as Drama, I have no idea'}  
{'percentage_match': 64, 'text': 'This film took me by surprise'}  
{'percentage_match': 64, 'text': 'This film laboured along with some of the most predictable story lines and shallow characters ever seen'}  
{'percentage_match': 63, 'text': 'Oh noes one of these attack of the Japanese ghost girl movies'}  
{'percentage_match': 63, 'text': 'I really like Salman Kahn so I was really disappointed when I seen this movie'}  
