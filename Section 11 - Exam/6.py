def build_query_string(params):
    url_address = [f'{key}={value}' for key, value in params.items()]
    return '&'.join(sorted(url_address))


print(build_query_string({'name': 'timur', 'age': 28}))
