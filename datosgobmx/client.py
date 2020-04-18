import re
import json

from urllib.request import urlopen
from urllib.parse import urljoin, quote_plus

BASE_URL = 'https://api.datos.gob.mx/v2/'

def api(endpoint='api-catalog', query={}):
    """Returns the `"results"` property from the response of a given endpoint"""
    return make_call(endpoint, query=query)['results']


def make_call(endpoint, query={}):
    """Make a request to https://api.datos.gob.mx

    :type endpoint: str
    :param endpoint: One of the endpoints available from https://api.datos.gob.mx

    :type query: dict, optional
    :param query: A dictionary where the key might include an operator, if no
        operator is provided "=" is assumed.
 
    :Example: 

    make_call('resource', query={'pageSize': 1})
    """
    url = create_url(endpoint, query)
    with urlopen(url) as response:
        result = json.loads(response.read().decode("utf-8"))
        return result


def create_url(endpoint='api-catalog', query={}):
    """Creates a URL using the API's base URL and the user specified endpoint
    and query.
    """
    url = urljoin(BASE_URL, endpoint)

    query_parts = create_query_parts(query)

    if query_parts:
        url += '?'
        url += '&'.join(query_parts)

    return url


def create_query_parts(query):
    """Converts the user query dictionary into URL Query string parts

    The query dictionary might contain _operators_ as part of each key, i.e.:

    ```
    {
        'count>': 10,
        'score<=': 11,
        'page': 1
    }
    ```

    This function converts the previous sample to a list of strings that look
    like this:

    ```
    ['count>10', 'score<=11', 'page=1']
    ```
    """
    parts = []
    for key, value in query.items():
        first_term = key
        operator = '='
        second_term = str(value)

        regex_result = re.search('(\<|\>)=?', first_term)
        if regex_result is not None:
            operator = regex_result.group(0)

        first_term = first_term.replace(operator, '')

        parts.append('{key}{operator}{value}'.format(
            key=first_term, operator=operator, value=quote_plus(second_term)
        ))

    return parts
