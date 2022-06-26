from django.apps import apps
from django.db import connection

class _CustomUpdate(object):
    def save_by_hash(self, match_field_hash={}):
        if match_field_hash == {}:
            raise ValueError("input hash cannot be empty")
        self._fields = [self._meta.get_field(name) for name in list(match_field_hash.keys())]

        def _inner_methods_for_validation(self):
            def check_concrete_values(_update_fields):
                return any(not f.concrete or f.many_to_many for f in _update_fields)

            def check_primary_key_values(_update_fields):
                return any(f.primary_key for f in _update_fields)

            if check_concrete_values(self._fields):
                raise ValueError("only concrete Values Should be updated")

            if check_primary_key_values(self._fields):
                raise ValueError("updating primary key not allowed")

        def create_set_string(match_field_hash):
            return ", ".join([f"{i[0]} = '{i[1]}'" for i in match_field_hash.items()])

        _inner_methods_for_validation(self)

        a_l, m_n = self._meta.app_label, self._meta.model_name

        with connection.cursor() as cursor:
            cursor.execute\
                (f"UPDATE {a_l}_{m_n} SET {create_set_string(match_field_hash)} WHERE id = {self.id}")




