from city_functions import get_formatted_city_country

def test_city_country():
    """能够正确地处理像city country 这样的格式吗？"""
    formatted_name = get_formatted_city_country('Santiago','Chile')
    assert formatted_name == 'Santiago Chile'