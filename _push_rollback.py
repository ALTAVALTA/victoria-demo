# -*- coding: utf-8 -*-
"""Деплой откаченной _deploy/index.html в ALTAVALTA/victoria-demo (Pages)."""
import io, os, re, shutil, subprocess, sys, tempfile

WORKSPACE = r'C:\Users\PORTAL\.openclaw\workspace'
DEPLOY = os.path.join(WORKSPACE, r'landings\victoria\_deploy')
TOKEN_FILE = os.path.join(WORKSPACE, 'secrets.txt')

COMMIT_MSG = 'victoria-demo: откат к 1705dd0e — старые заголовки (до H1 из B/v5), без schema.org'

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

shutil.copy2(os.path.join(DEPLOY, 'index.html'), os.path.join(repo_dir, 'index.html'))
for sub in ('fonts', 'img'):
    src = os.path.join(DEPLOY, sub)
    dst = os.path.join(repo_dir, sub)
    if os.path.isdir(src):
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)

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
