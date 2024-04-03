from plugins import plugin_base


class Simple(plugin_base.FormatterBase):

    data = {'ca': 'cangyue', "name": "caesar"}

    def format(self, data):
        lines = []
        for name, value in sorted(data.items()):
            line = '{name}={value}'.format(
                name=name,
                value=value
            )
            lines.append(line)
        return ''.join(lines)
