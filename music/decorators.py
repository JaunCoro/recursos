from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        title = args[0].request.data.get("title", "")
        artist = args[0].request.data.get("artist", "")
        if not title and not artist:
            return Response(
                data={
                    "message": "Both title and artist are required to add a song"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated

def validate_categoria_data(fn):
    def decorated(*args, **kwargs):
        name = args[0].request.data.get("name", "")
        if not name:
            return Response(
                data={
                    "message": "name is required to add a category"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated

def validate_material_data(fn):
    def decorated(*args, **kwargs):
        name = args[0].request.data.get("name", "")
        categoria = args[0].request.data.get("categoria", "")
        disponibilidad = args[0].request.data.get("disponibilidad", "")
        img = args[0].request.data.get("img", "")
        if not name and not categoria and not img:
            return Response(
                data={
                    "message": "name, categoria and img are required to add a material"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated

def validate_request(fn):
    def decorated(*args, **kwargs):
        user = args[0].request.data.get("user", "")
        material = args[0].request.data.get("material", "")
        if not user and not material:
            return Response(
                data={
                    "message": "user and material are required to add a material"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated