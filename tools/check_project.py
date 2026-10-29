"""Local-only lightweight project inspection; not a full security audit."""
import argparse
from pathlib import Path
import re
import subprocess
import sys

PATTERNS = {'eval call': r'\beval\s*\(', 'exec call': r'\bexec\s*\(', 'os.system call': r'\bos\.system\s*\('}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--root', default='.')
    args = p.parse_args()
    root = Path(args.root).resolve()
    findings=[]
    for path in root.rglob('*.py'):
        if any(x in path.parts for x in ('.git','.venv','venv','__pycache__')):
            continue
        if path.name == 'check_project.py':
            continue
        for i,line in enumerate(path.read_text(encoding='utf-8', errors='replace').splitlines(),1):
            for label,pattern in PATTERNS.items():
                if re.search(pattern,line):
                    findings.append(f'{path.relative_to(root)}:{i}: possible {label}')
    print('Static findings:', len(findings))
    for x in findings: print(' -', x)
    print('Running tests (if pytest available):')
    r=subprocess.run([sys.executable,'-m','pytest','-q'],cwd=root,check=False)
    return 1 if findings or r.returncode else 0

if __name__=='__main__':
    raise SystemExit(main())
