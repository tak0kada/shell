# What is this?
Python functions to call shell command which wraps subprocess.

# Usage
```python
from pathlib import Path
import shell

shell.exec("echo 'Hello World!'")
shell.exec("sleep 10", timeout_s = 1, log = Path("./log.txt"))

val = shell.valueof("pwd")
print(val)
```