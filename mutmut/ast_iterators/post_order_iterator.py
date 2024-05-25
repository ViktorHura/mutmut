from .ast_iterator import AST_Iterator


class PostOrder_Iterator(AST_Iterator):
    type = 'PostOrder'

    def _iter(self):
        self.path = []
        self.path_position = 0
        self._precompute_path()

    def _precompute_path(self):
        def visit_node(node):
            if node.type in ('tfpdef', 'import_from', 'import_name'):
                return

            if node.type == 'atom_expr' and node.children and node.children[0].type == 'name' and node.children[0].value == '__import__':
                return

            if node.type == 'expr_stmt':
                if node.children[0].type == 'name' and node.children[0].value.startswith('__') and node.children[0].value.endswith('__'):
                    if node.children[0].value[2:-2] in AST_Iterator.dunder_whitelist:
                        return

                # Avoid mutating pure annotations
            if node.type == 'annassign' and len(node.children) == 2:
                return

            if hasattr(node, 'children'):
                for c in node.children:
                    visit_node(c)

            if node != self.root:
                self.path.append(node)

        visit_node(self.root)

    def _next(self):
        if self.path_position == len(self.path):
            raise StopIteration

        next_node = self.path[self.path_position]
        self.path_position += 1
        return next_node
