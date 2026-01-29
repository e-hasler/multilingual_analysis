import json


def main():
    with open("benchmarks_curation/tydiqa-v1.0-dev.jsonl") as lines:
        for i, line in enumerate(lines):
            if i >= 1:
                break
            data = json.loads(line)
            print(data["question_text"])

if __name__ == "__main__":
    main()