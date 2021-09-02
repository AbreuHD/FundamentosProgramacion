Realiza un CRUD para registrar motores en el nuevo plan de seguridad. Al momento de registrar un motor debemos ingresar los siguientes campos:

1) Cédula (del chofer)
2) Nombre (del chofer)
3) Marca
4) Modelo
5) Placa
6) Chasis
7) Teléfono
8) Dirección
9) Lat (latitud de dirección donde vive el motor)
10) Lng (longitud de dirección donde vive el motor)
11) Actividad (Taxi, privado, Delivery, Etc).
12) Descripción (Como se ve el motor y que accesorios tiene)

El programa debe permitir agregar y editar los motores. 

Agregue la opción exportar, donde de alguna manera muestre un mapa con todos los motores registrado en su programa. Cuando haga click en un marcador.. debe mostrar los datos del motor. (al menos: marca, modelo, placa y nombre de a quien esta registrado)

Agregue la opción de exportar un motor para imprimir, donde se generara un documento HTML que tendrá el formato parecido a una licencia, pero con los datos que tenemos aqui. Si no sabe como son esos documentos averígüelo. Debe tener cierto parecido a las nuevas licencias de RD para motores... del lado donde salen los datos del motor. 

La base de datos a usar es SQLITE. Puedes hacerla usando un ORM o como LOS PROGRAMADORES DE VERDAD. 

Para los de software:  => El programa solo debe permitir registrar motos si la Lat y Lng son de República Dominicana si no lo hacen tendran el 50% del valor de la tarea.
