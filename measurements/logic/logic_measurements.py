from django.db.models.expressions import Value
from variables.models import Variable
from ..models import Measurement

#Consultar la lista de medidas
def get_all_measurements():
    variables = Measurement.objects.all()
    return variables

#Obtener una medida dado su identificador
def get_measurement(id):
    variable = []
    try:
        variable.append(Measurement.objects.get(pk = id))
    except Exception:
        pass
    return variable

#Eliminar una medida dado su identificador
def delete_measurement(id):
    Measurement.objects.delete(pk = id)

#Cambiar una medida dado su identificador
def update_measurement(id, newVariable, newValue, newUnit, newPlace, newDateTime):
    measurement = Measurement.objects.filter(pk = id)
    measurement.update(variable = newVariable, value = newValue, unit = newUnit, place = newPlace, dateTime = newDateTime)
    