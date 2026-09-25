"""Convierte los módulos Markdown del curso a capítulos LaTeX con pandoc.

Uso (desde cursos/curso-r/latex):  python3 convertir.py && latexmk -pdf curso-r.tex
"""
import pathlib
import re
import subprocess

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = pathlib.Path(__file__).resolve().parent / "capitulos"

FUENTES = [("00-presentacion", RAIZ / "README.md")] + [
    (p.stem, p) for p in sorted(RAIZ.glob("modulo-0*.md"))
]

REEMPLAZOS = {
    "🌐": "**Web:**",
    "▶️": "**Video:**",
    "📄": "**Artículo:**",
    "📚": "**Libro:**",
    "‑": "-",            # guion no separable
    "├──": "|--",
    "└──": "`--",
    "│": "|",
}


def preprocesar(texto: str, es_presentacion: bool) -> str:
    texto = re.sub(r"\A---\n.*?\n---\n", "", texto, flags=re.S)       # front matter YAML
    texto = texto.replace("<summary>Soluciones</summary>", "### Soluciones")
    texto = re.sub(r"^</?details>\s*$", "", texto, flags=re.M)
    texto = re.sub(r"^\[\[.*\]\]\s*$", "", texto, flags=re.M)          # navegación entre módulos
    texto = re.sub(r"^> Los enlaces `\[\[\.\.\.\]\]`.*$", "", texto, flags=re.M)
    texto = re.sub(r"\[\[[^|\]]+\\?\|([^\]]+)\]\]", r"\1", texto)       # [[archivo|texto]] -> texto
    for viejo, nuevo in REEMPLAZOS.items():
        texto = texto.replace(viejo, nuevo)
    if es_presentacion:
        # El título del curso va en la portada; el README es el capítulo "Presentación".
        texto = re.sub(r"\A\s*# .*\n", "# Presentación del curso {-}\n", texto)
        texto = re.sub(r"^(##+ .*)$", r"\1 {-}", texto, flags=re.M)     # sin numerar (evita "0.1")
    return texto


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for nombre, ruta in FUENTES:
        md = preprocesar(ruta.read_text(encoding="utf-8"), nombre == "00-presentacion")
        tex = subprocess.run(
            ["pandoc", "-f", "markdown+autolink_bare_uris-auto_identifiers",
             "-t", "latex", "--listings", "--top-level-division=chapter"],
            input=md, capture_output=True, text=True, check=True,
        ).stdout
        # \chapter* no actualiza el encabezado de página: se fija a mano.
        tex = tex.replace(r"\addcontentsline{toc}{chapter}{Presentación del curso}",
                          r"\addcontentsline{toc}{chapter}{Presentación del curso}"
                          r"\markboth{Presentación del curso}{}")
        (SALIDA / f"{nombre}.tex").write_text(tex, encoding="utf-8")
        print("ok", nombre)


if __name__ == "__main__":
    main()
