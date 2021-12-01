import requests

# Function for getting countries currency
def countryCurrency(code):
    """
    Takes a 2 digit country code and outputs the currency used by that country
    """
    # Get request
    response = requests.get(
        url=f'https://restcountries.com/v2/alpha/%s' % code)
    # Store data
    data = response.json()
    # Grab only currencies
    currency = data['currencies']
    # Grab only name of currency
    output = currency[0]['name']
    return output
