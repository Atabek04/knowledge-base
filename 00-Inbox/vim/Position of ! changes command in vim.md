
### `:!<command>` (! at start)

Execute external <mark style="background: #BBFABBA6;">shell command</mark>

`:!ls` - Run shell ls command
`:!python script.py` - Run Python script
`:!git status` - Run git status

---
### `:<command>!` (! at end)

Force VIM command
*override warnings / protection*

`:q!` - Quit without saving (ignores unsaved changes)
`:w!` - Force write (even if read-only)
`:e!` - Reload file, discard all changes
`:wq!` - Force save and quit

---

#### Summary

> ! prefix = shell command
> ! suffix = force VIM command