import json
from pathlib import Path

from main import lambda_handler

dir = Path(__file__).parent

with open(
    dir / "sample" / "message_obj.json",
    mode="r",
    encoding="utf-8"
) as f:
    message_json = json.load(f)

def test_lambda_handler():
    pass
