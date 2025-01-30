import json
import random

# Paths
INPUT_PATH = "/home/rilyn/project-files/test/vsi-ft-dataset/data/qa_pairs/all_qa/fixed_dataset_fixedd.json"
OUTPUT_PATH = "/home/rilyn/project-files/test/vsi-ft-dataset/data/qa_pairs/all_qa/fixed_dataset_20_percent.json"

# Load dataset
with open(INPUT_PATH, "r") as f:
    data = json.load(f)

# Determine sample size (1% of dataset)
sample_size = max(1, len(data) // 5)

# Randomly sample 1% of the dataset
sampled_data = random.sample(data, sample_size)

# Save the sampled dataset
with open(OUTPUT_PATH, "w") as f:
    json.dump(sampled_data, f, indent=4)

print(f"✅ Random 1% sample saved to {OUTPUT_PATH} (Size: {sample_size} entries)")
