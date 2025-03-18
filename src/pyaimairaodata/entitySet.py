class EntitySet:

    def __init__(
        self,
        entity_set,
        entity
    ):
        self._entity_set = entity_set
        self.entity = entity
        self.data = entity_set.__odata__.data

    def __repr__(self):
        try:
            return f"{self['Apprenant_Nom_Usage']} {self['Apprenant_Prenom_Usage']}"
        except KeyError:
            return '\n'.join(
                [
                    f"{key} : {value}"
                    for key, value in self.data.items()
                ]
            )

    def __getitem__(self, attribute):
        return self.data[attribute]

    def get(self, attribute):
        return self[attribute]
