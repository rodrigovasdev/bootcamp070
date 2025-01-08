from django.shortcuts import render, redirect
#from .forms import EmpleadoForm
from .models import Empleado
# Crear Empleados
def insertar_emp(request):
    if request.method == "POST":
        emp_id = request.POST['emp_id']
        emp_nombre = request.POST['emp_nombre'] 
        emp_correo = request.POST['emp_correo']
        emp_designacion = request.POST['emp_designacion']
        empleado = Empleado(emp_id=emp_id, emp_nombre=emp_nombre,emp_correo=emp_correo,emp_designacion= emp_designacion)
        empleado.save()
        return redirect('/crud/')
    else:
        return render(request, 'crudapp/insertar.html')

# obtener los Empleados
def mostrar_emp(request):
    empleados = Empleado.objects.all()
    return render(request, 'crudapp/mostrar.html', {'empleados': empleados})
# Editar Empleados
def editar_emp(request,pk):
    empleado = Empleado.objects.get(id=pk)
    context = {'empleado': empleado,}
    return render(request=request, template_name='crudapp/editar.html',context=context)

def actualizarempleado(request, id):
    emp_id = request.POST['emp_id']
    emp_nombre = request.POST['emp_nombre']
    emp_correo = request.POST['emp_correo']
    emp_designacion = request.POST['emp_designacion']
    empleado = Empleado.objects.get(id=id)
    empleado.emp_id = emp_id
    empleado.emp_nombre = emp_nombre
    empleado.emp_correo = emp_correo
    empleado.emp_designacion = emp_designacion
    empleado.save()
    return redirect('/crud/')
# Eliminar Empleados
def eliminar_emp(request,pk):
    empleado = Empleado.objects.get(id=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('/crud/')
    context = {
    'empleado': empleado,
    }
    return render(request, 'crudapp/eliminar.html', context)
