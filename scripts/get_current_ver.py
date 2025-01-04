import re
import tomllib
import pathlib


pattern = re.compile(r'^.*==(.*)$')

pyproject = tomllib.loads(
    pathlib.Path(__file__).parent.parent.joinpath('pyproject.toml').read_text(encoding='utf-8')
)

req = pyproject['project']['dependencies'][0]

m = pattern.match(req)

print(m.group(1))
