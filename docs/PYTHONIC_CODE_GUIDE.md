# 🐍 Pythonic Code Guide – PGR107

This guide explains what it means to write "Pythonic" code — code that follows Python’s style, idioms, and best practices to be clean, readable, and efficient.

---

## ✨ What Does “Pythonic” Mean?

> Pythonic code is code that *looks like it was written in Python*, not translated from Java, C#, or another language.

It’s about writing code that is:

- ✅ Readable
- ✅ Simple and elegant
- ✅ Leveraging Python’s built-in features
- ✅ In line with the [Zen of Python](https://peps.python.org/pep-0020/)

---

## 🧠 Examples: Pythonic vs Unpythonic

### List Building

❌ **Unpythonic**
```python
squares = []
for x in range(10):
    squares.append(x * x)
```

✅ **Pythonic**
```python
squares = [x * x for x in range(10)]
```

---

### Checking Empty Values

❌
```python
if len(my_list) == 0:
    print("Empty")
```

✅
```python
if not my_list:
    print("Empty")
```

---

### File Handling

❌
```python
f = open("data.txt")
contents = f.read()
f.close()
```

✅
```python
with open("data.txt") as f:
    contents = f.read()
```

---

### Swapping Values

❌
```python
temp = a
a = b
b = temp
```

✅
```python
a, b = b, a
```

---

## 🔑 Key Pythonic Tools and Patterns

| Technique             | Example                       |
|----------------------|-------------------------------|
| List comprehension   | `[x for x in items if x > 0]` |
| Truthy/Falsey checks | `if not x:`                   |
| `enumerate()`        | `for i, val in enumerate(x)`  |
| Unpacking            | `a, b = b, a`                 |
| `with` context       | `with open(...) as f:`        |
| Use of `in`          | `if "x" in my_list:`          |
| Simplicity           | Prefer clear over clever      |

---

## 🧘 The Zen of Python

You can read Python's philosophy in your terminal:

```python
import this
```

> "Simple is better than complex."  
> "Readability counts."  
> "There should be one-- and preferably only one --obvious way to do it."

---

## 📎 Related Resources

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Zen of Python – PEP 20](https://peps.python.org/pep-0020/)
- [Real Python: Writing Pythonic Code](https://realpython.com/tutorials/pythonic/)

---

For coding tips, also see our [Python Style Guide](./PYTHON_STYLE_GUIDE.md)
