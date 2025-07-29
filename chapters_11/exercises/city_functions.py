def get_formatted_city_country(city,country,population=''):
    """返回格式化的城市和国家"""
    if population:
        formatted_name = f"{city},{country}-{population}"
    else:
        formatted_name = f"{city},{country}"
    return formatted_name