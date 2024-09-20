
# Configuración Básica de un Cluster de Airflow con CeleryExecutor, Redis y PostgreSQL

Este archivo `docker-compose.yml` configura un entorno local de Airflow con **CeleryExecutor** utilizando Redis como intermediario de mensajes y PostgreSQL como base de datos.

> **Advertencia:** Esta configuración está diseñada para **desarrollo local**. No se debe utilizar en un entorno de producción.

## Requisitos Previos

- Docker
- Docker Compose

## Variables de Entorno Soportadas

Este archivo soporta la configuración básica usando **variables de entorno** o un archivo `.env`. A continuación, se detallan las variables más importantes que puedes ajustar:

- `AIRFLOW_IMAGE_NAME`: Nombre de la imagen de Docker utilizada para ejecutar Airflow.  
  **Valor predeterminado**: `apache/airflow:2.10.0`
  
- `AIRFLOW_UID`: ID de usuario en los contenedores de Airflow.  
  **Valor predeterminado**: `50000`

- `AIRFLOW_PROJ_DIR`: Ruta base donde se montarán los volúmenes de archivos como DAGs, logs, plugins y configuraciones.  
  **Valor predeterminado**: `.`
  
- `_AIRFLOW_WWW_USER_USERNAME`: Nombre de usuario para la cuenta de administrador (si es necesario crearla).  
  **Valor predeterminado**: `airflow`
  
- `_AIRFLOW_WWW_USER_PASSWORD`: Contraseña para la cuenta de administrador (si es necesario crearla).  
  **Valor predeterminado**: `airflow`
  
- `_PIP_ADDITIONAL_REQUIREMENTS`: Requerimientos adicionales de PIP a instalar al iniciar los contenedores.  
  **Nota:** Utiliza esta opción solo para pruebas rápidas. Para instalaciones en producción, se recomienda construir una imagen personalizada.  
  **Valor predeterminado**: `''`

## Servicios Configurados

### 1. **PostgreSQL**

- Utilizado como base de datos de Airflow.
- Configuración predeterminada:
  - `POSTGRES_USER`: `airflow`
  - `POSTGRES_PASSWORD`: `airflow`
  - `POSTGRES_DB`: `airflow`
  
### 2. **Redis**

- Actúa como intermediario de mensajes para Celery.

### 3. **Airflow Webserver**

- El servidor web de Airflow, accesible en `http://localhost:8080`.
  
### 4. **Airflow Scheduler**

- Programa y monitorea la ejecución de las tareas en Airflow.

### 5. **Airflow Worker**

- Los trabajadores de Celery que ejecutan las tareas programadas.

### 6. **Airflow Triggerer**

- Servicio encargado de ejecutar eventos basados en disparadores.

### 7. **Airflow CLI**

- Puedes usar este servicio para ejecutar comandos de la interfaz de línea de comandos de Airflow.

## Volúmenes

Los siguientes directorios locales se montan en los contenedores:

- `dags`: Directorio donde almacenar tus DAGs.
- `logs`: Directorio para los logs de ejecución de Airflow.
- `plugins`: Directorio para agregar plugins personalizados.
- `config`: Directorio para agregar configuraciones personalizadas de Airflow.

## Instrucciones de Uso

### 1. Iniciar el entorno

Para iniciar el entorno de Airflow, simplemente ejecuta:

```bash
docker-compose up
```

### 2. Acceder a la interfaz web de Airflow

Una vez que el entorno esté iniciado, puedes acceder a la interfaz de Airflow desde tu navegador en `http://localhost:8080`. Utiliza el siguiente usuario y contraseña predeterminados:

- **Usuario**: `airflow`
- **Contraseña**: `airflow`

### 3. Parar el entorno

Para detener el entorno, usa el siguiente comando:

```bash
docker-compose down
```

### 4. Agregar dependencias adicionales

Si necesitas instalar paquetes adicionales de Python, puedes usar la variable `_PIP_ADDITIONAL_REQUIREMENTS` para añadirlos rápidamente. Sin embargo, es recomendable que, para configuraciones más permanentes, extiendas la imagen de Docker oficial de Airflow y construyas una imagen personalizada.

## Notas Finales

- Este entorno está pensado solo para **pruebas y desarrollo**. Si planeas usar Airflow en producción, asegúrate de seguir las **mejores prácticas de seguridad** y optimización de recursos.
- Si experimentas problemas con recursos insuficientes (memoria, CPU, espacio en disco), sigue las recomendaciones en la [documentación oficial de Airflow](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#before-you-begin).

