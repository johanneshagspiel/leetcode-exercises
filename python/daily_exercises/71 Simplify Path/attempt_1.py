class Solution:
    def simplifyPath(self, path: str) -> str:

        split_path = path.split("/")
        canonical_path = []

        for element in split_path:

            if len(element) > 0:
                if element == "..":
                    if len(canonical_path) > 0:
                        canonical_path.pop()
                elif element == ".":
                    continue
                else:
                    canonical_path.append(element)

        return "/" + "/".join(canonical_path)
