from stepic import db
from stepic.models.mixin import BaseMixin


class User(db.Model, BaseMixin):
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    @property
    def is_active(self):
        """Returns `True` if the user is active."""
        return self.active
