"""Build the local manual with strict MkDocs validation. Does not deploy anything."""
import argparse
import os
from pathlib import Path
import subprocess
import sys
from check_content import check_source, check_site

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "site")
    args = parser.parse_args()
    output = args.output.resolve()
    if ROOT.is_relative_to(output) or (output.is_relative_to(ROOT) and output != ROOT / "site"):
        raise ValueError("Output must be the ignored site/ directory or a directory outside the documentation source.")
    env = dict(os.environ, NO_MKDOCS_2_WARNING="1")
    check_source()
    subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "--site-dir", str(output)], cwd=ROOT, env=env, check=True)
    check_site(output)
    print(f"Documentation site built locally: {output}")


if __name__ == "__main__":
    main()
