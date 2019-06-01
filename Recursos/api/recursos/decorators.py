from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        name = args[0].request.data.get("name", "")
        categoria = args[0].request.data.get("categoria", "")
        if not name and not categoria:
            return Response(
                data={
                    "message": "Both name and categoria are required to add a song"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated