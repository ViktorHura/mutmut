from abc import ABC, abstractmethod


class AST_Iterator(ABC):
    # We have a global whitelist for constants of the pattern __all__, __version__, etc
    dunder_whitelist = [
        'all',
        'version',
        'title',
        'package_name',
        'author',
        'description',
        'email',
        'version',
        'license',
        'copyright',
    ]

    def __init__(self, AST):
        self.root = AST
        self._iter()

    @abstractmethod
    def _iter(self):
        raise NotImplementedError

    def __iter__(self):
        self._iter()
        return self

    def _generateParentStack(self, node):
        stack = [node]
        while stack[-1].parent is not None:
            stack.append(stack[-1].parent)
        stack.reverse()
        return stack

    @abstractmethod
    def _next(self):
        raise NotImplementedError

    def __next__(self):
        out = self._next()
        return out, self._generateParentStack(out)