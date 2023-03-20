import re
from urllib.parse import urlsplit, parse_qs, urlparse


def parse_form_to_dict(url_or_formdata):
    """
    This function takes a form body or a URL string and returns a dictionary
    with key-value pairs extracted from the form body or URL query string.
    """
    # Check if the input is a URL
    if is_url(url_or_formdata):
        # Extract the query string from the URL
        query_string = urlparse(url_or_formdata).query
    else:
        query_string = url_or_formdata

    # Validate the query string format
    pattern = r'[^&\n\t]+=[^&\n\t]+'
    if not re.match(pattern, query_string):
        # raise ValueError("Invalid query string format")
        return False

    # Use 'parse_qs' to parse the query string into a dictionary
    form_dict = parse_qs(query_string)

    # Convert the list values into single values
    form_dict = {k: v[0] for k, v in form_dict.items()}

    return form_dict


def is_url(url):
    result = urlsplit(url)
    if not result.scheme or not result.netloc:
        return False

    try:
        result.port
    except Exception:
        return False

    if result.port:
        try:
            int(result.port)
        except ValueError:
            # raise ValueError("Port could not be cast to integer value as '{}'".format(result.port))
            return False

    if result.path.startswith("//"):
        return False

    if "//" in result.path[1:]:
        return False

    return True


if __name__ == '__main__':
    print(is_url("http://example.com:wrongport"))


