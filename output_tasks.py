import subprocess

# 1. Run lm-eval and save output
with open("tasks.txt", "w") as f:
    subprocess.run(
        ["lm-eval", "ls", "tasks"],
        cwd="lm-evaluation-harness",
        stdout=f,
        stderr=subprocess.STDOUT,
        text=True,
        check=True
    )

print("Saved lm-eval task list to tasks.txt")

# 2. Parse task names
all_tasks = []

with open("tasks.txt", "r") as f:
    for line in f:
        line = line.strip()

        # skip headers and separators
        if not line.startswith("|"):
            continue
        if "Group" in line or "---" in line:
            continue

        # split columns
        cols = [c.strip() for c in line.split("|") if c.strip()]
        if cols:
            all_tasks.append(cols[0])

# 3. Print the list
print(all_tasks)
