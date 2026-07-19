import os
import urllib.request

from dotenv import load_dotenv

from liteparse import LiteParse

load_dotenv()

source = os.environ["LITEPARSE_SOURCE_URL"]
request = urllib.request.Request(
    source, headers={"User-Agent": "hello-liteparse/0.1 (+https://github.com/run-llama/liteparse)"}
)
with urllib.request.urlopen(request) as response:
    document_bytes = response.read()

parser = LiteParse(output_format="markdown")
result = parser.parse(document_bytes)

print(result.text)
