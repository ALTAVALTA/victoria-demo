# -*- coding: utf-8 -*-
"""Деплой 2test_demo в ALTAVALTA/victoria-demo в подпапку 2test-demo/."""
import io, os, re, shutil, subprocess, sys, tempfile

WORKSPACE = r'C:\Users\PORTAL\.openclaw\workspace'
SRC = os.path.join(WORKSPACE, r'landings\victoria\_deploy\_deploy_2test')
TOKEN_FILE = os.path.join(WORKSPACE, 'secrets.txt')

COMMIT_MSG = 'Демо 2test-demo (2-й прогон свободного промпта, 26 фото, пульс-подпись)'

text = io.open(TOKEN_FILE, encoding='utf-8').read()
m = re.search(r'ghp_[A-Za-z0-9]{20,}', text)
if not m:
    print('NO TOKEN'); sys.exit(1)
token = m.group(0)
print('token ok, len', len(token))

repo_dir = tempfile.mkdtemp(prefix='victoria_demo_')
print('clone dir:', repo_dir)

def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode != 0:
        print('CMD FAIL:', ' '.join(cmd))
        print(r.stdout[-2000:])
        print(r.stderr[-2000:])
        sys.exit(1)
    return r.stdout

url = 'https://altavalta-dev:%s@github.com/ALTAVALTA/victoria-demo.git' % token
run(['git', 'clone', '--depth', '1', url, repo_dir])

dst_dir = os.path.join(repo_dir, '2test-demo')
if os.path.isdir(dst_dir):
    shutil.rmtree(dst_dir)
shutil.copytree(SRC, dst_dir)

out = run(['git', 'status', '--short'], cwd=repo_dir)
print('--- git status ---')
print(out)

if not out.strip():
    print('NOTHING TO COMMIT')
    sys.exit(0)

run(['git', 'add', '-A'], cwd=repo_dir)
run(['git', '-c', 'user.name=ALTAVALTA', '-c', 'user.email=altavalta@users.noreply.github.com',
     'commit', '-m', COMMIT_MSG], cwd=repo_dir)
run(['git', 'push', 'origin', 'main'], cwd=repo_dir)
print('PUSHED OK')
