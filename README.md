# Arquitectura de Software (TB034, FIUBA)

Apunte de Arquitectura de Software (cátedra Calónico), un capítulo por clase.
Se arma con el motor compartido de la plataforma
([fiuba-resumenes/motor](https://github.com/fiuba-resumenes/motor)), del que
depende una versión fija (ver `requirements.txt`).

## Cómo se construye

```
fuentes/completo/<id>.html   capítulos del apunte (uno por clase)
fuentes/materia.py           identidad, paleta y agrupación (CFG)
```

```bash
pip install -r requirements.txt
python3 -m motor_apuntes.lint_fragmentos fuentes/completo
python3 armar.py
```

Se van sumando clases: se crea el fragmento en `fuentes/completo/` y se lo
agrega a `_CLASES` en `fuentes/materia.py`. Commitear el fragmento junto con
el output regenerado (`index.html`, `sw.js`, `manifest.webmanifest`).
