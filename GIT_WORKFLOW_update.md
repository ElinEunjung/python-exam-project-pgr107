# 🧰 Git Workflow – PGR107 Python Exam Project

This guide outlines our Git-based collaboration process for the final exam project, followed by **Elin**, **Athiththiyan**, and **Ivan**.

📌 See [Peer Review Process](./PEER_REVIEW_PROCESS.md)  
📌 See [Peer Review Checklist](./PEER_REVIEW_CHECKLIST.md)  
📌 See [Python Style Guide](./PYTHON_STYLE_GUIDE.md)

---

## ✅ 1. First-Time Setup (One-Time Only)

```bash
git clone https://github.com/ElinEunjung/python-exam-project-prg107.git
cd python-exam-project-prg107
```

---

## 🌿 2. Always Start from Latest Main

```bash
git checkout main
git pull origin main
```

---

## 🌱 3. Create a Feature Branch

```bash
git checkout -b yourname/question-[number]
# e.g.
git checkout -b elin/question-2
```

---

## 🛠️ 4. Work on Your Code

```bash
touch q2_library.py
git status
git add q2_library.py
git commit -m "feat(q2): add checkout method"
```

---

## ☁️ 5. Push Your Branch to GitHub

```bash
git push -u origin elin/question-2
```

---

## 🔁 6. Create a Pull Request (PR)

1. Go to GitHub
2. Click **"Compare & pull request"**
3. Set base to `main`
4. Assign 2 reviewers
5. Add title + description
6. Click **"Create pull request"**

---

## 👀 7. Review & Merge

- Reviewers test and comment
- If good: ✅ Approve
- If issues: ❌ Request changes
- Once approved: squash & merge

---

## 🔄 8. Sync with Main Regularly

```bash
git checkout main
git pull origin main
git checkout your-branch
git merge main
```

---

## 🧪 9. Try or Refactor Someone's Code

```bash
git checkout main
git pull origin main
git checkout -b yourname/question-x-refactor
```

---

## 📊 Quick Reference

| Task                    | Command                                    |
|-------------------------|---------------------------------------------|
| New branch              | `git checkout -b ivan/question-3`          |
| Commit changes          | `git add .` + `git commit -m "feat(...)"` |
| Push to GitHub          | `git push -u origin branch-name`          |
| Sync main               | `git checkout main && git pull`           |
| Improve other's task    | `git checkout -b elin/question-4-alt`     |
