import os

def build_semantic(name, explanation):

    semantic = {
        "name": name,
        "description": explanation
    }

    file = name.replace(".hdbprocedure", ".txt").replace(".hdbtablefunction", ".txt")

    path = os.path.join("outputs/semantic", file)

    os.makedirs("outputs/semantic", exist_ok=True)

    with open(path, "w") as f:
        f.write(f"Name: {name}\n\n")
        f.write(explanation)

    return semantic
