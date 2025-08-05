
# Inductiva Barebones Shell

A minimal command-line interface for running Python scripts or executing `inductiva` CLI commands — **without needing to install Python or any packages manually**.

This tool is distributed as a **single-file executable** to help users **quickly try out Inductiva** or run simple workflows.

---

## 🚀 What Is This?

`Inductiva Barebones Shell` is a REPL-style terminal application that supports two types of commands:

- `python <script.py> [args]` – Runs a local Python script with arguments
- `inductiva <cli-command>` – Runs `inductiva` CLI commands (e.g., `inductiva auth login`, `inductiva list simulations`, etc.)

✅ All bundled into a single `.exe` — no Python installation required!

---

## 🖥️ Usage

### 🧪 Trying Inductiva with No Setup

Just download and run the executable:

```bash
./inductiva-runner.exe
```

Once launched, you'll see a prompt:

```
Inductiva Barebones Shell. Type 'exit' or Ctrl+C to quit.
>
```

### Start by logging in

First run the login cli command:
```
> indutiva auth login
```

You can now:

### ▶️ Run a Python Script

```bash
> python my_script.py arg1 arg2
```

Make sure the script is in the same folder or provide the full path.

### 🔧 Try the Inductiva CLI

```bash
> inductiva user info
```

This runs actual `inductiva` CLI commands — no installation needed.

---

## 💡 When to Use This

### ✅ Use This If:

* You want to **quickly try** the Inductiva CLI without setting up Python
* You’re testing a **simple workflow or script** that depends on `inductiva`
* You’re introducing Inductiva to someone new (e.g., in a workshop or tutorial)

### ❗ Recommended Alternative for Full Use:

For production use, development, or scripting, we **highly recommend installing `inductiva` via pip**:

```bash
pip install inductiva
```

This gives you the full Python environment and integration features.

---

## 🤝 Contributions

Pull requests and issues are welcome!
