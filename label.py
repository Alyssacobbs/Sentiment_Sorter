from openai import OpenAI


def get_sentiment(text: list) -> list:
    """
    Utilize openai large language model to output a list of sentiments from a list of reviews with no extraneous blank lines.

    Args:
       text (str): A list containing product reviews.
        
    Returns:
        processed_list (str): It will return the list of sentiments (e.g. positive, neutral, negative, or irrelevant). If input is not valid, a error message is returned. 
    
    """
    # Check if the input is not a string or is empty
    for elm in text:
        if not isinstance(elm, str): 
            return "Wrong input. text must be an array of strings."
    if text == []:
        return "Wrong input. text must be an array of strings."      
    
    system_prompt = """You are a helpful sentiment sorter that categorizes reviews. The catergories will either be
    positive, neutral, negative, or irrelevant."""

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """
    client = OpenAI()
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
	        { "role": "developer", "content": system_prompt},
             { "role": "user", "content": prompt},
        ]
)    

    output_list = response.choices[0].message.content.strip().split("\n")
    processed_list = []
    for items in output_list:
        items = items.strip()
        processed_list.append(items)
    return processed_list
    
    print(processed_list)