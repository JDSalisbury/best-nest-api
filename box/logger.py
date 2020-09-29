from rest_framework import status
from rest_framework.response import Response


def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize()
                           for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )


def handle_errors(f):
    def w(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:

            err = '{0}'.format(e)

            if err == "{'email': [ErrorDetail(string=' Email already in use! ', code='unique')]}":
                return Response("User may already be created, Emails must be unique.", status=status.HTTP_400_BAD_REQUEST)

            return Response(err, status=status.HTTP_400_BAD_REQUEST)
    return w
