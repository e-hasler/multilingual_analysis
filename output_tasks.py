import subprocess

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

all_tasks = []

with open("tasks.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line.startswith("|"):
            continue

        parts = [p.strip() for p in line.split("|") if p.strip()]
        if parts:
            all_tasks.append(parts[0])

print(all_tasks)
