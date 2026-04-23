from agents.xsa_loader import load_xsa
from agents.claude_explainer import explain_logic
from agents.semantic_builder import build_semantic

from publishers.collibra_publisher import publish_collibra
from publishers.ellie_publisher import publish_ellie


def main():

    objects = load_xsa("sample_xsa")

    for obj in objects:

        explanation = explain_logic(
            obj["code"]
        )

        semantic = build_semantic(
            obj["name"],
            explanation
        )

        print("Publishing to Collibra...")
        publish_collibra(semantic)

        print("Publishing to Ellie...")
        publish_ellie(semantic)


if __name__ == "__main__":
    main()
