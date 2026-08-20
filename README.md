# Radar del Rechazo — CD Rímac

Panel de seguimiento de rechazos de pedidos para la operación de reparto (Distribución BK37 / CD Rímac). Es un dashboard HTML autocontenido (sin backend, sin dependencias que instalar) generado a partir de una exportación de "hoja de ruta" y un par de archivos de referencia estables.

## Contenido del repositorio

- `prep.py` — script en Python (pandas) que lee la exportación operativa (`HojaRuta_1.xls`) más los archivos de referencia estables (`zona_venta_BK37.xlsx` para supervisor/canal comercial por zona, y `MAESTRO_DE_CLIENTE_*.xlsx` para las coordenadas de los clientes) y produce `data.json`.
- `data.json` — datos ya procesados y embebidos que consume el panel (incluye datos reales de clientes: nombres, ubicaciones, motivos de rechazo, retroalimentación de agentes — **repositorio privado, uso interno**).
- `template.html` — el esqueleto HTML/CSS del panel, con dos marcadores (`__DATA_JSON__` y `__APP_JS__`) donde se insertan los datos y la lógica.
- `app.js` — toda la lógica del panel: filtros, agregaciones, gráficos (SVG hecho a mano, sin librerías de charts), el mapa de clientes (Leaflet + OpenStreetMap), exportación de tablas a Excel, y la carga acumulativa de archivos adicionales directamente en el navegador.
- `radar_del_rechazo.html` — el panel ya compilado (template + data.json + app.js en un solo archivo), listo para abrir en cualquier navegador.

## Pestañas del panel

1. **Resumen general** — evolución de MR (motivo de rechazo), rutas y empresas con más rechazos, mapa de calor por ruta/día, motivos principales.
2. **Seguimiento EDT** — seguimiento por empresa: score, mezcla completo/parcial, rutas, motivos, top clientes con retroalimentación.
3. **Seguimiento comercial** — score por supervisor, zonas de venta con más rechazos, clientes rechazados por zona (con motivo principal, retroalimentación y reincidencia).
4. **Reincidencia de clientes** — clientes con rechazos recurrentes, historial de incidencias, mapa de ubicación real (calles de Lima vía OpenStreetMap) y ranking de distritos con más rechazos.

Todas las pestañas comparten filtros por fecha (con accesos rápidos de mes/semana/día de la semana), empresa, supervisor, zona AC, distrito, canal, motivo y tipo de rechazo — cada pestaña mantiene su propio estado de filtros de forma independiente.

## Cómo regenerar el panel

Si cambia la fuente de datos (`HojaRuta_1.xls`) o alguno de los archivos de referencia, hay que:

1. Ajustar las rutas de los archivos de origen al inicio de `prep.py`.
2. Ejecutar `python3 prep.py` — esto regenera `data.json`.
3. Combinar los tres archivos en el HTML final:

```python
with open('template.html', 'r', encoding='utf-8') as f: tpl = f.read()
with open('data.json', 'r', encoding='utf-8') as f: data_json = f.read()
with open('app.js', 'r', encoding='utf-8') as f: app_js = f.read()
out = tpl.replace('__DATA_JSON__', data_json).replace('__APP_JS__', app_js)
with open('radar_del_rechazo.html', 'w', encoding='utf-8') as f: f.write(out)
```

El panel también permite cargar archivos adicionales directamente desde el navegador (botón "Agregar archivo"), que se suman a los datos originales sin necesidad de volver a ejecutar `prep.py`.

## Notas

- El mapa de la pestaña "Reincidencia de clientes" usa Leaflet + tiles de OpenStreetMap cargados desde internet al abrir el archivo — si no hay conexión, el resto del panel funciona igual y el mapa muestra un aviso.
- Este repositorio contiene datos reales de clientes (nombres, ubicaciones, motivos de rechazo, comentarios de agentes) — manténlo privado.
