"""Approved-only gh-pages push, isolated from the documentation main checkout."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REMOTE = 'https://github.com/hyunter777/dungeon-shooter-maker-docs.git'


def git(folder, *args):
    return subprocess.check_output(['git', '-C', str(folder), *args], text=True, encoding='utf-8').strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--approved', action='store_true', help='Only after explicit publisher approval.')
    args = parser.parse_args()
    if not args.approved:
        raise SystemExit('Publication requires explicit approval and --approved. No commands executed.')
    if Path(git(ROOT, 'rev-parse', '--show-toplevel')).resolve() != ROOT:
        raise ValueError('Deploy only from the independent documentation repository.')
    if git(ROOT, 'branch', '--show-current') != 'main' or git(ROOT, 'status', '--porcelain'):
        raise ValueError('Documentation main must be checked out and completely committed.')
    if (git(ROOT, 'remote', 'get-url', '--all', 'origin') != REMOTE or
            git(ROOT, 'remote', 'get-url', '--push', '--all', 'origin') != REMOTE):
        raise ValueError('Unexpected origin; refusing deployment.')
    visibility = subprocess.check_output(['gh', 'api', 'repos/hyunter777/dungeon-shooter-maker-docs', '--jq', '.private'], text=True, encoding='utf-8').strip()
    if visibility != 'false':
        raise ValueError('Expected the approved PUBLIC documentation repository.')
    subprocess.run([sys.executable, str(ROOT / 'scripts/check_content.py'), '--history'], check=True)
    subprocess.run([sys.executable, str(ROOT / 'scripts/build.py')], check=True)
    checkout = ROOT / '.build/gh-pages'
    checkout.parent.mkdir(exist_ok=True)
    if not checkout.exists():
        checkout.mkdir()
        git(checkout, 'init', '-b', 'gh-pages')
        git(checkout, 'remote', 'add', 'origin', REMOTE)
    if checkout.is_symlink() or checkout.is_junction():
        raise ValueError('Linked deployment checkout is not allowed.')
    if Path(git(checkout, 'rev-parse', '--show-toplevel')).resolve() != checkout.resolve():
        raise ValueError('Invalid deployment checkout.')
    if (git(checkout, 'remote', 'get-url', '--all', 'origin') != REMOTE or
            git(checkout, 'remote', 'get-url', '--push', '--all', 'origin') != REMOTE):
        raise ValueError('Unexpected deployment origin.')
    if git(checkout, 'branch', '--show-current') != 'gh-pages' or git(checkout, 'status', '--porcelain'):
        raise ValueError('Deployment checkout must be clean on gh-pages; inspect a previous failure before retrying.')
    exists = bool(git(ROOT, 'ls-remote', '--heads', 'origin', 'refs/heads/gh-pages'))
    if exists:
        # Also works for an unborn local branch. Pull immediately before changing site files.
        print('gh-pages: git pull --rebase --autostash origin gh-pages', flush=True)
        git(checkout, 'pull', '--rebase', '--autostash', 'origin', 'gh-pages')
    else:
        print('gh-pages: first push; no remote branch exists to pull.', flush=True)
    # Delete tracked output only, inside the verified isolated checkout.
    git(checkout, 'rm', '-r', '--ignore-unmatch', '--', '.')
    for path in (ROOT / 'site').iterdir():
        target = checkout / path.name
        if path.is_dir():
            shutil.copytree(path, target, dirs_exist_ok=True)
        else:
            shutil.copyfile(path, target)
    (checkout / '.nojekyll').touch()
    source_commit = git(ROOT, 'rev-parse', 'HEAD')
    (checkout / 'source-revision.txt').write_text(source_commit + '\n', encoding='utf-8')
    # Stage only the explicitly enumerated generated files, never git add -A.
    files = sorted(p.relative_to(checkout).as_posix() for p in checkout.rglob('*')
                   if p.is_file() and '.git' not in p.relative_to(checkout).parts)
    for start in range(0, len(files), 50):
        git(checkout, 'add', '--', *files[start:start + 50])
    changed = subprocess.run(['git', '-C', str(checkout), 'diff', '--cached', '--quiet'])
    if changed.returncode == 1:
        git(checkout, 'commit', '-m', f'Public manual deployment {source_commit[:12]}')
    elif changed.returncode != 0:
        raise RuntimeError('Failed to inspect generated site changes.')
    git(checkout, 'push', '--set-upstream', 'origin', 'gh-pages')
    deployed = git(checkout, 'rev-parse', 'HEAD')
    remote_head = git(checkout, 'ls-remote', 'origin', 'refs/heads/gh-pages').split()[0]
    if deployed != remote_head:
        raise RuntimeError('gh-pages remote commit did not match.')
    print(f'gh-pages push verified: {deployed}; source {source_commit}', flush=True)


if __name__ == '__main__':
    main()
