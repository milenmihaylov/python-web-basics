from urllib import parse

encoded_urls = [
	'http://www.google.bg/search?q=C%23',
	'https://mysite.com/show?n%40m3=+p3%24h0',
	'http://url-decoder.com/i%23de%25?id=23'
]

test_urls = [
	'http://www.google.bg/search?q=C#',
	'https://mysite.com/show?n@m3=+p3$h0',
	'http://url-decoder.com/i#de%?id=23'
]


def decode_url(url):
	return parse.unquote(url)


for i, url in enumerate(encoded_urls):
	decoded = decode_url(url)
	print('encoded url: ', url)
	print('decoded url: ', decoded)
	print('test url:    ', test_urls[i])
	print(decoded == test_urls[i])
