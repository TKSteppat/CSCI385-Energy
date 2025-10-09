CSCI 385 - Energy group

## Setup Python environment

Needs requirements.txt to be populated

Before running any code, in your terminal follow these next steps

Create a new virtual environment for Python
```bash
python3 -m venv .venv
```

Activate your new environment by running the activation program for your system. These are located at `.venv/bin/`

Then with the environment activated you can run `pip install requirements.txt` to update your environment

Once this has been done once, you just need to follow the last two steps whenever `requirements.txt` is updated to keep up to date.

## 1. Pull the Latest Changes

Always start by syncing your local repo:

```bash
git checkout main
git pull origin main
```

---

## 2. Create a New Branch

Create a branch for your task/feature.  
Use the format: `name/feature-description`

Examples:

- `alex/add-audio-player`
- `sara/fix-style-bug`
- `nathan/setup-docker`

```bash
git checkout -b <your-branch-name>
```

---

## 3. Work on Your Feature

- Make changes in your branch
- Stage and commit regularly

```bash
git add .
git commit -m "Short description of changes"
```

---

## 4. Push Your Branch to GitHub

```bash
git push -u origin <your-branch-name>
```

---