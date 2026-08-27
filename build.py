#!/usr/bin/env python3
"""
Regenera index.html a partir de template.html + base_data.json.

Usar esto solo si en el futuro cambian los datos base (por ejemplo, una
nueva version completa de la hoja de ruta) o si alguien edita template.html
directamente. Para el uso normal del dashboard (subir archivos nuevos,
filtrar, calcular tiempos, etc.) NO hace falta tocar esto: eso ya funciona
dentro del propio index.html, desde el navegador, con Firebase.

Uso:
    cd source
    python3 build.py

Esto sobreescribe ../index.html con la version actualizada.
"""
import pathlib

HERE = pathlib.Path(__file__).parent
template = (HERE / "template.html").read_text(encoding="utf-8")
base_data = (HERE / "base_data.json").read_text(encoding="utf-8")

if "__BASE_DATA_JSON__" not in template:
    raise SystemExit("template.html no tiene el marcador __BASE_DATA_JSON__ — revisa el archivo.")

output = template.replace("__BASE_DATA_JSON__", base_data)
out_path = HERE.parent / "index.html"
out_path.write_text(output, encoding="utf-8")
print(f"OK: {out_path} regenerado ({len(output):,} caracteres)")
