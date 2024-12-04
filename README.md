# HubUIDE

**HubUIDE** es un proyecto basado en el patrón arquitectónico **MVC** desarrollado en **Python** usando **Flet** para el frontend y **Firebase** para la autenticación y el backend.

## Tabla de Contenidos
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Dependencias](#dependencias)
- [Firebase](#configuración-de-firebase)
- [CI/CD con GitHub Actions](#cicd-con-github-actions)
- [Comandos importantes](#comandos-importantes)
- [Notas adicionales](#notas-adicionales)

---

## Requisitos previos
1. **Python 3.10+**: Se recomienda usar una versión reciente de Python.
2. **Node.js 18+**: Para utilizar Firebase CLI.
3. **Firebase CLI**: Instalado globalmente.
4. **Git**: Para control de versiones.
5. **GitHub Actions**: Configurado en el repositorio.
6. Acceso a una cuenta de Firebase con un proyecto configurado.

---

## Estructura del proyecto
El proyecto sigue el patrón **Modelo-Vista-Controlador (MVC)**:

```
HubUIDE/
├── app.py                  # Archivo principal del proyecto
├── firebase.json           # Configuración de Firebase Hosting
├── controllers/            # Lógica de negocio
│   ├── firebase_manager.py
│   ├── login_controller.py
│   └── user_controller.py
├── models/                 # Manejo de datos
│   ├── user_model.py
│   └── other_model.py
├── views/                  # Interfaces gráficas (Flet)
│   ├── login_view.py
│   ├── main_view.py
│   └── other_view.py
├── static/                 # Archivos estáticos (CSS, JS, imágenes)
├── templates/              # Plantillas HTML (si las usas)
└── README.md               # Documentación
```

---

## Dependencias

### Python
Las dependencias de Python se encuentran en el archivo `requirements.txt`. Si necesitas generarlo nuevamente, usa:
```bash
pip freeze > requirements.txt
```

Contenido del archivo `requirements.txt`:
```
flet==0.5.0  # Framework para la UI
pyrebase4    # Firebase para Python
firebase-admin  # SDK de Firebase para administrar servicios
```

### Node.js
Si utilizas Firebase Hosting, asegúrate de incluir un archivo `package.json` con las siguientes dependencias:
```json
{
  "dependencies": {
    "firebase-tools": "^12.4.7"  // CLI para desplegar en Firebase Hosting
  }
}
```

---

## Configuración de Firebase

1. **Inicializa Firebase Hosting** en tu proyecto:
   ```bash
   firebase init hosting
   ```

2. **Archivo `firebase.json`**:
   Asegúrate de que el archivo `firebase.json` apunte al directorio correcto con tus archivos estáticos:
   ```json
   {
     "hosting": {
       "public": "build",  // Cambia "build" si usas otro directorio
       "ignore": [
         "firebase.json",
         "**/.*",
         "**/node_modules/**"
       ]
     }
   }
   ```

3. **Configura el token de Firebase**:
   Obtén el token de Firebase ejecutando:
   ```bash
   firebase login:ci
   ```
   Guarda el token en **GitHub Secrets** con el nombre `FIREBASE_TOKEN`.

---

## CI/CD con GitHub Actions

Archivo `.github/workflows/deploy.yml` para CI/CD:

```yaml
name: Deploy to Firebase Hosting

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'

    - name: Install dependencies
      run: npm install

    - name: Install Firebase CLI
      run: npm install -g firebase-tools

    - name: Deploy to Firebase Hosting
      run: firebase deploy --only hosting
      env:
        FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}
```

---

## Comandos importantes

### Desplegar manualmente a Firebase Hosting
```bash
firebase deploy --only hosting
```

### Instalar dependencias
```bash
pip install -r requirements.txt
npm install
```

---

## Notas adicionales
- **Autenticación:** Usa `pyrebase4` para manejar la autenticación de usuarios.
- **Errores comunes:**
  - `firebase.json not found`: Asegúrate de que el archivo esté en el directorio raíz.
  - `EMAIL_EXISTS`: Indica que el correo ya está registrado.
- **DeprecationWarning de Node.js:** Actualiza tus dependencias para resolver advertencias.

--- 

Con este `README.md`, tendrás una guía detallada para configurar y desplegar tu proyecto correctamente.