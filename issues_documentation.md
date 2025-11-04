# Static Code Analysis - Issues Documentation

## Summary
- **Original Code Score:** Pylint 4.80/10, Bandit 2 issues, Flake8 11 violations
- **Total Issues Found:** 11 major issues
- **Issues Fixed:** 11 (ALL - eligible for +2 extra credit)
- **Date:** November 4, 2025

---

## Issues Identified and Fixed

| # | Tool | Line | Code | Severity | Issue Description | How Fixed |
|---|------|------|------|----------|-------------------|-----------|
| 1 | Bandit, Pylint | 58 | B307, W0123 | **HIGH** | Use of eval() - code injection vulnerability | Removed eval() call entirely |
| 2 | Pylint | 7 | W0102 | **HIGH** | Dangerous mutable default argument `logs=[]` - shared between calls | Changed to `logs=None`, initialize inside function |
| 3 | Pylint, Flake8, Bandit | 18 | W0702, E722, B110 | **MEDIUM** | Bare except clause catches all exceptions including Ctrl+C | Changed to `except (KeyError, ValueError) as e:` |
| 4 | Pylint | 25, 31 | R1732 | **MEDIUM** | No context manager - files may not close on error | Changed to `with open() as f:` |
| 5 | Pylint | 25, 31 | W1514 | **MEDIUM** | No encoding specified - platform-dependent behavior | Added `encoding="utf-8"` |
| 6 | Pylint, Flake8 | 2 | W0611, F401 | **MEDIUM** | Unused import 'logging' | Removed the import statement |
| 7 | Pylint | 11 | C0209 | **LOW** | Old % string formatting | Changed to f-string |
| 8 | Pylint | Multiple | C0114, C0116 | **LOW** | Missing module and function docstrings | Added comprehensive docstrings |
| 9 | Pylint | Multiple | C0103 | **LOW** | camelCase function names (not PEP 8) | Renamed to snake_case |
| 10 | Flake8 | Multiple | E302, E305 | **LOW** | PEP 8 spacing - need 2 blank lines | Added proper spacing |
| 11 | Custom | 7, 14 | N/A | **MEDIUM** | No input validation - crashes on invalid input | Added type checking and validation |

---

## Detailed Explanation of Top 3 Critical Issues

### Issue #1: eval() Security Vulnerability (Line 58)
**Original:**
```python
eval("print('eval used')")  # DANGEROUS
```

**Problem:** eval() executes ANY Python code. Attackers could use this to delete files, steal data, or crash the system.

**Fixed:**
```python
print("System demonstration completed successfully")
```

---

### Issue #2: Mutable Default Argument (Line 7)
**Original:**
```python
def addItem(item="default", qty=0, logs=[]):  # BUG!
```

**Problem:** The `[]` is created ONCE when function is defined. All calls share the SAME list object. Logs accumulate unexpectedly across different function calls.

**Fixed:**
```python
def add_item(item="default", qty=0, logs=None):
    if logs is None:
        logs = []  # Fresh list each time
```

---

### Issue #3: Bare Except Clause (Line 18)
**Original:**
```python
except:  # Catches EVERYTHING
    pass  # Silent failure
```

**Problem:** Catches ALL exceptions including KeyboardInterrupt (can't stop program with Ctrl+C) and makes debugging impossible.

**Fixed:**
```python
except (KeyError, ValueError) as e:
    print(f"Error removing item: {e}")
    return False
```

---

## Additional Improvements Beyond Tool Findings

### Input Validation Added
**Problem:** Original code crashes on line 50 with `addItem(123, "ten")` because it tries to add string to number.

**Solution:** Added validation to check:
- Item must be a string
- Quantity must be a non-negative integer
- Returns boolean for error handling

---

**Total improvements: Security ✅ Robustness ✅ Maintainability ✅ Style ✅**