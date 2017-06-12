from . import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', backref='role')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guests', ['Administrators']]))
        db.session.commit()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    role_id = db.Column(db.INTEGER, db.ForeignKey('roles.id')) #外键

    @staticmethod
    def on_created(target, value, initiator):
        target.role = Role.query.filter_by(name='Guests').first()

db.event.listen(User.name, 'set', User.on_created)