"""Config de este apunte para motor_apuntes. Ver contrato-fragmento.md del
paquete (motor_apuntes) para el vocabulario de los fragmentos.

Apunte de Arquitectura de Software (TB034, FIUBA). Una sola salida: el
apunte completo (fuentes/completo/ -> ./), un capitulo por clase. Se arma
con motor_apuntes.armar.construir(). CFG["grupos"] lista solo las clases que
ya tienen fragmento.

Paleta: propia de la materia (magenta sobre neutros frios), pensada para que
se distinga de las otras materias de la plataforma: el violeta ya es de
Sistemas Distribuidos y el azul de Ciencia de Datos.
"""

PALETA_LIGHT = """:root {
      color-scheme: light;
      --bg: #f6f4f6;
      --surface: #ffffff;
      --surface-2: #eeeaee;
      --ink: #1f1a1e;
      --muted: #675d64;
      --line: #e2dbe0;
      --accent: #a8336b;
      --accent-2: #f9e1ec;
      --accent-ink: #7a1f4c;
      --warm: #9a5a12;
      --warm-bg: #fdeecf;
      --danger: #a33540;
      --danger-bg: #fbe7e9;
      --blue: #2f6f8f;
      --blue-bg: #e2f0f6;
      --ok: #35704a;
      --ok-bg: #e6f4ea;
      --exam: #5b4bb0;
      --exam-bg: #ebe8fa;
      --hl-yellow: #ffe08a;
      --hl-mint: #a7ead2;
      --hl-pink: #ffc1d2;
      --hl-blue: #bcd7ff;
      --shadow: 0 18px 55px rgba(48, 18, 34, .09);
      --radius: 18px;
      --sidebar: 292px;
    }"""

PALETA_DARK = """html[data-theme="dark"] {
      color-scheme: dark;
      --bg: #141013;
      --surface: #1c171b;
      --surface-2: #271f25;
      --ink: #f4edf1;
      --muted: #b3a5ae;
      --line: #372c34;
      --accent: #f08cba;
      --accent-2: #3d1a2c;
      --accent-ink: #f9c6dd;
      --warm: #f0b766;
      --warm-bg: #392a17;
      --danger: #f19aa2;
      --danger-bg: #3c2125;
      --blue: #86bdd6;
      --blue-bg: #163040;
      --ok: #86cf9b;
      --ok-bg: #182f21;
      --exam: #b3a6f5;
      --exam-bg: #26214a;
      --hl-yellow: #725d19;
      --hl-mint: #185a4d;
      --hl-pink: #71384b;
      --hl-blue: #294f78;
      --shadow: 0 18px 55px rgba(0, 0, 0, .26);
    }"""

_CLASES = [
    ("intro", "1", "Introducción: qué es la arquitectura de software"),
    ("qa1", "2", "Atributos de calidad I: disponibilidad y escalabilidad"),
    ("performance", "3", "Performance y la red conceptual"),
    ("metricas", "4", "Métricas del TP1 y ejercicios de escalabilidad"),
    ("qa2", "5", "Atributos de calidad II y tácticas de escalabilidad"),
]

CFG = {
    "clave": "arq",
    "codigo": "TB034",
    "catedra": "Calónico",
    "autores": ["flopeztancredi"],
    "prefijo_ls": "arq",
    "titulo_tab": "Arquitectura de Software - Apunte",
    "marca": "Arquitectura de Software",
    "h1": "Arquitectura de Software",
    "hero": ("Apunte de Arquitectura de Software (TB034, FIUBA), clase por "
             "clase: lo que dicen las diapositivas y lo que se agregó en la "
             "clase grabada, con los ejemplos y las advertencias de los "
             "docentes. Arranca por qué es arquitectura y los atributos de "
             "calidad."),
    "descripcion": "Apunte de Arquitectura de Software (TB034, FIUBA), un resumen por clase.",
    "theme_color": "#a8336b",
    "favicon_hex": "a8336b",
    "grupos": [
        ("Clases", _CLASES),
    ],
    "paleta_light": PALETA_LIGHT,
    "paleta_dark": PALETA_DARK,
}
