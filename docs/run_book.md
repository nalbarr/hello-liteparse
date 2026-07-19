# Run Book

Concise usage reference for `hello-liteparse`. For LiteParse itself, see the
[upstream repo](https://github.com/run-llama/liteparse).

## Setup

```
uv sync
make init-env
```

Requires Python `>=3.11.8` (see `.python-version`) and [uv](https://docs.astral.sh/uv/).

`main.py` reads its source from the `LITEPARSE_SOURCE_URL` env var (loaded
from `.env`, gitignored). `.env.example` is checked in with a working default
— edit `.env` to point at a different PDF/URL.

## Common commands

| Command | What it does |
|---|---|
| `make init-env` | Copies `.env.example` to `.env`, overwriting any existing `.env`. |
| `make run` | Runs `src/hello_liteparse/main.py` — downloads the PDF/URL from `LITEPARSE_SOURCE_URL` (see `.env`), parses it to markdown, prints to stdout. |
| `make run-custom` | Runs `src/hello_liteparse/custom.py` — builds a `LiteParse` parser with Tesseract OCR enabled and complexity detection on, converts `inputs/2408.09869v5.pdf`, writes markdown to `scratch/`. |
| `make test` | Runs the pytest suite (`tests/`). |
| `make clean` | Removes `scratch/` (generated output). Runs automatically before `run`/`run-custom`. |
| `make liteparse-run` | Raw `lit` CLI: converts `inputs/2408.09869v5.pdf` to markdown with OCR disabled, output to `scratch/`. |

## Project layout

- `src/hello_liteparse/` — the package. `main.py` (minimal URL example) and
  `custom.py` (Tesseract-backed OCR parser).
- `inputs/` — sample input PDF(s) checked into the repo.
- `scratch/` — generated conversion output, gitignored, wiped by `make clean`.
- `tests/` — pytest suite.
- `docs/` — this file.

## Direct CLI usage

Beyond what the `Makefile` wraps, the `lit` CLI (installed alongside the
`liteparse` Python package) can be invoked directly:

```
# Convert a local file to markdown
lit parse ./inputs/2408.09869v5.pdf --format markdown

# Check whether a document needs OCR before committing to a full parse
lit is-complex ./inputs/2408.09869v5.pdf

# Generate page screenshots (useful for feeding LLM agents)
lit screenshot ./inputs/2408.09869v5.pdf -o ./scratch/screenshots
```

`src/hello_liteparse/custom.py` shows the equivalent programmatic setup —
constructing a `LiteParse` instance directly with OCR/output options, rather
than going through the CLI.

## Troubleshooting

- **`main.py` downloads the URL itself**: unlike Docling's
  `DocumentConverter`, LiteParse's `parse()` only accepts a local file path
  or raw bytes — it has no built-in URL fetching. `main.py` downloads
  `LITEPARSE_SOURCE_URL` with `urllib` before handing the bytes to
  `LiteParse.parse()`.
- **Non-PDF formats need system tools**: DOCX/XLSX/PPTX/ODF conversion
  requires LibreOffice, and image formats require ImageMagick, installed on
  the host — LiteParse shells out to them rather than bundling them.
- **No EasyOCR/PaddleOCR out of the box**: those only work via
  `ocr_server_url` pointing at an external HTTP OCR server. This project uses
  LiteParse's bundled Tesseract OCR instead (see `LITEPARSE_OCR_LANGUAGE`
  env var, default `eng`).
- **`scratch/` gets wiped**: `make run` and `make run-custom` both depend on
  `clean`, which deletes `scratch/` before every run — don't store anything
  there you want to keep.
