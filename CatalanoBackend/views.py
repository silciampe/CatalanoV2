from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import csv, io
from CatalanoBackend.models import MotoParte, AgroParte, Cliente
from django.contrib.auth.models import User
from CatalanoBackend.utils import Utils
import datetime


@method_decorator(csrf_exempt, name='dispatch')
class ImportarAgropartes(View):
    def post (self, request):
        archivo = request.FILES['file']
        str_file = io.StringIO(archivo.read().decode('latin-1'), newline='\n')
        #file_extension = pathlib.Path(file.name).suffix
        carpeta = 'agropartes'
        errores = []
        nuevos = 0
        actualizados = 0

        try:
            filereader = csv.reader(str_file)
            for linea in filereader:
                try:
                    if linea[0] == 'DISCOS Y CUCHILLAS' or linea[0] == 'DISCOS DE RASTRA':
                        
                        agroparte = AgroParte.objects.filter(id_catalano=Utils.sanitize_data(linea[2]))
                        if agroparte.exists():
                            agroparte.update(
                                grupo=Utils.sanitize_data(linea[0]),
                                modelo=Utils.sanitize_data(linea[1]),
                                diametro_exterior=Utils.sanitize_data(linea[3]),
                                espesor_mm=Utils.sanitize_data(linea[4]),
                                diametro_interior=Utils.sanitize_data(linea[5]),
                                cantidad_agujero_x_diametro_agujero=Utils.sanitize_data(linea[6]),
                                rad_mm=Utils.sanitize_data(linea[7]),
                                observacion=Utils.sanitize_data(linea[8]),
                                marca=Utils.sanitize_data(linea[9]),
                                imagen=Utils.format_image_path(carpeta, linea[10])
                            )
                            actualizados += 1
                        else:
                            AgroParte.objects.create(
                                id_catalano=Utils.sanitize_data(linea[2]),
                                grupo=Utils.sanitize_data(linea[0]),
                                modelo=Utils.sanitize_data(linea[1]),
                                diametro_exterior=Utils.sanitize_data(linea[3]),
                                espesor_mm=Utils.sanitize_data(linea[4]),
                                diametro_interior=Utils.sanitize_data(linea[5]),
                                cantidad_agujero_x_diametro_agujero=Utils.sanitize_data(linea[6]),
                                rad_mm=Utils.sanitize_data(linea[7]),
                                observacion=Utils.sanitize_data(linea[8]),
                                marca=Utils.sanitize_data(linea[9]),
                                imagen=Utils.format_image_path(carpeta, linea[10])
                            )
                            nuevos += 1
                    elif linea[0] == 'MEDIAS LLANTAS':
                        #el archivo viene 'MEDIAS LLANTAS' pero en grupo y modelo se guarda 'MEDIA LLANTA NATURAL'
                        grupo = 'MEDIA LLANTA NATURAL' 
                        agroparte = AgroParte.objects.filter(id_catalano=Utils.sanitize_data(linea[2]))
                        if agroparte.exists():
                            agroparte.update(
                                grupo=grupo,
                                modelo=grupo,
                                medida_cub=Utils.sanitize_data(linea[3]) + ' ' + Utils.sanitize_data(linea[4]) ,
                                diametro_interior=Utils.sanitize_data(linea[5]),
                                diametro_exterior=Utils.sanitize_data(linea[6]),
                                cantidad_agujero_x_diametro_agujero=Utils.sanitize_data(linea[7]),
                                marca=Utils.sanitize_data(linea[8]),
                                espesor_mm=Utils.sanitize_data(linea[9]),
                                imagen=Utils.format_image_path(carpeta, linea[10])
                            )
                            actualizados += 1
                        else:
                            AgroParte.objects.create(
                                id_catalano=Utils.sanitize_data(linea[2]),
                                grupo=grupo,
                                modelo=grupo,
                                medida_cub=Utils.sanitize_data(linea[3]) + ' ' + Utils.sanitize_data(linea[4]) ,
                                diametro_interior=Utils.sanitize_data(linea[5]),
                                diametro_exterior=Utils.sanitize_data(linea[6]),
                                cantidad_agujero_x_diametro_agujero=Utils.sanitize_data(linea[7]),
                                marca=Utils.sanitize_data(linea[8]),
                                espesor_mm=Utils.sanitize_data(linea[9]),
                                imagen=Utils.format_image_path(carpeta, linea[10])
                            )
                            nuevos += 1
                    elif linea[0] == 'DISCOS DENTADOS ORIGINALES':
                        agroparte = AgroParte.objects.filter(id_catalano=Utils.sanitize_data(linea[2]))
                        if agroparte.exists():
                            agroparte.update(
                                grupo=Utils.sanitize_data(linea[0]),
                                modelo=Utils.sanitize_data(linea[1]),
                                dientes=Utils.sanitize_data(linea[3]),
                                diametro_interior=Utils.sanitize_data(linea[4]),
                                imagen=Utils.format_image_path(carpeta, linea[5])
                            )
                            actualizados += 1
                        else:
                            AgroParte.objects.create(
                                id_catalano=Utils.sanitize_data(linea[2]),
                                grupo=Utils.sanitize_data(linea[0]),
                                modelo=Utils.sanitize_data(linea[1]),
                                dientes=Utils.sanitize_data(linea[3]),
                                diametro_interior=Utils.sanitize_data(linea[4]),
                                imagen=Utils.format_image_path(carpeta, linea[5])
                            )
                            nuevos += 1
                
                except Exception as e:
                    errores.append(f"Error al importar {linea[2]} - {str(e)}")
            
            #TODO: chequear las imagenes que no existen
            mensaje=f"{archivo.name} se importo correctamente. Nuevos: {nuevos}, Actualizados: {actualizados}"
            if len(errores) > 0:
                mensaje += f", Errores: {errores}"
            return JsonResponse(dict(success=True, message=mensaje))
    
        except Exception as e:
            return JsonResponse(dict(success=False, message=str(e)))
    
    
@method_decorator(csrf_exempt, name='dispatch')
class ImportarMotopartes(View):
    def post (self, request):
        archivo = request.FILES['file']
        str_file = io.StringIO(archivo.read().decode('latin-1'), newline='\n')
        carpeta = 'motopartes'
        errores = []
        nuevos = 0
        actualizados = 0

        try:
            filereader = csv.reader(str_file)
            for linea in filereader:
                try:
                    if linea[0] == 'CORONAS':
                        linea[0] = 'CORONA'
                        if Utils.sanitize_data(linea[1]) == 'P/CONTROL':
                            continue
                        motoparte = MotoParte.objects.filter(id_catalano=Utils.sanitize_data(linea[1]))
                        if motoparte.exists():
                            motoparte.update(
                                grupo=Utils.sanitize_data(linea[0]),
                                marca=Utils.sanitize_data(linea[2]),
                                modelo=Utils.sanitize_data(linea[3]),
                                dientes=Utils.sanitize_data(linea[4]) if Utils.sanitize_data(linea[4]) != '' else 0,
                                cadena=Utils.sanitize_data(linea[5]),
                                diametro_interior=Utils.sanitize_data(linea[6]),
                                diametro_exterior=Utils.sanitize_data(linea[7]),
                                cantidad_agujero_x_diametro_agujero=Utils.sanitize_data(linea[8]),
                                codigo_original=Utils.sanitize_data(linea[9]),
                                imagen=Utils.format_image_path(carpeta, linea[10])
                            )
                            actualizados += 1
                        else:
                            MotoParte.objects.create(
                                id_catalano=Utils.sanitize_data(linea[1]),
                                grupo=Utils.sanitize_data(linea[0]),
                                marca=Utils.sanitize_data(linea[2]),
                                modelo=Utils.sanitize_data(linea[3]),
                                dientes=Utils.sanitize_data(linea[4]) if Utils.sanitize_data(linea[4]) != '' else 0,
                                cadena=Utils.sanitize_data(linea[5]),
                                diametro_interior=Utils.sanitize_data(linea[6]),
                                diametro_exterior=Utils.sanitize_data(linea[7]),
                                cantidad_agujero_x_diametro_agujero=Utils.sanitize_data(linea[8]),
                                codigo_original=Utils.sanitize_data(linea[9]),
                                imagen=Utils.format_image_path(carpeta, linea[10])
                            )
                            nuevos += 1
                    elif linea[0] == 'PIÑONES':
                        linea[0] = 'PIÑON' 
                        motoparte = MotoParte.objects.filter(id_catalano=Utils.sanitize_data(linea[1]))
                        if motoparte.exists():
                            motoparte.update(
                                grupo=Utils.sanitize_data(linea[0]),
                                marca=Utils.sanitize_data(linea[2]),
                                modelo=Utils.sanitize_data(linea[3]),
                                dientes=Utils.sanitize_data(linea[4]) if Utils.sanitize_data(linea[4]) != '' else 0,
                                cadena=Utils.sanitize_data(linea[5]),
                                diametro_interior=Utils.sanitize_data(linea[6]),
                                diametro_exterior=Utils.sanitize_data(linea[7]),
                                diametro_rodillo=Utils.sanitize_data(linea[8]),
                                cantidad_estrias_x_tipo_rosca=Utils.sanitize_data(linea[9]),
                                cantidad_estrias_x_espesor_estrias=Utils.sanitize_data(linea[10]),
                                codigo_original=Utils.sanitize_data(linea[11]),
                                imagen=Utils.format_image_path(carpeta, linea[12])
                            )
                            actualizados += 1
                        else:
                            MotoParte.objects.create(
                                id_catalano=Utils.sanitize_data(Utils.sanitize_data(linea[1])),
                                grupo=Utils.sanitize_data(linea[0]),
                                marca=Utils.sanitize_data(linea[2]),
                                modelo=Utils.sanitize_data(linea[3]),
                                dientes=Utils.sanitize_data(linea[4]) if Utils.sanitize_data(linea[4]) != '' else 0,
                                cadena=Utils.sanitize_data(linea[5]),
                                diametro_interior=Utils.sanitize_data(linea[6]),
                                diametro_exterior=Utils.sanitize_data(linea[7]),
                                diametro_rodillo=Utils.sanitize_data(linea[8]),
                                cantidad_estrias_x_tipo_rosca=Utils.sanitize_data(linea[9]),
                                cantidad_estrias_x_espesor_estrias=Utils.sanitize_data(linea[10]),
                                codigo_original=Utils.sanitize_data(linea[11]),
                                imagen=Utils.format_image_path(carpeta, linea[12])
                            )
                            nuevos += 1
                except Exception as e:
                    errores.append(f"Error al importar {linea[1]} - {str(e)}")
            #TODO: chequear las imagenes que no existen

            mensaje=f"{archivo.name} se importo correctamente. Nuevos: {nuevos}, Actualizados: {actualizados}"
            if len(errores) > 0:
                mensaje += f", Errores: {errores}"
            return JsonResponse(dict(success=True, message=mensaje))
            
        except Exception as e:
            return JsonResponse(dict(success=False, message=str(e))) 

@method_decorator(csrf_exempt, name='dispatch')
class ImportarClientes(View):
    def post (self, request):
        archivo = request.FILES['file']
        str_file = io.StringIO(archivo.read().decode('latin-1'), newline='\n')
        errores = []
        nuevos = 0
        actualizados = 0

        try:
            
            filereader = csv.reader(str_file, delimiter='¦')
            for linea in filereader:
                try:
                    if len(linea) == 0:
                        continue
                    cliente = Cliente.objects.filter(id_catalano=linea[0])
                    puntos = 0
                    # tipo cliente 5 es Agro, 1 es Moto
                    if Utils.sanitize_data(linea[6]) == '5':
                        puntos = Utils.sanitize_data(linea[3])
                        tipo_cliente = Cliente.TIPO_CLIENTE[0][0]
                    else:
                        puntos = Utils.sanitize_data(linea[2])
                        tipo_cliente = Cliente.TIPO_CLIENTE[1][0]
                    if cliente.exists():
                        cliente.update(
                            razon_social=Utils.sanitize_data(linea[1]),
                            puntos=puntos,
                            cuit=Utils.sanitize_data(linea[4]),
                            # sample date is 16/12/24
                            fecha_actualizacion=datetime.datetime.strptime(linea[5], '%d/%m/%y'),
                            rubro=Utils.sanitize_data(linea[6]),
                            tipo_cliente=tipo_cliente
                        )
                        cliente[0].user.set_password(Utils.sanitize_data(linea[0]))
                        cliente[0].user.email = Utils.sanitize_data(linea[7])
                        cliente[0].user.save()
                        actualizados += 1
                    else:
                        user = User.objects.create_user(
                            username=Utils.sanitize_data(linea[4]),
                            email=Utils.sanitize_data(linea[7]),
                            password=Utils.sanitize_data(linea[0])
                        )
                        Cliente.objects.create(
                            id_catalano=Utils.sanitize_data(linea[0]),
                            razon_social=Utils.sanitize_data(linea[1]),
                            puntos=puntos,
                            cuit=Utils.sanitize_data(linea[4]),
                            fecha_actualizacion=datetime.datetime.strptime(linea[5], '%d/%m/%y'),
                            rubro=Utils.sanitize_data(linea[6]),
                            tipo_cliente=tipo_cliente,
                            user=user
                        )
                        nuevos += 1
                except Exception as e:
                    errores.append(f"Error al importar {linea[0]} - {str(e)}")
            mensaje=f"{archivo.name} se importo correctamente. Nuevos: {nuevos}, Actualizados: {actualizados}"
            if len(errores) > 0:
                mensaje += f", Errores: {errores}"
            return JsonResponse(dict(success=True, message=mensaje))
        
        except Exception as e:
            return JsonResponse(dict(success=False, message=str(e)))
