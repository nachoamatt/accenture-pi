# Proyecto Integrador - Data Engineering

Este proyecto simula un entorno profesional de análisis de datos de ventas para una empresa de comestibles.  
Fue desarrollado como parte del curso de Data Engineering, aplicando principios de programación orientada a objetos, diseño de arquitectura de software y carga de datos en una base relacional.

## 📁 Estructura del Proyecto

- `data/`:  
  Archivos `.csv` originales con los datos del negocio (countries, cities, customers, employees, categories, products, sales).  

- `sql/`:  
  Scripts SQL para:  
  - Creación de las tablas (`schema.sql`)  
  - Carga inicial de datos mediante comandos `LOAD DATA` (`load_data.sql`, aunque no se usa directamente en el código Python)  

- `src/`: Código fuente en Python, organizado en subcarpetas:  
  - `models/`: Clases que representan las entidades del sistema siguiendo POO.  
  - `loaders/`: Funciones para leer archivos CSV y mapearlos a objetos Python.  
  - `db/`: Clase de conexión a la base de datos usando SQLAlchemy, implementada con patrón Singleton para manejo eficiente.  
  - `ingestion/`: Scripts para insertar los datos en la base de datos, usando los loaders y el conector.  
  - `factories/`: Implementación del patrón Factory para creación de objetos modelo.  

- `tests/`: Pruebas unitarias con `pytest` que verifican funcionalidades de los modelos, loaders, y la conexión a la base de datos.  

- `.gitignore`: Archivo para excluir archivos y carpetas no deseados en el control de versiones (por ejemplo, `venv/`, `.env`).  

- `requirements.txt`: Archivo con las dependencias necesarias para ejecutar el proyecto (`sqlalchemy`, `pandas`, `python-dotenv`, `pytest`, etc.).  


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

La carga de datos se realiza mediante scripts Python ubicados en `src/ingestion/` que procesan y validan la información antes de insertarla en la base.

Estos scripts:

- Usan los loaders para leer los archivos CSV y crear objetos Python.
- Gestionan correctamente las relaciones entre entidades (por ejemplo, asignar la ciudad correcta a un cliente).
- Insertan los datos en la base usando SQLAlchemy para garantizar integridad y manejo eficiente.

#### Ejecución del script general de carga

Para automatizar la inserción de todos los datos en orden, se creó el script `run_all_inserts.py` en la carpeta `src/ingestion/`.

Ejecutar el script con:

```bash
python -m src.ingestion.run_all_inserts
```

El script realiza la carga secuencial de todas las entidades (countries, cities, customers, employees, categories, products y sales), mostrando en consola el estado de cada inserción y posibles errores.


## 🐍 Modelado en Python (POO)

Se crearon clases que representan las entidades del negocio, siguiendo principios de Programación Orientada a Objetos:

- **Encapsulamiento:** atributos privados y acceso controlado mediante métodos o propiedades.
- **Constructores:** para inicializar objetos con datos relevantes.
- **Métodos específicos:** como `apply_discount()` en `Product` o `full_name()` en `Customer`.
- **Relaciones:** objetos anidados, por ejemplo, un `Product` contiene una `Category`.

Esto facilita mantener el código limpio, escalable y con una representación fiel del dominio del problema.

## 📥 Lectura de CSV y mapeo a objetos

Los loaders:

- Usan `csv.DictReader` para leer archivos CSV.
- Crean instancias de las clases modelo con los datos leídos.
- Gestionan correctamente las relaciones entre entidades (por ejemplo, asignan la `Category` correcta a un `Product`).
- Permiten pruebas y manipulación previa a la inserción en base.

## 🔌 Conexión a la Base de Datos con SQLAlchemy

Se diseñó una clase `DatabaseConnector`:

- Implementa el **patrón Singleton** para mantener una única conexión activa.
- Usa `SQLAlchemy` para la conexión y ejecución eficiente de queries.
- Carga las credenciales desde un archivo `.env` mediante `python-dotenv`.
- Expone un método para ejecutar consultas y devolver resultados en formato `pandas.DataFrame`.

Esto permite centralizar la conexión y facilitar la integración con análisis y tests.

### Variables de entorno (.env)

Las credenciales de la base se definen en el archivo `.env` y se cargan automáticamente con `python-dotenv`.

Ejemplo:

```
DB_USER=xxxx
DB_PASSWORD=xxxx
DB_HOST=localhost
DB_PORT=xxxx
DB_NAME=supermercado
```

## 📊 Consultas desde Python

La clase `DatabaseConnector` incluye un método para ejecutar consultas SQL simples:

- Recibe una consulta SQL como string.
- Ejecuta la consulta usando la conexión activa.
- Devuelve los resultados como un DataFrame de pandas, facilitando el análisis y manipulación de datos.

Este enfoque permite integrar el acceso a la base de datos con las herramientas de análisis propias de Python, como pandas.

## 🧪 Pruebas unitarias

- Se implementaron pruebas unitarias con `pytest` para validar funcionalidades críticas.
- Por ejemplo, existe un test para verificar la correcta creación de instancias de modelos.
- Otro test asegura que la conexión a la base de datos funcione y se mantenga única (Singleton).
- Se prueba la correcta ejecución de queries y retorno de datos.

Las pruebas automatizadas facilitan mantener la calidad del código y evitar regresiones.

## 🧠 Justificación técnica

El diseño modular y orientado a objetos aplicado en este proyecto ofrece varias ventajas clave:

- **Escalabilidad**: Es sencillo agregar nuevas entidades, loaders o funcionalidades sin afectar el núcleo del sistema.
- **Reutilización**: Las clases modelo pueden usarse tanto para manipulación en memoria como para persistencia en base de datos.
- **Mantenibilidad**: La separación clara de responsabilidades permite detectar y corregir errores de forma ágil.
- **Eficiencia**: El patrón Singleton en la conexión evita overheads por múltiples conexiones simultáneas.
- **Flexibilidad**: La integración de loaders que generan objetos facilita el trabajo con diferentes fuentes de datos.

Este enfoque prepara la base para futuros desarrollos de análisis avanzados y pipelines de datos robustos.

## 👨‍💻 Autor

Ignacio Amatt