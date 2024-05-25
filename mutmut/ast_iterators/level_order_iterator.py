from .ast_iterator import AST_Iterator


class LevelOrder_Iterator(AST_Iterator):
    type = 'LevelOrder'

    def _iter(self):
        self.queue = []
        self._queue_children(self.root)

    def _queue_children(self, node):
        if hasattr(node, 'children'):
            for c in node.children:
                self.queue.append(c)

    def _next(self):
        next_node = None

        while next_node is None:
            if len(self.queue) == 0:
                raise StopIteration

            next_node = self.queue.pop(0)

            if next_node.type in ('tfpdef', 'import_from', 'import_name'):
                next_node = None
                continue

            if next_node.type == 'atom_expr' and next_node.children and next_node.children[0].type == 'name' and next_node.children[0].value == '__import__':
                next_node = None
                continue

            if next_node.type == 'expr_stmt':
                if next_node.children[0].type == 'name' and next_node.children[0].value.startswith('__') and next_node.children[0].value.endswith('__'):
                    if next_node.children[0].value[2:-2] in AST_Iterator.dunder_whitelist:
                        next_node = None
                        continue

            # Avoid mutating pure annotations
            if next_node.type == 'annassign' and len(next_node.children) == 2:
                next_node = None
                continue

        self._queue_children(next_node)
        return next_node