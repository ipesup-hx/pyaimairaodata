from pyaimairaodata import EntitySet


class Entity:

    def __init__(
        self,
        entity,
        odata
    ):
        self._entity = entity
        self.name = self._entity.__name__
        self.odata = odata

    def __repr__(self):
        return self.name

    def get_schema(self):
        return self._entity.__odata_schema__["properties"]

    def get_attributes(self):
        return list(
            map(
                lambda prop: prop["name"],
                self.get_schema()
            )
        )

    def __iter__(self):
        return iter(
            [
                EntitySet(
                    entity_set=entity_set,
                    entity=self
                )
                for entity_set in self.odata.query(self)
            ]
        )

    def filter(self, criteria):
        """
        Filtrage d'une entité selon un critère sous la forme d'un dictionnaire de strings ou de listes, indexé par des strings
        """
        # initialisation de la propriété avec le premier couple du dictionnaire
        keys = list(criteria.keys())
        key = keys[0]
        value = criteria[key]
        if isinstance(value, str | int):
            prop = getattr(self._entity, key) == value
        elif isinstance(value, list):
            assert len(value) >= 1
            subprop = getattr(self._entity, key) == value[0]
            for element in value[1:]:
                subprop = subprop | (getattr(self._entity, key) == element)
            prop = subprop
        # construction de la propriété complète
        for key, value in criteria.items():
            if isinstance(value, str | int):
                prop = prop & (getattr(self._entity, key) == value)
            elif isinstance(value, list):
                assert len(value) >= 1
                sub_prop = getattr(self._entity, key) == value[0]
                for element in value[1:]:
                    sub_prop = sub_prop | (getattr(self._entity, key) == element)
                prop = prop & sub_prop
        return [
            EntitySet(
                entity_set=row,
                entity=self
            )
            for row in self.odata.query(self).filter(prop).all()
        ]
