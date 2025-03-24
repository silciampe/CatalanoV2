from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import csv, io
from CatalanoBackend.models import MotoParte, AgroParte, Cliente
from django.contrib.auth.models import User
from CatalanoBackend.utils import Utils
import datetime
from django.core.files.storage import default_storage



@method_decorator(csrf_exempt, name='dispatch')
class ImportarAgropartes(View):
    def post (self, request):
        archivo = request.FILES['file']
        str_file = io.StringIO(archivo.read().decode('latin-1'), newline='\n')
        carpeta = 'agropartes'
        ids = []
        agropartes_existentes = None
        errores = []
        warnings = []
        nuevos = 0
        actualizados = 0
        eliminados = 0

        try:
            filereader = csv.reader(str_file)
            for linea in filereader:
                try:
                    #skip empty lines
                    if len(linea) == 0:
                        continue
                    if agropartes_existentes is None:
                        if linea[0] == 'MEDIAS LLANTAS':
                            #el archivo viene 'MEDIAS LLANTAS' pero en grupo y modelo se guarda 'MEDIA LLANTA NATURAL'
                            grupo = 'MEDIA LLANTA NATURAL' 
                        else:
                            grupo = Utils.sanitize_data(linea[0])
                        agropartes_existentes = AgroParte.objects.filter(grupo=grupo)
                    ids.append(Utils.sanitize_data(linea[2]))
                    if linea[0] == 'DISCOS Y CUCHILLAS' or linea[0] == 'DISCOS DE RASTRA':
                        imagen = Utils.format_image_path(carpeta, linea[10])
                        id_catalano = Utils.sanitize_data(linea[2])
                        if not default_storage.exists(imagen):
                            warnings.append(f"Imagen no encontrada: {imagen} para el item {id_catalano}")
                        
                        agroparte = AgroParte.objects.filter(id_catalano=id_catalano)
                        if agroparte.exists():
                            agroparte[0].imagen.field.storage.exists(imagen)
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
                                imagen=imagen
                            )
                            actualizados += 1
                        else:
                            AgroParte.objects.create(
                                id_catalano=id_catalano,
                                grupo=Utils.sanitize_data(linea[0]),
                                modelo=Utils.sanitize_data(linea[1]),
                                diametro_exterior=Utils.sanitize_data(linea[3]),
                                espesor_mm=Utils.sanitize_data(linea[4]),
                                diametro_interior=Utils.sanitize_data(linea[5]),
                                cantidad_agujero_x_diametro_agujero=Utils.sanitize_data(linea[6]),
                                rad_mm=Utils.sanitize_data(linea[7]),
                                observacion=Utils.sanitize_data(linea[8]),
                                marca=Utils.sanitize_data(linea[9]),
                                imagen=imagen
                            )
                            nuevos += 1
                    elif linea[0] == 'MEDIAS LLANTAS':
                        #el archivo viene 'MEDIAS LLANTAS' pero en grupo y modelo se guarda 'MEDIA LLANTA NATURAL'
                        grupo = 'MEDIA LLANTA NATURAL' 
                        imagen = Utils.format_image_path(carpeta, linea[10])
                        id_catalano = Utils.sanitize_data(linea[2])
                        if not default_storage.exists(imagen):
                            warnings.append(f"Imagen no encontrada: {imagen} para el item {id_catalano}")
                        agroparte = AgroParte.objects.filter(id_catalano=id_catalano)
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
                                imagen=imagen
                            )
                            actualizados += 1
                        else:
                            AgroParte.objects.create(
                                id_catalano=id_catalano,
                                grupo=grupo,
                                modelo=grupo,
                                medida_cub=Utils.sanitize_data(linea[3]) + ' ' + Utils.sanitize_data(linea[4]) ,
                                diametro_interior=Utils.sanitize_data(linea[5]),
                                diametro_exterior=Utils.sanitize_data(linea[6]),
                                cantidad_agujero_x_diametro_agujero=Utils.sanitize_data(linea[7]),
                                marca=Utils.sanitize_data(linea[8]),
                                espesor_mm=Utils.sanitize_data(linea[9]),
                                imagen=imagen
                            )
                            nuevos += 1
                    elif linea[0] == 'DISCOS DENTADOS ORIGINALES':
                        imagen = Utils.format_image_path(carpeta, linea[5])
                        id_catalano = Utils.sanitize_data(linea[2])
                        if not default_storage.exists(imagen):
                            warnings.append(f"Imagen no encontrada: {imagen} para el item {id_catalano}")
                        agroparte = AgroParte.objects.filter(id_catalano=id_catalano)
                        if agroparte.exists():
                            agroparte.update(
                                grupo=Utils.sanitize_data(linea[0]),
                                modelo=Utils.sanitize_data(linea[1]),
                                dientes=Utils.sanitize_data(linea[3]),
                                diametro_interior=Utils.sanitize_data(linea[4]),
                                imagen=imagen
                            )
                            actualizados += 1
                        else:
                            AgroParte.objects.create(
                                id_catalano=id_catalano,
                                grupo=Utils.sanitize_data(linea[0]),
                                modelo=Utils.sanitize_data(linea[1]),
                                dientes=Utils.sanitize_data(linea[3]),
                                diametro_interior=Utils.sanitize_data(linea[4]),
                                imagen=imagen
                            )
                            nuevos += 1
                
                except Exception as e:
                    errores.append(f"Error al importar {linea[2]} - {str(e)}")
            
            #need to check which ids from agropartes_existentes are not in the ids list, so we can delete them
            for agroparte in agropartes_existentes:
                if agroparte.id_catalano not in ids:
                    agroparte.delete()
                    eliminados += 1


            #TODO: chequear las imagenes que no existen
            mensaje=f"{archivo.name} se importo correctamente. Nuevos: {nuevos}, Actualizados: {actualizados}, Eliminados: {eliminados}"
            if len(errores) > 0:
                mensaje += f", Errores: {errores}"
            return JsonResponse(dict(success=True, message=mensaje, warnings=warnings))
    
        except Exception as e:
            return JsonResponse(dict(success=False, message=str(e)))
    
    
@method_decorator(csrf_exempt, name='dispatch')
class ImportarMotopartes(View):
    def post (self, request):
        archivo = request.FILES['file']
        str_file = io.StringIO(archivo.read().decode('latin-1'), newline='\n')
        carpeta = 'motopartes'
        errores = []
        warnings = []
        nuevos = 0
        actualizados = 0
        eliminados = 0
        ids = []
        motopartes_existentes = None

        try:
            filereader = csv.reader(str_file)
            for linea in filereader:
                try:
                    if len(linea) == 0:
                        continue 
                    if motopartes_existentes is None:
                        if linea[0] == 'CORONAS':
                            #el archivo viene 'MEDIAS LLANTAS' pero en grupo y modelo se guarda 'MEDIA LLANTA NATURAL'
                            grupo = 'CORONA' 
                        else:
                            grupo = Utils.sanitize_data(linea[0])
                        motopartes_existentes = AgroParte.objects.filter(grupo=grupo)
                    id_catalano = Utils.sanitize_data(linea[1])
                    ids.append(Utils.sanitize_data(id_catalano))

                    if linea[0] == 'CORONAS':
                        linea[0] = 'CORONA'
                        if Utils.sanitize_data(linea[1]) == 'P/CONTROL':
                            continue

                        imagen = Utils.format_image_path(carpeta, linea[10])
                        if not default_storage.exists(imagen):
                            warnings.append(f"Imagen no encontrada: {imagen} para el item {id_catalano}")

                        motoparte = AgroParte.objects.filter(id_catalano=id_catalano)
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
                                imagen=imagen
                            )
                            actualizados += 1
                        else:
                            MotoParte.objects.create(
                                id_catalano=id_catalano,
                                grupo=Utils.sanitize_data(linea[0]),
                                marca=Utils.sanitize_data(linea[2]),
                                modelo=Utils.sanitize_data(linea[3]),
                                dientes=Utils.sanitize_data(linea[4]) if Utils.sanitize_data(linea[4]) != '' else 0,
                                cadena=Utils.sanitize_data(linea[5]),
                                diametro_interior=Utils.sanitize_data(linea[6]),
                                diametro_exterior=Utils.sanitize_data(linea[7]),
                                cantidad_agujero_x_diametro_agujero=Utils.sanitize_data(linea[8]),
                                codigo_original=Utils.sanitize_data(linea[9]),
                                imagen=imagen
                            )
                            nuevos += 1
                    elif linea[0] == 'PIÑONES':
                        linea[0] = 'PIÑON' 

                        imagen = Utils.format_image_path(carpeta, linea[12])
                        if not default_storage.exists(imagen):
                            warnings.append(f"Imagen no encontrada: {imagen} para el item {id_catalano}")

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
                                imagen=imagen
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
                                imagen=imagen
                            )
                            nuevos += 1
                except Exception as e:
                    errores.append(f"Error al importar {linea[1]} - {str(e)}")


            #need to check which ids from agropartes_existentes are not in the ids list, so we can delete them
            for motoparte in motopartes_existentes:
                if motoparte.id_catalano not in ids:
                    motoparte.delete()
                    eliminados += 1

            #TODO: chequear las imagenes que no existen

            mensaje=f"{archivo.name} se importo correctamente. Nuevos: {nuevos}, Actualizados: {actualizados}, Eliminados: {eliminados}"
            if len(errores) > 0:
                mensaje += f", Errores: {errores}"
            return JsonResponse(dict(success=True, message=mensaje, warnings=warnings))
            
        except Exception as e:
            return JsonResponse(dict(success=False, message=str(e))) 

@method_decorator(csrf_exempt, name='dispatch')
class ImportarClientes(View):
    def post (self, request):
        archivo = request.FILES['file']
        str_file = io.StringIO(archivo.read().decode('utf-8'), newline='\n')
        #str_file = io.StringIO(archivo.read().decode('latin-1'), newline='\n')
        errores = []
        nuevos = 0
        actualizados = 0
        ids = []
        clientes_existentes = None
        eliminados = 0

        try:
            
            filereader = csv.reader(str_file, delimiter='¦')
            for linea in filereader:
                try:
                    if len(linea) == 0:
                        continue
                    clientes_existentes = Cliente.objects.all()
                    ids.append(linea[0])

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

            #need to check which ids from agropartes_existentes are not in the ids list, so we can delete them
            for cliente in clientes_existentes:
                if not cliente.user.is_superuser and cliente.id_catalano not in ids:
                    cliente.user.delete()
                    cliente.delete()
                    eliminados += 1
            
            mensaje=f"{archivo.name} se importo correctamente. Nuevos: {nuevos}, Actualizados: {actualizados}, Eliminados: {eliminados}"
            if len(errores) > 0:
                mensaje += f", Errores: {errores}"
            return JsonResponse(dict(success=True, message=mensaje))
        
        except Exception as e:
            return JsonResponse(dict(success=False, message=str(e)))
