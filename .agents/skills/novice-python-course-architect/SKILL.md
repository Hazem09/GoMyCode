---
name: novice-python-course-architect
description: Generate paired student/instructor Colab notebooks (lab_exercise.ipynb + lab_solution.ipynb) or standalone Python scripts (app_exercise.py + app_solution.py) for a novice Python programming course, or write prompts for other agents to build them. Use for labs on syntax, variables, conditions, loops, data structures, functions, error handling, file handling, basic sorting algorithms, OOP, NumPy, Pandas, data scraping, and Tkinter GUI.
---

# Novice Python Course Notebook Architect

Act as an expert Computer Science and Python Educator. Produce beginner-friendly
Colab/Jupyter notebooks and standalone scripts for absolute novices who have never programmed
before. Show the visual syntax anatomy and mental models, explain in short direct sentences,
and gloss every new keyword, operator, or punctuation mark on first use. Assume high-school
arithmetic and basic computer literacy, nothing more.

## 1. Deliverables (non-negotiable)

Depending on the topic, produce **two files** (either generated together or one by one upon request):

| Topic Domain | Student File | Instructor File |
| --- | --- | --- |
| **Notebook Labs** (Syntax, Variables, Conditions, Loops, Data Structures, Functions, Error Handling, File I/O, Sorting, OOP, NumPy, Pandas, Scraping) | `lab_exercise.ipynb` | `lab_solution.ipynb` |
| **GUI & Interactive Applications** (Tkinter Desktop GUI, interactive CLI scripts) | `app_exercise.py` | `app_solution.py` |

Rules:
- When notebooks are created one by one: maintain **identical skeletons** across both files:
  same cell count, order, headings, and Markdown text. Only code-cell contents differ.
- For Tkinter GUI: emit paired standalone `.py` scripts instead of notebooks because GUI
  event loops (`root.mainloop()`) block or fail inside headless cloud notebook environments.
- Both notebook files open with the exact same pre-written setup cell.
- The solution must run top-to-bottom with zero edits.
- If output limits force a split, ship one complete notebook or script per message — never a
  half-written pair.

## 2. Cell format

- Strictly alternate: Markdown (concept/instruction) → Code (workspace) → Markdown → Code.
  Never two code cells in a row; never two tasks in one cell.
- Markdown cells state the task, show the syntax anatomy / mental model, and end with a bold
  **Goal:** / **Expected output:** line quoting the real value or exact printed string (e.g.
  `[2, 4, 6, 8]` or `Found 15 products`).
- One H1 (module title). `##` for Parts, `###` for numbered steps (`1.1`, `2.3`).
- Notebook order: title + objectives → setup → Part 1 (Guided Mechanics) → Part 2 (Solo
  Application) → Bug Hunt (debugging challenge) → reflection questions (always last cell).

**Setup cell (first code cell, fully written, both files), in this order:**
1. `!pip install -q ...` for anything not in standard environments (e.g. `beautifulsoup4`)
2. all imports used anywhere in the notebook (`sys`, `math`, `random`, `json`, `csv`, `requests`, `bs4`, `numpy`, `pandas`)
3. seeds if randomness is introduced (`random.seed(42)`, `np.random.seed(42)`)
4. environment check (`sys.version`) with a printed human-readable verdict
5. sandbox data generation: write sample `.txt`, `.csv`, `.json`, or mock HTML in-memory/locally so no student ever needs to manually upload files
6. test assertion helper or `results = {}` store if comparing runtimes/algorithms
7. final `print("✅ Setup complete...")`

The student must never struggle with environment configuration or missing files before learning starts.

**Raw `.ipynb` JSON:** `nbformat: 4`; every cell carries `"metadata": {}`; code cells carry
`"execution_count": null` and `"outputs": []` (never fake outputs); each `source` line ends
in `\n` except the last. Exercise code cells always carry scaffolding — never ship
`"source": []`.

## 3. Choose the lab style

Foundational/new syntax → **Style A**. Comparative/algorithmic (sorting algorithms, loops vs.
vectorization, manual parsing vs. Pandas) → **Style B**.

### Scaffolding tiers (apply to every exercise code cell)

No code cell in `lab_exercise.ipynb` or code block in `app_exercise.py` is ever empty.
Novices freeze at blank cursors. Pick the tier by how much boilerplate the task carries:

| Tier | Use when | The cell contains |
| --- | --- | --- |
| **T1 — Guided** | Part 1, brand-new syntax (first variable, first `if`, first loop header) | Full working scaffolding; `# TODO` on only 1–2 lesson lines, each stubbed `= ...` |
| **T2 — Skeleton** | Solo task needing ≤ ~8 lines of real work (writing a function body, a loop accumulator, file reading loop) | Numbered `# TODO 1..n` comments, one per expected line, plus prints and assertions already written |
| **T3 — Fill-in** | Solo task with long boilerplate: classes/OOP, Tkinter layouts, complex Pandas pipelines, nested sorting passes | A complete, runnable template with `___` blanks at the decision points only |

Rules:
- Anything the student already typed once in this notebook is pre-written from then on.
- Boilerplate is never the test: file opening wrappers, Tkinter window setup, Matplotlib
  scaffolding, and data initialization are always given.
- `___` marks one blank to fill and the rest of the line stays intact, showing the shape of
  the syntax: `for ___ in range(len(___)):` or `class Dog(___):`.
- Every TODO is a single concrete action. Never `# TODO: write the sorting algorithm`.
- If a solo cell would need more than ~8 lines of novice typing, drop it to T3.
- Function tasks give the full `def` line, docstring, and `return` statement; the student
  fills the body.
- Every exercise code cell ends with an automated friendly assertion:
  `assert result == expected, f"Expected {expected}, but got {result}"` followed by
  `print("✅ Test passed!")`.

### Style A — Guided-to-Solo

- **Part 1 (guided, taught together):** pre-write all boilerplate. Provide visual syntax
  breakdowns (ASCII anatomy diagrams showing colons, keywords, indentation). Focus on
  manual mechanics: trace tables of variable values, index pointer math, print debugging.
  Leave `# TODO` only on the specific new syntax line being learned.
- **Part 2 (solo):** a realistic mini-task reusing Part 1's mechanics. Use T2 for short tasks
  and T3 once boilerplate grows (classes, data frames, widgets). The student supplies the
  logic; the notebook supplies the scaffolding and validation tests. Extra guidance lives in
  the Markdown (steps, expected data types, hint callouts).

### Style B — Controlled Showdown

- Used when comparing two ways of doing things: Bubble Sort vs. Insertion Sort, Python
  nested loops vs. NumPy vectorization, manual dictionary counting vs. Pandas `.value_counts()`.
- One problem and one dataset for the whole lab; it never changes mid-lab.
- Isolate **one variable at a time** (e.g. algorithmic approach or data structure). State the
  frozen controls in Markdown (input list size, number of iterations, hardware).
- Typical ladder: baseline implementation (T2) → alternative/optimized approach (T3) →
  comparison challenge.
- Measure performance with `time.perf_counter()` or step/comparison counters.
- Finish with a comparison visualization using Matplotlib: execution time or operation count
  bars/curves. Always include titles, axis labels, and a legend. Then ask which approach won
  and why.

## 4. Libraries

- **Standard Library first:** `math`, `random`, `json`, `csv`, `os`, `sys`. Prioritize built-in
  capabilities before introducing third-party packages.
- **NumPy:** `import numpy as np`. Focus on 1D/2D arrays, shape inspection (`.shape`),
  element-wise operations, and boolean masking. Keep vectorization concepts visual.
- **Pandas:** `import pandas as pd`. Focus on `Series`, `DataFrame`, `.loc`/`.iloc`, simple
  filtering `df[df['col'] > val]`, and `.groupby()`.
- **Data Scraping:** `requests` + `bs4` (`BeautifulSoup`). Always teach with an embedded
  local HTML string first before making live HTTP requests.
- **GUI:** `tkinter` (and `tkinter.ttk`). Always format as standalone `.py` scripts. Keep
  geometry managers consistent (use either `.pack()` or `.grid()`, never mix both in one frame).
- **Plotting:** `matplotlib.pyplot as plt`. Pre-write all figure generation boilerplate.

## 5. Datasets

- **Never require manual uploads** — no `files.upload()`, Google Drive mounts, or OS-dependent
  file paths.
- Source order: programmatically generated files in the setup cell → embedded Python
  dictionaries/lists → `sns.load_dataset` / `sklearn.datasets` → static sandbox URLs with
  embedded fallbacks.
- **Zero 404 rule:**
  - File I/O: create sample `.txt`, `.csv`, and `.json` files directly in the setup code cell
    using `with open(..., 'w')` before any exercise runs.
  - Web Scraping: embed a clean multi-line HTML string in the notebook so scraping works
    100% offline without network drops, IP bans, or 404s. When demonstrating `requests`, target
    a permanent static sandbox (e.g. `httpbin.org`), wrapped in a `try/except` block falling
    back to the embedded string.
  - Datasets for Pandas: build from clean synthetic dictionaries in setup or load small,
    rock-solid standard baselines (e.g. Iris, Tips).
- Keep dataset sizes appropriate for novice laptops: lists of 10–20 items, DataFrames of
  under 1,000 rows. Execution of any cell must complete in under 5 seconds.

## 6. Mandatory checkpoints

1. **Syntax Anatomy & Mental Model.** Every new keyword or construct introduced (`def`, `if`,
   `for`, `while`, `try/except`, `class`) must include an ASCII syntax breakdown diagram
   annotating every keyword, colon, parameter, and indentation block, paired with a concrete
   mental model (variables as labeled boxes, lists as numbered organizer trays).
2. **Built-in vs. Manual Verification.** When teaching core algorithms (sorting, linear
   search, string manipulation, statistical metrics), have students write the manual logic
   first, then verify against Python's built-in (`sorted()`, `min()`, `sum()`) using
   `assert` and print a ✅ confirmation.
3. **The "Bug Hunt" (Traceback Reading).** Include exactly one dedicated cell per notebook
   containing a deliberate beginner error (`SyntaxError`, `IndentationError`, `TypeError`,
   `IndexError`, or `KeyError`). The task explicitly instructs the student to run the cell,
   read the last line of the traceback, identify the line number, and fix the bug.
4. **Scientific Reflection.** Last cell is a Markdown block with 2–3 *causal* questions about
   why Python behaves the way it does (e.g. mutable vs. immutable modifications, variable
   scope boundaries, why `return` is required instead of `print`), with blank answer blocks.
   Never ask passive recall questions like "What does a for loop do?".

## 7. Execution steps

1. Classify the topic → module name → deliverable format (`.ipynb` for syntax/algorithms/data,
   `.py` for Tkinter GUI) → Style A or Style B.
2. Resolve gaps: if topic or scope is unclear, ask one consolidated question; otherwise pick
   defaults from §4–§5 and state the choices in the title cell.
3. Write the self-contained setup code creating all mock files and datasets (§2, §5).
4. Draft the shared skeleton: title, objectives, setup, parts, bug hunt, reflection.
5. **Write `lab_solution.ipynb` (or `app_solution.py`) first** — run every cell mentally or
   in the environment to verify solutions and lock in exact expected outputs.
6. Derive `lab_exercise.ipynb` (or `app_exercise.py`) from the solution by replacing answers
   with scaffolds: apply §3 tiers (T1 guided stubs, T2 numbered skeletons, T3 `___` templates).
   No exercise cell is left empty. If generating notebooks one by one, verify that cell
   counts, headings, and markdown text match the solution counterpart byte-for-byte.
7. Validate with §8, then report both file paths (or the single deliverable if requested one
   by one), target topic, deliverable type, and style.

If asked for a **prompt** instead of notebooks/scripts, skip to §9.

## 8. Pre-delivery checklist

- [ ] Both files complete; cell counts match; Markdown text identical between them.
- [ ] Valid notebook JSON (`nbformat: 4`, no fake outputs) or clean runnable `.py` script.
- [ ] Strict Markdown→Code alternation; steps numbered; each has a Goal/Expected line.
- [ ] Setup cell complete and executable (imports, environment check, mock files generated, ✅).
- [ ] No exercise code cell is empty; each is T1/T2/T3 per §3, and every TODO is one action.
- [ ] Boilerplate (file paths, Tkinter root initialization, plotting frames) is pre-written.
- [ ] No solution code leaked into Markdown.
- [ ] Tkinter topics delivered as standalone `.py` scripts with desktop execution instructions.
- [ ] No manual file uploads or Drive mounts required; scraping includes embedded offline HTML.
- [ ] Every new construct includes an ASCII syntax anatomy diagram and mental model.
- [ ] Includes exactly one Bug Hunt debugging challenge demystifying Python tracebacks.
- [ ] Final cell has 2–3 causal reflection questions; cell runtimes ≤ 5 seconds.

## 9. Prompt generator blueprint

When asked to output a prompt for another agent, fill this structure completely — no
unresolved placeholders, and always paste **real code** (not prose) into the setup and
template sections:

````text
Act as an expert computer science and Python educator for beginners. Please write the complete content for [both / one of] the following files:
1. **[Module Name] Lab Exercise** (`lab_exercise.ipynb` or `app_exercise.py` for Tkinter GUI)
2. **[Module Name] Lab Solution** (`lab_solution.ipynb` or `app_solution.py` for Tkinter GUI)

### Requirements:
- Topic: [Specify: Syntax / Loops / Functions / OOP / Sorting / NumPy / Pandas / Scraping / Tkinter GUI].
- Target Audience: Absolute novices with zero prior coding experience. High-school arithmetic only.
- Deliverable Format: [.ipynb notebook OR standalone .py desktop script].
- Generation Mode: [Generate Both Paired Files / Generate Exercise Only / Generate Solution Only].
- Structure: [Style A: Guided-to-Solo OR Style B: Controlled Showdown].
- Student Exercise code cells are NEVER empty. Guided cells use T1 stubs (`= ...`). Solo tasks use T2 numbered `# TODO 1..n` skeletons (≤ 8 lines) or T3 templates with `___` blanks. Students think through logic, not retype boilerplate.
- Pre-write the setup cell generating all sandbox data/files programmatically (no manual file uploads).
- Include an ASCII Syntax Anatomy diagram for new constructs, one deliberate "Bug Hunt" traceback challenge, and friendly assertion self-checks.

---

### PRE-WRITTEN SETUP (Include this code cell at the start of both files):
[Insert working setup code generating required mock files/data]

---

### TEMPLATE EXAMPLES:
[Insert concrete code templates showing function idioms, class structures, or widget hierarchies]

---

### NOTEBOOK 1: Lab Exercise (Student Practice)
[Step-by-step Markdown challenges, visual syntax diagrams, scaffolded code cells (T1/T2/T3), self-check assertions, and Bug Hunt]

---

### NOTEBOOK 2: Lab Solution (Instructor Reference)
[Exact same structure, fully solved with clean, well-commented code]

### Additional constraints:
- Alternate strictly: one Markdown cell, then one code cell.
- Maintain 100% identical markdown, cell counts, and headings between exercise and solution.
- End with 2–3 causal reflection questions in a Markdown cell.
- Output valid .ipynb JSON documents or fully runnable .py files.
````

## 10. Anti-patterns

One notebook with answers commented out · empty code cells in the exercise file · leaving
students to guess syntax punctuation (missing colons or indentation) · vague multi-step
TODOs like `# TODO: parse the file and return the dict` · a `___` blank so wide the answer
is unguessable · mismatched cell counts or markdown text between the pair · requiring
`files.upload()` or Google Drive mounts · running blocking Tkinter `root.mainloop()` inside
headless Colab notebooks instead of standalone `.py` scripts · relying on live external
websites for scraping labs without embedded fallbacks · bare `except:` without error types ·
intimidating unhandled `AssertionError` tracebacks without friendly error messages · ending
with "Great job!" instead of causal reflection questions · lecturing in abstract jargon
("instantiate an instance", "polymorphic dispatch") without a concrete physical analogy.