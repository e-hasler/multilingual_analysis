import os

languages = [
    "Albanian", "Arabic", "Armenian", "Azerbaijani", "Basque", "Belarusian", 
    "Bengali", "Bulgarian", "Chinese", "Croatian", "Dutch", "Estonian", 
    "Finnish", "French", "Georgian", "German", "Greek", "Hebrew", "Hindi", 
    "Hungarian", "Indonesian", "Italian", "Japanese", "Kazakh", "Korean", 
    "Lithuanian", "Malay", "Malayalam", "Nepali", "North Macedonian", 
    "Persian", "Polish", "Portuguese", "Russian", "Serbian", "Spanish", 
    "Tagalog", "Tamil", "Telugu", "Turkish", "Ukrainian", "Urdu", "Uzbek", 
    "Vietnamese"
]

print(len(languages)) # should print 44


template = """task: include_base_44_{lang_lower}
dataset_path: CohereLabs/include-base-44
dataset_name: {lang_proper}
test_split: test
output_type: multiple_choice
doc_to_text: "{{{{question}}}}"
doc_to_target: label
doc_to_choice: "{{{{choices}}}}"
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
"""

local_output_dir = "/Users/eleonore.hasler/Documents/multilingual_analysis/custom_tasks"

for lang in languages[:1]: # for testing purpose
    lang_lower = lang.lower()
    with open(f"{local_output_dir}/include_base_44_{lang_lower}.yaml", "w") as f:
        f.write(template.format(lang_lower=lang_lower, lang_proper=lang))

count = len(os.listdir(local_output_dir))
print(f"Generated {count} YAML files in {local_output_dir}")