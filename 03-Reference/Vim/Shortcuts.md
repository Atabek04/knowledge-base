# Vim Shortcuts

## Motion (Normal Mode)

| Keys | Action |
|------|--------|
| `h` | Left |
| `j` | Down |
| `k` | Up |
| `l` | Right |
| `w` | Start of next word |
| `b` | Start of previous word |
| `e` | End of word |
| `0` | Start of line |
| `$` | End of line |
| `^` | First non-blank char |
| `gg` | Start of file |
| `G` | End of file |
| `nG` | Go to line n |
| `Ctrl+D` | Half page down |
| `Ctrl+U` | Half page up |

## Insert/Append

| Keys | Action |
|------|--------|
| `i` | Insert before cursor |
| `I` | Insert at line start |
| `a` | Append after cursor |
| `A` | Append at line end |
| `o` | New line below |
| `O` | New line above |
| `s` | Replace char + insert |
| `S` | Replace line + insert |

## Delete/Cut

| Keys | Action |
|------|--------|
| `x` | Delete char under cursor |
| `X` | Delete char before cursor |
| `d` | Delete (motion operator) |
| `dd` | Delete line |
| `d$` | Delete to end of line |
| `d0` | Delete to start of line |
| `dw` | Delete word |
| `D` | Delete from cursor to end of line |

## Copy/Yank

| Keys | Action |
|------|--------|
| `y` | Yank (copy) |
| `yy` | Copy line |
| `y$` | Copy to end of line |
| `yw` | Copy word |
| `Y` | Copy line (same as yy) |
| `p` | Paste after cursor |
| `P` | Paste before cursor |

## Undo/Redo

| Keys | Action |
|------|--------|
| `u` | Undo |
| `Ctrl+R` | Redo |
| `U` | Undo all changes on line |

## Search/Replace

| Keys | Action |
|------|--------|
| `/pattern` | Search forward |
| `?pattern` | Search backward |
| `n` | Next match |
| `N` | Previous match |
| `:s/old/new/` | Replace on line |
| `:%s/old/new/g` | Replace all in file |
| `:s/old/new/gc` | Replace with confirm |

## Selection (Visual Mode)

| Keys | Action |
|------|--------|
| `v` | Visual (character) |
| `V` | Visual line |
| `Ctrl+V` | Visual block |
| `o` | Toggle end point |

## File Operations

| Keys | Action |
|------|--------|
| `:w` | Save |
| `:q` | Quit |
| `:wq` | Save and quit |
| `:q!` | Quit without saving |
| `:e file` | Open file |
| `:bn` | Next buffer |
| `:bp` | Previous buffer |

## Find & Replace Advanced

| Keys | Action |
|------|--------|
| `*` | Search for word under cursor |
| `#` | Search backward for word |
| `:%s/old/new/gi` | Case-insensitive replace all |
| `:g/pattern/d` | Delete all lines matching pattern |

## Marks & Registers

| Keys | Action |
|------|--------|
| `ma` | Set mark a |
| `'a` | Jump to mark a |
| `"ap` | Paste from register a |
| `:marks` | List all marks |

## Indentation

| Keys | Action |
|------|--------|
| `>>` | Indent line |
| `<<` | Unindent line |
| `>motion` | Indent selection |
| `<motion` | Unindent selection |

## Useful Combos

| Keys | Action |
|------|--------|
| `ciw` | Change inner word |
| `ci"` | Change inside quotes |
| `ca"` | Change around quotes |
| `daw` | Delete word with space |
| `vip` | Select paragraph |
| `gd` | Go to definition |
| `.` | Repeat last command |
