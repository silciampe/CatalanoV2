from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import csv, io
from CatalanoBackend.models import MotoParte, AgroParte



@method_decorator(csrf_exempt, name='dispatch')
class ImportarMotopartes(View):
    def post (self, request):
        archivo = request.FILES['file']
        str_file = io.StringIO(archivo.read().decode('utf-8'), newline='\n')
        #file_extension = pathlib.Path(file.name).suffix

        #TODO: agregar static/imagenes/motopartes a las imagenes


        filereader = csv.reader(str_file)
        for linea in filereader:
            if linea[0] == 'DISCOS Y CUCHILLAS':
                
              agroparte = AgroParte.objects.filter(id_catalano=linea[2])
              if agroparte.exists():
                  agroparte.update(
                      grupo=self.sanitize_data(linea[0]),
                      modelo=self.sanitize_data(linea[1]),
                      diametro_exterior=self.sanitize_data(linea[3]),
                      espesor_mm=self.sanitize_data(linea[4]),
                      diametro_interior=self.sanitize_data(linea[5]),
                      cantidad_agujero_x_diametro_agujero=self.sanitize_data(linea[6]),
                      rad_mm=self.sanitize_data(linea[7]),
                      observacion=self.sanitize_data(linea[8]),
                      marca=self.sanitize_data(linea[9]),
                      imagen=self.format_image_path(linea[10])
                  )
              else:
                  AgroParte.objects.create(
                      id_catalano=self.sanitize_data(linea[2]),
                      grupo=self.sanitize_data(linea[0]),
                      modelo=self.sanitize_data(linea[1]),
                      diametro_exterior=self.sanitize_data(linea[3]),
                      espesor_mm=self.sanitize_data(linea[4]),
                      diametro_interior=self.sanitize_data(linea[5]),
                      cantidad_agujero_x_diametro_agujero=self.sanitize_data(linea[6]),
                      rad_mm=self.sanitize_data(linea[7]),
                      observacion=self.sanitize_data(linea[8]),
                      marca=self.sanitize_data(linea[9]),
                      imagen=self.format_image_path(linea[10])
                  )
            elif linea[0] == 'MEDIAS LLANTAS': 
              agroparte = AgroParte.objects.filter(id_catalano=linea[2])
              if agroparte.exists():
                  agroparte.update(
                      grupo=self.sanitize_data(linea[0]),
                      modelo=self.sanitize_data(linea[1]),
                      medida_cub=self.sanitize_data(linea[3]) + ' ' + self.sanitize_data(linea[4]) ,
                      diametro_interior=self.sanitize_data(linea[5]),
                      diametro_exterior=self.sanitize_data(linea[6]),
                      cantidad_agujero_x_diametro_agujero=self.sanitize_data(linea[7]),
                      marca=self.sanitize_data(linea[8]),
                      espesor_mm=self.sanitize_data(linea[9]),
                      imagen=self.format_image_path(linea[10])
                  )
              else:
                AgroParte.objects.create(
                    id_catalano=self.sanitize_data(linea[2]),
                    grupo=self.sanitize_data(linea[0]),
                    modelo=self.sanitize_data(linea[1]),
                    medida_cub=self.sanitize_data(linea[3]) + ' ' + self.sanitize_data(linea[4]) ,
                    diametro_interior=self.sanitize_data(linea[5]),
                    diametro_exterior=self.sanitize_data(linea[6]),
                    cantidad_agujero_x_diametro_agujero=self.sanitize_data(linea[7]),
                    marca=self.sanitize_data(linea[8]),
                    espesor_mm=self.sanitize_data(linea[9]),
                    imagen=self.format_image_path(linea[10])
                )
            elif linea[0] == 'DISCOS DENTADOS ORIGINALES':
              agroparte = AgroParte.objects.filter(id_catalano=linea[2])
              if agroparte.exists():
                  agroparte.update(
                      grupo=self.sanitize_data(linea[0]),
                      modelo=self.sanitize_data(linea[1]),
                      dientes=self.sanitize_data(linea[3]),
                      diametro_interior=self.sanitize_data(linea[4]),
                      imagen=self.format_image_path(linea[5])
                  )
              else:
                AgroParte.objects.create(
                    id_catalano=self.sanitize_data(linea[2]),
                    grupo=self.sanitize_data(linea[0]),
                    modelo=self.sanitize_data(linea[1]),
                    dientes=self.sanitize_data(linea[3]),
                    diametro_interior=self.sanitize_data(linea[4]),
                    imagen=self.format_image_path(linea[5])
                )


        #TODO: chequear las imagenes que no existen

        return JsonResponse(dict(success=True, message=f"File {archivo.name} uploaded successfully"))
    
    def sanitize_data(self, data):
        return data.strip().strip('"', '')
    
    def format_image_path(self, image):
        image = self.sanitize_data(image)
        return f"static/imagenes/agropartes/{image}"

