import csv

from cride.circles.models.circles import Circle

def import_data(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Busca un registro existente con el mismo 'slug_name'
                circle, created = Circle.objects.get_or_create(
                    name=row['name'],
                    defaults={
                        'slug_name': row['slug_name'],
                    }
                )

                # Actualiza los campos is_public y verified de acuerdo a los valores 1 o 0
                circle.slug_name = row['slug_name']
                circle.is_public = int(row['is_public']) == 1
                circle.verified = int(row['verified']) == 1
                circle.members_limit = row['members_limit']

                circle.save()
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al importar los datos: {str(e)}")

# Llama a la función para importar los datos desde el CSV
import_data('circles.csv')