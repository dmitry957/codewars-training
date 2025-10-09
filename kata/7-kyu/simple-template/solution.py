import re
def create_template(template):
    pattern = re.compile(r"{{\s*(\w+)\s*}}")
    def filter(**kwargs):
        return pattern.sub(lambda m: str(kwargs.get(m.group(1), "")), template)
    return filter