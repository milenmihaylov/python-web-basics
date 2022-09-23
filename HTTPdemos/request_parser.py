def read_paths():
    END_COMMAND = 'END'

    paths = {
        'GET': [],
        'POST': []
    }

    while True:
        the_input = input()
        if the_input == END_COMMAND:
            break
        path = the_input[:the_input.rindex('/')]
        method = the_input[the_input.rindex('/') + 1:]
        paths[method.upper()].append(path)

    return paths


def read_request():
    method, path, _ = input().split()
    return {
        'method': method,
        'path': path
    }


def make_result(paths, request):
    valid_paths = paths[request['method']]
    if request['path'] in valid_paths:
        return """HTTP/1.1 200 OK
Content-Length: 2
Content-Type: text/plain

OK"""
    return """HTTP/1.1 404 Not Found
Content-Length: 9
Content-Type: text/plain

Not Found"""


def solve():
    paths = read_paths()
    print(paths)
    request = read_request()
    print(request)
    result = make_result(paths, request)
    print(result)


solve()
