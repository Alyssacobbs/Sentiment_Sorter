import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    Create a bar chart showing the frequency of sentiment labels.

    Args:
        sentiments (str): A list of sentiments as strings labeled either "positive", "negative", "neutral", or "irrelevant".

    Returns:
       image: The count of each sentiment category visualized as a bar graph.
    """
    #Count sentiments from the list of data.
    pos_count= sentiments.count("positive")
    neg_count= sentiments.count("negative")
    neu_count= sentiments.count("neutral")
    irr_count= sentiments.count("irrelevant")
    
    
    # Create a bar chart to plot the number of sentiments.
    fig, ax = plt.subplots()
    ax.bar(["positive", "negative", "neutral", "irrelevant"], [pos_count,neg_count,neu_count,irr_count])
    ax.set_title("Sentiment Analysis")
    ax.set_xlabel("Types of Sentiments")
    ax.set_ylabel("Frequency")
    fig.savefig("images/sentimentsfinal") 
    
    
    
