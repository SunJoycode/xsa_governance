import json
import os

def build_semantic(name, explanation):

    semantic = {
        "name": name,
        "description": explanation
    }

    file = name.replace(".hdbprocedure", ".json")

    path = os.path.join("outputs/semantic", file)

    os.makedirs("outputs/semantic", exist_ok=True)

    with open(path, "w") as f:
        json.dump(semantic, f, indent=2)

    return semantic
