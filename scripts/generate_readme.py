#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
DATA = ROOT / 'data' / 'engines.json'
BEGIN = '<!-- BEGIN ENGINE CATALOG: generated from data/engines.json; do not edit by hand -->'
END = '<!-- END ENGINE CATALOG -->'

SECTIONS = [
    ('general-2d-3d', 'General-purpose 2D + 3D engines', 'Full engines capable of both 2D and 3D workflows.'),
    ('2d-focused', '2D-focused engines and frameworks', 'Projects primarily aimed at 2D development.'),
    ('3d-focused', '3D-focused engines', 'Projects primarily aimed at 3D games, simulations, or rendering-heavy applications.'),
    ('frameworks', 'Code-first frameworks and libraries', 'Lower-level options for developers who prefer to build more of the game architecture themselves.'),
    ('specialized', 'Specialized engines and authoring systems', 'Genre-specific engines, narrative systems, fantasy consoles, interpreters, and domain-focused runtimes.'),
    ('legacy', 'Legacy, archived, or historical projects', 'Still useful to study or maintain existing projects, but not the first recommendation for a new project.'),
]


def esc(value: str) -> str:
    return value.replace('|', '\\|').replace('\n', ' ')


def render(data: dict) -> str:
    engines = data['engines']
    out = [BEGIN, '']
    for category, title, intro in SECTIONS:
        rows = [e for e in engines if e['category'] == category]
        out += [f'## {title}', '', intro, '',
                '| Project | Type | Focus | Main languages | License | Workflow | Website | Source |',
                '|---|---|---|---|---|---|---|---|']
        for e in rows:
            out.append('| **{name}** | {type} | {dimensions} | {languages} | {license} | {workflow} | [Website]({website}) | [Source]({source}) |'.format(
                **{k: esc(str(v)) for k, v in e.items()}
            ))
        out += ['', '<details>', '<summary>Notes on these entries</summary>', '']
        for e in rows:
            out.append(f"- **{e['name']}:** {e['notes']}")
        out += ['', '</details>', '']
    out += [END]
    return '\n'.join(out)


def update_readme(current: str, generated: str, repair_markers: bool = False) -> str:
    if BEGIN in current and END in current:
        before = current.split(BEGIN, 1)[0].rstrip()
        after = current.split(END, 1)[1].lstrip()
        return before + '\n\n' + generated + '\n\n' + after

    if not repair_markers:
        raise SystemExit(
            'README generation markers are missing.\n'
            'Run: python scripts/generate_readme.py --repair-markers\n'
            'Then commit the updated README.md.'
        )

    # Recover older OpenEngineAtlas READMEs that predate the generated markers.
    first_heading = '## General-purpose 2D + 3D engines'
    next_static_heading = '## Projects intentionally not included'
    if first_heading not in current or next_static_heading not in current:
        raise SystemExit(
            'Could not safely repair README markers automatically. '
            'Expected catalog headings were not found.'
        )

    before = current.split(first_heading, 1)[0].rstrip()
    static_tail = next_static_heading + current.split(next_static_heading, 1)[1]
    return before + '\n\n' + generated + '\n\n' + static_tail.lstrip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Fail if README.md is not up to date.')
    parser.add_argument('--repair-markers', action='store_true', help='Repair an older README that is missing generated catalog markers.')
    args = parser.parse_args()

    data = json.loads(DATA.read_text(encoding='utf-8'))
    current = README.read_text(encoding='utf-8')
    expected = update_readme(current, render(data), repair_markers=args.repair_markers)

    if args.check:
        if current != expected:
            print('README.md is out of date. Run: python scripts/generate_readme.py')
            return 1
        print(f"OK: README catalog matches data/engines.json ({len(data['engines'])} entries).")
        return 0

    README.write_text(expected, encoding='utf-8')
    print(f"Updated README.md from data/engines.json ({len(data['engines'])} entries).")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
