# 🐍 Python Style Guide – PGR107

This guide follows [PEP 8](https://peps.python.org/pep-0008/) and our internal best practices.

---

## ✍️ Naming Conventions

| Type       | Convention            | Example                    |
|------------|------------------------|-----------------------------|
| Variable   | snake_case             | `book_title`, `total_count`|
| Function   | snake_case             | `check_out_book()`         |
| Class      | CamelCase              | `Book`, `LibraryManager`   |
| Constant   | UPPER_CASE             | `MAX_TRIES`, `VERSION`     |
| File name  | lowercase_with_underscores.py | `q1_word_guess.py`   |

---

## ✅ Code Formatting

- Use **4 spaces** per indent
- Keep lines under **79 characters**
- Leave **2 blank lines** between top-level functions or classes
- Use spaces **around operators**: `x = a + b`
- Don’t mix tabs and spaces

---

## 🧼 Clean Code Tips

- Avoid deeply nested logic
- Remove unused variables/functions
- Keep functions short and focused
- Prefer clear over clever

---

## 📝 Comments & Docstrings

- Use `#` for inline comments
- Use triple quotes `"""` for function/class docstrings
- Every public function should have a docstring

```python
def check_out(title):
    """Marks a book as checked out by title."""
    ...
```


---

📌 Also see: [Pythonic Code Guide](./PYTHONIC_CODE_GUIDE.md)
