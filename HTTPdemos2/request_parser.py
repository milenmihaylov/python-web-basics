def get_requests(requests=None):
	if requests:
		total_requests = requests
	else:
		total_requests = []
	request_input = input()
	if request_input == 'END':
		allowed_method = input()
		return total_requests, allowed_method
	_, path, method = request_input.split('/')
	total_requests.append((path, method))
	return get_requests(total_requests)


def return_response(paths, method: str):
	request_method, request_path, http = method.split()
	_, request_path = request_path.split('/')
	for p, m in paths:
		if request_method.lower() == m:
			if request_path == p:
				status_code = '200'
				status_text = 'OK'
				break
	else:
		status_code = "404"
		status_text = "Not Found"
	return f"""HTTP/1.1 {status_code} {status_text}
Content-Length: {len(status_text)}
Content-Type: text/plain

{status_text}"""


def solve():
	paths, method = get_requests()
	print(return_response(paths, method))


solve()
