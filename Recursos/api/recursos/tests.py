from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from recursos.models import Materiales
from recursos.serializers import MaterialesSerializer

class BaseViewTest(APITestCase):
    client = APIClient

    @staticmethod
    def createMaterial(name="",categoria=""):
        if name != "" and categoria != "":
            Materiales.objects.create(name=name,categoria=categoria)

    def setUP(self):
        self.createMaterial('Canon EOS Rebel T6', 'Camara')
        self.createMaterial('Blue Micrófono Usb Yeti', 'Sonido')
        self.createMaterial('Cooled HPL 1600/200', 'Iluminacion')

class GetAllMaaterial(BaseViewTest):
    def test_get_all_material(self):
        response = self.client.get(
            reverse("material-all", kwargs={"version":"v1"})
        )

        expected = Materiales.objects.all()
        serialized = MaterialesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)