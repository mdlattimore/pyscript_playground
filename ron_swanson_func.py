import requests


def ron_swanson_quote(query: str) -> str:
    """A generic function that retrieves one or more (or none) Ron Swanson quotes
    using a search term ('query'). If 'query' is an empty string, the api will
    return a random quote. Requires calling program to import requests module. 
    Return value is a list. It is left to the calling code to decide 
    what to do with the return value. Alternatively, user could comment out 
    'return response.json()' and uncomment the three following lines to print the
    quote(s) from the function"""

    endpoint = "https://ron-swanson-quotes.herokuapp.com/v2/quotes/search/{}".format(
        query)

    response = requests.get(endpoint)
    return response.json()
    # for quote in response.json():
    #     print(quote)
    #     print()


if __name__ == "__main__":

    response = ron_swanson_quote("")
    for quote in response:
        print(quote)
    print(type(response))