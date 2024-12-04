import json
from typing import Any

with open("input.json") as f:
    data = json.load(f)
    
def search(node: dict[str, Any] | list | str | int, skip: str | None = None) -> int:
    if isinstance(node, int):
        return node
    if isinstance(node, dict):
        if skip is not None and any(x == skip for x in node.values()):
            return 0
        return sum(search(x, skip) for x in node.values())
    if isinstance(node, list):
        return sum(search(x, skip) for x in node)
    return 0

print("Part 1:", search(data))
print("Part 2:", search(data, skip="red"))