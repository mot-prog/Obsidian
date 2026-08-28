---
tags:
  - python
  - venv
  - uv
  - cli
  - troubleshooting
aliases:
  - Fix broken venv
  - Recreate uv environment
---
When a Python virtual environment breaks (e.g., after moving a project directory or upgrading system Python), you can quickly recreate it using `uv`. 

## Steps to Recreate

```bash
# 1. Deactivate the broken environment (ignore any errors if it says command not found)
deactivate

# 2. Delete the broken virtual environment
rm -rf .venv

# 3. Create a brand new virtual environment in your current, new path
uv venv

# 4. Activate the new environment
source .venv/bin/activate

# 5. Reinstall packages (e.g., lerobot) - this will be instant thanks to uv's cache
uv pip install lerobot