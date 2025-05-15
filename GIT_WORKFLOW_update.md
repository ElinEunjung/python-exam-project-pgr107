
# 🧰 Git Workflow – PGR107 Python Exam Project

This file describes how Elin and Athi should work together in a clean and professional Git-based workflow for the final exam project.

---

## 🚀 INITIAL SETUP (First time only)

```bash
git clone https://github.com/your-username/python-exam-project-prg107.git
cd python-exam-project-prg107
git checkout -b elin/question-2     # or athi/question-1
```

---

## 📦 CREATE A NEW BRANCH (before you start working)

Always pull latest `main` before branching:

```bash
git checkout main
git pull origin main
git checkout -b elin/question-2     # example branch
```

> 💡 Naming pattern: `[your-name]/question-[number]` or `-refactor`, `-alt` if needed

---

## 🧑‍💻 WORKING LOCALLY

```bash
# After making changes
git status                      # See modified files
git add question2.py            # Stage file
git commit -m "Add solution for Question 2 – Elin"  # Commit
```

---

## ☁️ PUSH YOUR WORK

```bash
git push origin elin/question-2
```

---

## 🔁 CREATE A PULL REQUEST (on GitHub)

1. Go to GitHub → your repo
2. Click **"Compare & pull request"**
3. Target: `main`
4. Add comments, assign your teammate
5. Click **"Create pull request"**

---

## 👀 REVIEW & MERGE A PR

1. Review the code (leave comments if needed)
2. Click **"Merge pull request"**
3. Delete the branch (optional)

---

## 🧲 PULL LATEST MAIN (often!)

```bash
git checkout main
git pull origin main
```

---

## 🛠️ TRYING A TEAMMATE'S TASK OR MAKING REFACTOR

```bash
# After pulling main
git checkout -b athi/question-2-refactor
# Work on question2.py, push, and PR to main as usual
```

---

## 🔄 SUMMARY TABLE

| Task                        | Command Example                            |
|-----------------------------|---------------------------------------------|
| Create feature branch       | `git checkout -b ivan/question-4`          |
| Add + commit changes        | `git add .` → `git commit -m "message"`     |
| Push to GitHub              | `git push origin ivan/question-4`          |
| Sync with latest main       | `git checkout main` → `git pull origin main`|
| Refactor other's solution   | `git checkout -b athi/question-4-refactor` |



---

## 🧱 Best Practice After Checking Out a Branch

Once you've created or checked out a branch (like `elin/question-2`), follow these steps:

### ✅ 1. Create your solution file

```bash
touch question2.py     # Or create it in your IDE
```

### ✅ 2. Make an initial commit

```bash
git add question2.py
git commit -m "chore(question2): initial commit with file structure"
```

Use `chore` for setup commits, and later use `feat`, `fix`, or `refactor` as appropriate.

### ✅ 3. Push your local branch

```bash
git push -u origin elin/question-2
```

This sets the upstream so you can later just use `git push` without specifying the branch.

---

| Action                            | Commit Message Example                         |
|----------------------------------|------------------------------------------------|
| Create empty or template file    | `chore(question2): initial commit with file`   |
| Add input/output structure       | `feat(question2): setup input/output handling` |
| Implement real logic             | `feat(question2): add binary search function`  |
