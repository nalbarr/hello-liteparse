import logging
import os
import time
from pathlib import Path

from liteparse import LiteParse

_log = logging.getLogger(__name__)


def get_parser_ocr():
    return LiteParse(
        ocr_enabled=True,
        ocr_language=os.environ.get("LITEPARSE_OCR_LANGUAGE", "eng"),
        output_format="markdown",
        include_complexity=True,
    )


def main():
    logging.basicConfig(level=logging.INFO)

    parser = get_parser_ocr()

    filenames = ["./inputs/2408.09869v5.pdf"]
    for filename in filenames:
        input_doc_path = filename

        start_time = time.time()
        result = parser.parse(input_doc_path)
        end_time = time.time() - start_time

        _log.info(f"Document converted in {end_time:.2f} seconds.")

    output_dir = Path("scratch")
    output_dir.mkdir(parents=True, exist_ok=True)
    doc_filename = Path(input_doc_path).stem

    with (output_dir / f"{doc_filename}.md").open("w", encoding="utf-8") as fp:
        fp.write(result.text)


if __name__ == "__main__":
    main()
