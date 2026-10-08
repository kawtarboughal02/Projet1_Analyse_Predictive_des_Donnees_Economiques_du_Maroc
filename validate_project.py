import json
import os
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
NOTEBOOK_DIR = ROOT / 'notebooks'

# Prevent interactive display from blocking automated validation.
plt.show = lambda: None

for notebook_path in sorted(NOTEBOOK_DIR.glob('*.ipynb')):
    namespace = {'__name__': '__main__'}
    notebook = json.loads(notebook_path.read_text(encoding='utf-8'))
    print(f'Validation de {notebook_path.name}')
    with os.scandir(NOTEBOOK_DIR):
        previous_directory = Path.cwd()
        os.chdir(NOTEBOOK_DIR)
        try:
            for cell_number, cell in enumerate(notebook.get('cells', []), start=1):
                if cell.get('cell_type') != 'code':
                    continue
                source = ''.join(cell.get('source', []))
                try:
                    exec(compile(source, f'{notebook_path.name}:cell_{cell_number}', 'exec'), namespace)
                except Exception as error:
                    raise RuntimeError(
                        f'{notebook_path.name}, cellule {cell_number}: {error}'
                    ) from error
        finally:
            os.chdir(previous_directory)
    print(f'OK: {notebook_path.name}')

print('VALIDATION_COMPLETE')
