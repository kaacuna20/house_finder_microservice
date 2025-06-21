# 🏠 House Finder Microservice

**House Finder Microservice** es una arquitectura de microservicios diseñada para gestionar y coordinar múltiples servicios relacionados con la búsqueda y gestión de propiedades. El sistema está compuesto por varios microservicios independientes que se comunican a través de un API Gateway centralizado, garantizando una estructura escalable, segura y mantenible.

---

## 📁 Estructura del Proyecto
```ini
house_finder_microservice/
├── proxy/             # proxy server
│   └── nginx.conf
│   └── Dockerfile
├── auth/              # Microservicio de autenticación y autorización
│   └── .env
│   └── app.py
│   └── requirements.txt
│   └── Dockerfile
│   └── src/
├── projects/          # Microservicio de gestión de proyectos de vivienda
│   └── .env
│   └── app.py
│   └── requirements.txt
│   └── Dockerfile
│   └── src/
├── scraping/          # Microservicio de scraping de datos
│   └── .env
│   └── app.py
│   └── requirements.txt
│   └── Dockerfile
│   └── src/
├── gateway/           # API Gateway central
│   └── .env
│   └── app.py
│   └── requirements.txt
│   └── Dockerfile
│   └── src/
├── docker-compose.yml # Archivo de orquestación de servicios
├── .env.example # .env global de ejemplo para el docker-compose
└── README.md          # Documentación del proyecto

```
---

## 🌐 API Gateway

El microservicio `gateway` actúa como el punto de entrada principal para todas las solicitudes externas. Sus responsabilidades clave incluyen:

### 🧭 Gestión de Rutas

Almacena una tabla de rutas en una base de datos **MongoDB**, donde cada documento define:

- `service`: Nombre del microservicio destino.
- `module`: Módulo específico dentro del servicio.
- `path`: Ruta del endpoint.
- `action`: Acción asociada para validación de permisos.
- `method`: Método HTTP correspondiente.

### 📝 Registro de Logs

Guarda un registro detallado de cada solicitud HTTP que se redirige a los microservicios, facilitando el monitoreo y la auditoría del sistema.

### 🔐 Middleware de Autenticación y Autorización

- **Autenticación**: Verifica la identidad del usuario mediante tokens o credenciales proporcionadas.
- **Autorización**: Determina si el usuario tiene los permisos necesarios, basándose en roles y acciones definidas en la tabla de rutas.

### 🔄 Servicio Proxy

Después de la validación, el proxy redirige las solicitudes al microservicio correspondiente según la información almacenada en la base de datos.

---

## 🛡️ Seguridad entre Microservicios

Para garantizar una comunicación segura dentro del ecosistema:

- **Restricción de Acceso**: Cada microservicio (`auth`, `projects`, `scraping`) implementa un middleware que permite únicamente solicitudes provenientes de la IP del contenedor del API Gateway.
  
- **Aislamiento de Servicios**: Se utiliza una red personalizada en Docker (`bridge` con IPs asignadas manualmente) para garantizar que los servicios no estén expuestos públicamente y solo sean accesibles a través del Gateway.

---

## 🛠️ Configuración y Despliegue

1. **Variables de Entorno**:  
   Cada microservicio contiene un archivo `.env` con sus configuraciones específicas (puertos, credenciales, nombres de bases de datos, etc).

2. **Orquestación con Docker Compose**:
   - Ejecuta el siguiente comando para construir y levantar todos los servicios:
     ```bash
     docker-compose up --build
     ```
   - Verifica que las IPs asignadas en `docker-compose.yml` coincidan con las reglas de acceso y dependencias establecidas en el código.

3. **Base de Datos MongoDB**:
   - Utilizada por el API Gateway para almacenar:
     - La tabla de rutas.
     - Los logs de las solicitudes HTTP.
   - Las credenciales y puertos se encuentran definidos en el archivo `.env`.

---

## 📌 Notas Adicionales

- Es fundamental mantener actualizada la **tabla de rutas** en MongoDB para reflejar cualquier cambio en los endpoints de los microservicios.
  
- La estructura modular del proyecto permite escalar fácilmente añadiendo nuevos servicios o funcionalidades sin comprometer la estabilidad del sistema.

---

> Desarrollado por [kaacuna20](https://github.com/kaacuna20)

