## Descripción
---
Este programa implementa una clase llamada `OdooActions` que facilita la interacción con una instancia de Odoo a través de XML-RPC en Python. Permite conectarse a una base de datos de Odoo y realizar operaciones como buscar registros, actualizarlos, crear nuevos registros y ejecutar métodos de modelos de Odoo de manera remota. Es útil para automatizar tareas de gestión de datos en Odoo desde un entorno Python, ofreciendo una interfaz sencilla y flexible para interactuar con la API XML-RPC de Odoo.

## Uso  
___
1. **Agregar credenciales**

La herramienta funciona por medio de los campos:
- username: Nombre de usuario en odoo 
- password: Contraseña del usuario en odoo
- db: Nombre de la base de datos a la que se va a conectar
- url: Url de la web (Ejemplo http://localhost:8069)

Estos estan disponibles en el archivo `__main__.py`

2. **Agregar logica en __main__.py**

Agregar logica a partir de la instancia  odoo = odoo_actions.OdooActions(url, db, username, password)

Ejemplo:
```python
record_id = odoo.search_record('res.users', [('name','=',"Alejandro Minor")])
```

[Ir a los Ejemplos de Uso](#ejemplos)

3. **Ejecutar**

	```shell
python3 odoo-python-xmlrpc-actions
	```

## Características y opciones
___
- Conexión a una instancia de Odoo a través de XML-RPC.
- Búsqueda de registros en un modelo.
- Actualización de registros en un modelo.
- Creación de nuevos registros en un modelo.
- Ejecución de métodos de un modelo.
- Leer datos de un registro.

  

## Ejemplos
---

**Buscar un registro:**

```python
domain = [('field_name', '=', 'value')]
record_id = odoo.search_record('res.partner', domain)
```

**Actualizar un registro:**

```python
record_id = 1  # ID del registro a actualizar
values = {'field_name': 'new_value'}
odoo.update_record('res.partner', record_id, values)

```


**Crear un nuevo registro:**

```python
values = {'field_name': 'value'}
new_record_id = odoo.create_record('res.partner', values)
```


**Ejecutar un método de un modelo:**

Para el caso que el metodo tenga varios argumentos, aparte de self. Cada arg seria un argumento, en este caso 2.

```python
method = 'method_name'
record_id = 1
arg1 = 'value1'
arg2 = 'value2'
context = {'context': {'active_id': 2}}
result = odoo.execute_model_method('res.partner', method, record_id, arg1, arg2, **context)
```


Para el caso que no requiera argumentos adicionales a self.

```python
method = 'method_name'
record_id = 1
context = {'context': {'active_id': 2}}
result = odoo.execute_model_method('res.partner', method, record_id, **context)
```
  

Para el caso que no requiera ni argumentos adicionales a self, ni contexto.

```python
method = 'method_name'
record_id = 1
result = odoo.execute_model_method('res.partner', method, record_id)
```


**Leer un registro:**

En este caso record estaria teniendo toda la información relacionda al registro.

```python
record_id = 1  # ID del registro a leer
record = odoo.read_record('res.partner', record_id)
```

  
## Requisitos
___
- Python 3.x
