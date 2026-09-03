"""Guard the hand-written parts of this generated SDK.

`pyproject.toml`, `README.md`, `.gitignore` and `src/famn_sdk/__init__.py` are
rewritten by the Swagger code generator on every run. Anything hand-written in them is lost
silently, and for the packaging metadata that only surfaces once a release has
already reached PyPI without a license — which disqualifies the package from
Home Assistant's dependency-transparency rule.

Run this after regenerating, and in CI.
"""

from __future__ import annotations

import pathlib
import sys
import tomllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
GENERATOR_PLACEHOLDER = "Swagger API client"
REQUIRED_URLS = ("Homepage", "Source", "Issues")
REQUIRED_IGNORES = ("build/", "dist/", "*.egg-info/")


def _check_packaging(problems: list[str]) -> None:
    """Check the metadata a regenerate is most likely to drop."""
    project = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]

    if not project.get("license"):
        problems.append("pyproject.toml has no `license`")
    if not project.get("license-files"):
        problems.append("pyproject.toml has no `license-files`")
    if project.get("description", GENERATOR_PLACEHOLDER) == GENERATOR_PLACEHOLDER:
        problems.append("pyproject.toml still has the generator's placeholder summary")
    if missing := [url for url in REQUIRED_URLS if url not in project.get("urls", {})]:
        problems.append(f"pyproject.toml is missing project URLs: {', '.join(missing)}")
    if not (ROOT / "LICENSE").is_file():
        problems.append("LICENSE is missing")


def _check_handwritten_modules(problems: list[str]) -> None:
    """Check the modules the generator does not own are still present."""
    realtime = ROOT / "src" / "famn_sdk" / "realtime.py"
    if not realtime.is_file():
        problems.append("src/famn_sdk/realtime.py was removed")
    elif "class RealtimeClient" not in realtime.read_text():
        problems.append("src/famn_sdk/realtime.py no longer defines RealtimeClient")


def _check_gitignore(problems: list[str]) -> None:
    """Check the build artifacts stay ignored.

    Without these a `python -m build` leaves `build/` and `*.egg-info/` looking
    like new source files, which is easy to commit by accident.
    """
    ignored = (ROOT / ".gitignore").read_text().splitlines()
    if missing := [rule for rule in REQUIRED_IGNORES if rule not in ignored]:
        problems.append(f".gitignore is missing: {', '.join(missing)}")


def main() -> int:
    """Report anything a regenerate has clobbered."""
    problems: list[str] = []
    _check_packaging(problems)
    _check_handwritten_modules(problems)
    _check_gitignore(problems)

    if problems:
        print("Hand-written content was lost, most likely to a regenerate:")
        for problem in problems:
            print(f"  - {problem}")
        print("\nRe-apply it before releasing; see the Releasing section of README.md.")
        return 1

    print("Hand-written content is intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
