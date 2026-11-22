"""Audit the exact public file set, repository history, and generated local links."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FILES = frozenset('''
.gitignore
LICENSE
README.md
SUPPORT.md
mkdocs.yml
requirements.txt
.github/ISSUE_TEMPLATE/config.yml
.github/ISSUE_TEMPLATE/bug_report.yml
deployment/pages-workflow.yml
deployment/welcome.md
scripts/build.py
scripts/check_content.py
scripts/deploy_pages.py
docs/en/index.md
docs/en/quick-start.md
docs/en/editors.md
docs/en/run-rules.md
docs/en/content.md
docs/en/music-sfx.md
docs/en/faq.md
docs/en/support.md
docs/en/assets/styles.css
'''.split())
OPTIONAL_PUBLIC_FILES = {'.github/workflows/pages.yml'}
IGNORED = {'.git', '.venv', '.build', '.cache', 'site', '__pycache__'}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for name in ('href', 'src'):
            if attrs.get(name):
                self.links.append(attrs[name])


def check_source(root=ROOT, history=False):
    actual = set()
    problems = []
    def visit(folder):
        for path in folder.iterdir():
            if path.is_symlink() or path.is_junction():
                problems.append(f'Linked path: {path.relative_to(root)}')
            elif path.is_dir():
                if not ((folder == root and path.name in IGNORED) or
                        (path.name == '__pycache__' and not path.is_relative_to(root / 'docs'))):
                    visit(path)
            else:
                actual.add(path.relative_to(root).as_posix())
    visit(root)
    allowed = PUBLIC_FILES | OPTIONAL_PUBLIC_FILES
    problems += [f'Unexpected public file: {p}' for p in sorted(actual - allowed)]
    problems += [f'Missing public file: {p}' for p in sorted(PUBLIC_FILES - actual)]
    for relative in sorted(actual & allowed):
        path = root / relative
        if path.suffix == '.png':
            if path.read_bytes()[:8] != b'\x89PNG\r\n\x1a\n':
                problems.append(f'Invalid PNG: {relative}')
            continue
        source = path.read_text(encoding='utf-8')
        if re.search(r'(?<![A-Za-z])[A-Za-z]:[\\/]|file:/{3}|-----BEGIN [A-Z ]*PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}', source):
            problems.append(f'Private path or credential pattern: {relative}')
    if history:
        top = subprocess.check_output(['git', '-C', str(root), 'rev-parse', '--show-toplevel'], text=True, encoding='utf-8').strip()
        if Path(top).resolve() != root.resolve():
            raise ValueError('History audit requires the independent public repository root.')
        objects = subprocess.check_output(['git', '-C', str(root), 'rev-list', '--objects', 'HEAD'], text=True, encoding='utf-8')
        for entry in objects.splitlines():
            _, separator, name = entry.partition(' ')
            if separator and name and name not in allowed and not any(p.startswith(name + '/') for p in allowed):
                problems.append(f'Forbidden path in git history: {name}')
    if problems:
        raise ValueError('\n'.join(problems))
    print(f'Public file audit passed: {len(actual)} allowed files; no product source/assets/packages/fonts.')


def check_site(site):
    pages = {}
    problems = []
    for path in site.rglob('*.html'):
        page = Page()
        page.feed(path.read_text(encoding='utf-8'))
        pages[path.resolve()] = page
    if not pages:
        raise ValueError('No generated HTML pages found.')
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            decoded = unquote(url.path)
            if decoded.startswith('/'):
                decoded = decoded.removeprefix('/dungeon-shooter-maker-docs/')
                target = (site / decoded.lstrip('/')).resolve()
            else:
                target = (path.parent / decoded).resolve() if decoded else path
            if target.is_dir():
                target /= 'index.html'
            if not target.is_relative_to(site) or not target.exists():
                problems.append(f'{path.relative_to(site)} -> missing {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                problems.append(f'{path.relative_to(site)} -> missing anchor {link}')
    if problems:
        raise ValueError('\n'.join(problems[:50]))
    print(f'Content check passed: {len(pages)} HTML pages; local links and anchors valid.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--site', type=Path)
    parser.add_argument('--history', action='store_true')
    args = parser.parse_args()
    check_source(history=args.history)
    if args.site:
        check_site(args.site.resolve())
