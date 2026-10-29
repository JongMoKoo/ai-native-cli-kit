# AI Native CLI Prep Kit (public, reusable)

A generic, synthetic-data-only preparation toolkit for Codex CLI workflows. **Not an exam solution or official SK hynix/Cofa material.**

## Rules first
- Do not upload, commit, push, paste, or transmit any real exam prompt, files, logs, outputs, credentials or proprietary data to GitHub/external services.
- During the exam use only the provided Codex and tools explicitly permitted by the official guide. No Codex updates, extra AI model connections, Computer Use, or security/proctoring bypass.
- A public repository must remain public until the second-round result notice under the user's provided rules. Never rely on a private repository.
- This kit offers **generic** instructions, skills, checks and starter utilities. Adapt and implement the actual task yourself; do not substitute a downloaded solution wholesale.
- Verify licensing and network behavior of third-party dependencies before use. The MIT license here applies only to original kit files.

## Local start (Windows CMD / PowerShell)
```cmd
cd ai-native-cli-kit
python --version
python -m pip install -r requirements.txt
python -m pytest -q
python tools\check_project.py --root .
codex --version
codex
```
Codex CLI must already be installed and authorized. The commands above **do not install or update Codex**. If the provided exam environment differs, follow its guide.

## Files
- `AGENTS.md`: reusable Codex instructions
- `.agents/skills/`: skill instructions for task planning, data/ML, tests and security
- `tools/check_project.py`: local-only harness (structure, unsafe patterns, tests)
- `src/`: generic input checks and rule evaluation utilities
- `templates/`: project acceptance criteria, experiment report, model card
- `practice/`: synthetic 90-minute compressed mock, dataset, starter code

## Practice
Open `practice/COMPRESSED_MOCK.md`. Run `python -m pytest -q` and implement the missing functions in `practice/starter.py`. Do not copy this kit's practice solutions into a real exam submission.

## Sources / licenses
Original materials in this repository: MIT (`LICENSE`). No third-party source code is bundled. `pytest` is an optional development dependency; consult its own license. Public GitHub links to tools do not imply approval for use during the actual exam.
