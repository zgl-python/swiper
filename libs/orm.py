class ModelMixin:
    def to_dict(self, *exclude):
        attr_dict = {}
        for field in self._meta.fields:
            if field.attname not in exclude:
                name = field.attname
                attr_dict[name] = getattr(self, name)
        return attr_dict