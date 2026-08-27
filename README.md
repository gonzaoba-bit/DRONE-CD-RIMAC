# Drone CD Rimac — Dashboard de reparto

Tablero de seguimiento de rutas de reparto para Lima, Perú: mapa interactivo,
filtros por ruta/viaje/distrito, carga de archivos Excel adicionales
sincronizada en vivo entre todos los que lo abren (vía Firebase), y una
pestaña de "Tiempos Reales" que calcula el tiempo honesto de cada ruta
considerando el tráfico real de Lima.

Es una aplicación de **un solo archivo HTML** (`index.html`). No necesita
build, servidor propio, ni instalar nada — corre entero en el navegador.

## 1. Subir esto a GitHub

**Opción rápida, sin usar git (desde el navegador):**

1. Entra a [github.com/new](https://github.com/new) y crea un repositorio
   (puede ser público o privado).
2. Dentro del repositorio recién creado, click en **"Add file" → "Upload files"**.
3. Arrastra el archivo `index.html` de esta carpeta (y este `README.md` si
   quieres).
4. Click en **"Commit changes"**.

**Si usas git desde la terminal:**

```bash
git init
git add index.html README.md
git commit -m "Dashboard Drone CD Rimac"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
git push -u origin main
```

## 2. Publicarlo como página web (opcional)

Si quieres que el dashboard tenga un link propio (en vez de abrir el
archivo localmente cada vez):

1. En el repositorio, ve a **Settings → Pages**.
2. En "Branch", elige `main` y la carpeta `/ (root)`.
3. Guarda. GitHub te da un link como
   `https://TU-USUARIO.github.io/TU-REPO/` (tarda uno o dos minutos en
   activarse).

Importante: `index.html` tiene que estar en la raíz del repositorio para
que esto funcione directamente (ya viene así en esta carpeta).

## 3. Sobre Firebase (sincronización en vivo)

El archivo ya trae la configuración de tu proyecto de Firebase integrada
(es la que me pasaste), así que la sincronización de archivos cargados
funciona apenas lo subas — no hay nada que configurar aparte.

Ten en cuenta que, al subir esto a un repositorio **público**, cualquiera
que vea el código podrá ver esa configuración de Firebase (el `apiKey`,
`projectId`, etc.). Esto es normal en aplicaciones web con Firebase — esa
clave no es secreta por sí sola — pero la seguridad real depende de las
**reglas de Firestore** de tu proyecto. Te recomiendo revisar, en la
consola de Firebase (Firestore Database → Reglas), que solo se permita
lectura/escritura a usuarios autenticados (aunque sea de forma anónima,
como ya lo hace este dashboard), para que nadie pueda borrar o modificar
los datos desde fuera del tablero. Si prefieres, puedo ayudarte a revisar
esas reglas.

Si el repositorio es **privado**, este punto no es un problema porque
nadie fuera de tu equipo puede ver el código de todos modos.

## 4. Contraseña de carga/borrado de archivos

Para adjuntar o eliminar una hoja de ruta desde el propio dashboard se pide
una contraseña (`ESPARTANO`). Está escrita directamente en el código como
un filtro simple para evitar cambios accidentales, no es una medida de
seguridad fuerte — cualquiera con acceso al código fuente puede verla.

## 5. Carpeta `source/` (opcional — solo si cambian los datos base)

Esta carpeta no hace falta para que el dashboard funcione; es solo por si
en el futuro necesitas regenerar `index.html` a partir de una nueva hoja de
ruta completa (no un archivo adicional — eso ya se sube desde el propio
tablero):

- `template.html` — la plantilla con todo el código, sin los datos.
- `base_data.json` — los 1,410 registros base ya procesados.
- `build.py` — script que junta ambos y genera `index.html`.

Uso: `cd source && python3 build.py`.
