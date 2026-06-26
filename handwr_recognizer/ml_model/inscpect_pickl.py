"""This script originally to incpect pickle file, get key, values and verions of the modules"""

import joblib
model_path = "=./digits.pkl"

print("Loading pickle...")
obj = joblib.load(model_path)

print("\nType:", type(obj))

if isinstance(obj, (tuple, list)):
    print("Length:", len(obj))
    for i, item in enumerate(obj):
        print(f"\n--- Item {i} ---")
        print(f"Type: {type(item)}")
        print(f"Content: {item}")
        if hasattr(item, 'predict'):
            print("  --> Has predict() method")
        if hasattr(item, 'transform'):
            print("  --> Has transform() method")
        if hasattr(item, 'steps'):
            print("  --> Pipeline steps:", item.steps)

elif isinstance(obj, dict):
    print("Keys:", list(obj.keys()))
    for k, v in obj.items():
        print(f"\nKey: {k}")
        print(f"Type: {type(v)}")
        print(f"Content: {v}")
else:
    print("Object:", obj)
    if hasattr(obj, 'steps'):
        print("Pipeline steps:", obj.steps)