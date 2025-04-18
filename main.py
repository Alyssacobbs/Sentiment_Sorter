from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    Import a JSON file containing review data and visualizes the frequency of sentiments.
    
    Args:
        filepath (str): The path to the JSON file containing review data as a list.

    Returns:
       final_sentiment (str): A list of sentiment labeled for each review as positive, neutral, negative, or irrelevant.  The count of each sentiments will be visualized as a bar graph.
        
    """
    # open the json object
    with open(filepath, 'r') as file:
        open_reviews = json.load(file)

    # extract the reviews from the json file
    data_reviews = open_reviews["results"]

    # get a list of sentiments for each line using get_sentiment
    final_sentiments = get_sentiment(data_reviews)

    # plot a visualization expressing sentiment ratio
    make_plot(final_sentiments)

    # return sentiments
    print(final_sentiments)
    return final_sentiments
    

if __name__ == "__main__":
    print(run("data/raw/reviews.json"))


