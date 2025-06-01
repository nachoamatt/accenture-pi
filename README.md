# Proyecto Integrador - Data Engineering

Este proyecto simula un entorno profesional de análisis de datos de ventas para una empresa de comestibles.  
Fue desarrollado como parte del curso de Data Engineering, aplicando principios de programación orientada a objetos, diseño de arquitectura de software y carga de datos en una base relacional.

## 📁 Estructura del Proyecto

- `data/`: archivos `.csv` originales con los datos del negocio  
- `sql/`: scripts SQL para creación de tablas y carga de datos  
- `src/`: código fuente en Python, organizado en:
  - `models/`: clases que representan las entidades del sistema (POO)
  - `loaders/`: scripts para leer archivos CSV y mapearlos a objetos Python
  - `db/`: clase de conexión a base de datos usando SQLAlchemy
- `tests/`: pruebas unitarias con `pytest`  
- `.env`: variables de entorno (credenciales y parámetros de conexión)  
- `.gitignore`: exclusión de archivos innecesarios en el control de versiones  
- `requirements.txt`: dependencias del proyecto  

## ⚙️ Configuración del entorno

1. Crear entorno virtual:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Instalar dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## 🗄️ Base de Datos

### Creación de tablas

Ejecutar el siguiente script desde el monitor de MySQL:

```sql
source sql/schema.sql;
```

O desde la terminal:

```bash
mysql -u root supermercado < sql/schema.sql
```

### Carga de datos

Asegurarse de tener habilitado `local_infile` y luego ejecutar:

```bash
mysql --local-infile=1 -u root supermercado < sql/load_data.sql
```

## 🐍 Modelado en Python (POO)

Se crearon clases como `Category`, `Product`, `Customer`, `Employee`, etc., siguiendo los principios de programación orientada a objetos:

- Encapsulamiento  
- Uso de constructores  
- Métodos específicos del dominio (como `.apply_discount()` en `Product`)  
- Relaciones entre objetos (por ejemplo, un `Product` contiene una `Category` como atributo)

## 📥 Lectura de CSV y mapeo a objetos

Se implementaron loaders que:

- Leen los archivos `.csv` con `csv.DictReader`  
- Instancian objetos Python de cada clase  
- Asocian correctamente entidades (por ejemplo, `Product` ↔ `Category`)  

### Ejemplo de uso

```bash
PYTHONPATH=. python3 src/loaders/load_products.py
```

## 🔌 Conexión a la Base de Datos con SQLAlchemy

Se creó una clase `DatabaseConnector` en `src/db/connector.py`, que utiliza **SQLAlchemy** para establecer una conexión eficiente a la base de datos MySQL.

### Uso del patrón Singleton

La clase aplica el **patrón de diseño Singleton** para asegurar que toda la aplicación comparta la misma conexión.

#### Justificación

- **Eficiencia de recursos**: evita múltiples conexiones redundantes  
- **Consistencia**: asegura que todas las operaciones usen la misma instancia de engine  
- **Mantenimiento**: centraliza y simplifica la lógica de conexión  

### Variables de entorno (.env)

Las credenciales de la base se definen en el archivo `.env` y se cargan automáticamente con `python-dotenv`.

Ejemplo:

```
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
DB_NAME=supermercado
```

## 📊 Consultas desde Python

La clase `DatabaseConnector` expone una propiedad `.engine` para ejecutar queries con SQLAlchemy o pandas.  
(Más detalles en el notebook del avance 3.)

## 🧪 Pruebas unitarias

Se agregó un test de conexión en `tests/test_connection.py` que verifica si la instancia Singleton conecta correctamente a la base.

Ejecución:

```bash
PYTHONPATH=src python3 tests/test_connection.py
```

## ✅ Testing (Avance 1)

Se utilizan pruebas unitarias con `pytest`, cubriendo al menos una clase del modelo.  
(Ver `tests/test_product.py` próximamente)

## 🧠 Justificación técnica

Este enfoque modular permite:

- **Escalabilidad**: se pueden agregar nuevas entidades o fuentes de datos fácilmente  
- **Reutilización**: las clases del modelo pueden conectarse a una DB o usarse en análisis en memoria  
- **Mantenibilidad**: el código está limpio y desacoplado, lo que facilita futuras mejoras

## 👨‍💻 Autor

Ignacio Amatt