from urllib import parse

valid_urls = [
	'http://softuni.bg/',
	'https://softuni.bg:447/search?Query=pesho&Users=true#go',
	'http://mysite.com:80/demo/index.aspx',
	'https://my-site.bg',
	'https://mysite.bg/demo/search?id=22o#go'
]

invalid_urls = [
	'http://google:443/',
	'https://mysite:80/demo/index.aspx',
	'somesite.com:80/search?',
	'https/mysite.bg?id=2'
]


def get_protocol(scheme):
	if scheme in ('http', 'https'):
		return scheme


def get_netloc(netloc, scheme):
	if '.' not in netloc:
		return None, None
	if ':' not in netloc:
		default_port = 80 if scheme == 'http' else 443
		netloc = f'{netloc}:{default_port}'
	return netloc.split(':')


def get_path(path):
	return path or '/'


def get_query(query):
	return query


def get_fragment(fragment):
	return fragment


def validate_url(url):
	components = parse.urlparse(url)
	protocol = get_protocol(components.scheme)
	host, port = get_netloc(components.netloc, components.scheme)
	path = get_path(components.path)
	query = get_query(components.query)
	fragment = get_fragment(components.fragment)
	if not (protocol and host and port):
		return 'Invalid URL'
	result = f"""Protocol: {protocol}
Host: {host}
Port: {port}
Path: {path}"""
	if query:
		result += f'\nQuery: {query}'
	if fragment:
		result += f'\nFragment: {fragment}'

	return result


[print(validate_url(url)) for url in valid_urls]
[print(validate_url(url)) for url in invalid_urls]
