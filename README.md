
# Movie Recommendation System

Recommending 5 movies based on the movie that you like.

## Dataset

 - [ Kaggle TMDB Dataset ](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)


## Deployment

- To deploy this project download and extract dataset from kaggle.
- Download `MRS.ipynb` ,`main.py` and `api.py` files from the repository.
- Create a TMDB acoount and request for an API key.
- Replace the 'YOUR_API_KEY' text in `api.py` file.
- Run all the cells in `MRS` juputer notebook file to create the `.pkl` files for the application.
- Run the `main.py` application by using the below command.


```bash
  streamlit run main.py
```


## Libraries
- `numpy`
- `pandas`
- `ast`
- `CountVectorizer` from `sklearn.feature_extraction.text`
- `PorterStemmer` from `nltk.stem.porter`
- `cosine_similarity` from `sklearn.metrics.pairwise`
- `pickle`
- `requests`
- `streamlit`

