"""Compare freshly generated certificates in scripts/ with the pinned copies in
evidence/, ignoring run-dependent fields (timings, interpreter, paths)."""
import json
import sys
from pathlib import Path

assert sys.prefix != sys.base_prefix, 'run inside the project venv'
ROOT = Path(__file__).resolve().parents[1]
VOLATILE = {'cpu_seconds', 'wall_seconds', 'python', 'executable'}


def strip(x):
    if isinstance(x, dict):
        return {k: strip(v) for k, v in x.items() if k not in VOLATILE}
    if isinstance(x, list):
        return [strip(v) for v in x]
    return x


bad = []
names = (('infimum-certificate.json',) if sys.argv[1:] == ['infimum'] else
         ('finite-certificate.json', 'class4-certificate.json', 'class4-sanity.json'))
for name in names:
    new = ROOT / 'scripts' / name
    old = ROOT / 'evidence' / name
    if not new.is_file():
        bad.append(f'{name}: not regenerated; run make verify first')
    elif strip(json.loads(new.read_text())) != strip(json.loads(old.read_text())):
        bad.append(f'{name}: differs from evidence/{name}')
    else:
        print(f'{name}: matches evidence/{name}')
if bad:
    print('\n'.join(bad))
    raise SystemExit(1)
print('CERTIFICATES MATCH')
