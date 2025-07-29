from city_functions import get_formatted_city_country

def test_city_country():
    """能够正确地处理像city country 这样的格式吗？"""
    formatted_name = get_formatted_city_country('Santiago','Chile')
    assert formatted_name == 'Santiago,Chile'

def test_city_country_population():
    """能够正确处理像city country population 这样的格式吗？"""
    formatted_name =get_formatted_city_country('santiago','chile',
                                               'population=500000')
    assert formatted_name == 'santiago,chile-population=500000'