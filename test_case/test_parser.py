import pytest
from myHttprunner.parser import is_url, parse_form_to_dict

valid_cases = [
    ("https://www.example.com", "Standard secure URL"),
    ("http://example.com", "Standard insecure URL"),
    ("https://example.org/test", "URL with path"),
    ("ftp://user:password@example.com/path", "FTP URL with credentials"),
    ("http://localhost", "Localhost URL"),
    ("http://127.0.0.1", "IPv4 URL"),
    ("http://[::1]", "IPv6 URL"),
    ("https://www.example.com:8080", "URL with custom port"),
    ("http://example.com/?query=param", "URL with query parameters"),
    ("http://example.com/?query=param&query1=param1", "URL with query parameters"),
]

invalid_cases = [
    ("example.com", "Missing scheme"),
    ("www.example.com", "Missing scheme"),
    ("not a url", "Invalid string"),
    ("http://", "Missing netloc"),
    ("https://", "Missing netloc"),
    ("://example.com", "Missing scheme"),
    ("http:///example.com", "Invalid scheme separator"),
    ("http://example.com:wrongport", "Invalid port"),
    ("http://example.com//", "Extra slash"),
]


@pytest.mark.parametrize("url, description", valid_cases)
def test_valid_urls(url, description):
    assert is_url(url), f"{description}: {url}"


@pytest.mark.parametrize("url, description", invalid_cases)
def test_invalid_urls(url, description):
    assert not is_url(url), f"{description}: {url}"


# Test data for successful test cases
success_test_data = [
    ("account=sunsinan&password=1", {"account": "sunsinan", "password": "1"}),
    ("https://example.com?account=sunsinan&password=1", {"account": "sunsinan", "password": "1"}),
    ("name=John%20Doe&age=30", {"name": "John Doe", "age": "30"}),
    ("https://example.com?name=John%20Doe&age=30", {"name": "John Doe", "age": "30"}),
]

# Test data for failure test cases
failure_test_data = [
    "account:sunsinan,password:1",
    "https://example.com?account:sunsinan,password:1",
    "{account: sunsinan, password: 1}",
]


# Successful test cases
@pytest.mark.parametrize("input_str,expected_output", success_test_data)
def test_parse_form_to_dict_success(input_str, expected_output):
    assert parse_form_to_dict(input_str) == expected_output


# Failure test cases
@pytest.mark.parametrize("input_str", failure_test_data)
def test_parse_form_to_dict_failure(input_str):
    assert parse_form_to_dict(input_str) != {}


if __name__ == '__main__':
    import os

    pytest.main([
        os.path.abspath(__file__),
        "-s",
        "-v",
        "--html=report.html"
    ])
