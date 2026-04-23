import os

def load_xsa(folder):

    objects = []

    for file in os.listdir(folder):

        if file.endswith(".hdbprocedure"):

            path = os.path.join(folder, file)

            with open(path, "r") as f:
                code = f.read()

            objects.append({
                "name": file,
                "code": code
            })

    return objects
