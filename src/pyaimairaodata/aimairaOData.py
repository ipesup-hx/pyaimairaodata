import json

from pyaimairaodata import OData
from pathlib import Path


class AimairaOData(OData):

    def __init__(self):
        with open(Path(__file__)/'..'/"credentials.json", 'r') as file:
            credentials = json.load(file)
        super().__init__(
            url="https://ipesupodata.aimaira.com/oData/",
            email=credentials["email"],
            password=credentials["password"]
        )
