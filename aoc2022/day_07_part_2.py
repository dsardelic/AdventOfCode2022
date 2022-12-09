from __future__ import annotations

import itertools
from dataclasses import dataclass, field


@dataclass
class Node:
    name: str
    size: int = 0
    parent: Node = None
    children: list[Node] = field(default_factory=list)


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        folders = resolve_folders(ifile.read().strip().split("\n"))
        folders.sort(key=lambda folder: folder.size)
        used_space = folders[-1].size
        unused_space = 70000000 - used_space
        # assert unused_space < 30000000
        space_to_free_up = 30000000 - unused_space
        return next(
            itertools.dropwhile(lambda folder: folder.size < space_to_free_up, folders)
        ).size


def resolve_folders(output_lines):
    root = Node("/")
    curr_node = None
    folders = [root]
    for output_line in output_lines:
        match output_line.split():
            case ["$", "cd", "/"]:
                curr_node = root
            case ["$", "cd", ".."]:
                curr_node = curr_node.parent
            case ["$", "cd", name]:
                for child in curr_node.children:
                    if child.name == name and child in folders:
                        curr_node = child
                        break
                else:
                    curr_node = None
            case ["$", "ls"]:
                continue
            case ["dir", name]:
                child = Node(name)
                if child not in curr_node.children:
                    curr_node.children.append(child)
                    child.parent = curr_node
                    folders.append(child)
            case [size, name]:
                child = Node(name, int(size))
                if child not in curr_node.children:
                    # curr_node.children.append(child)
                    # child.parent = curr_node
                    increase_sizes_upstream(curr_node, int(size))
    return folders


def increase_sizes_upstream(node, size):
    curr_node = node
    while curr_node:
        curr_node.size += size
        curr_node = curr_node.parent


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
