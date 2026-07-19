from hello_liteparse.custom import get_parser_ocr


def test_get_parser_ocr_config():
    parser = get_parser_ocr()
    cfg = parser.get_config()
    assert cfg.ocr_enabled is True
    assert cfg.output_format == "markdown"
    assert cfg.ocr_language == "eng"
