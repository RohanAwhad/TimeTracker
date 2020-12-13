import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

conn = "mysql+mysqldb://root:password@localhost:3306/trial"

engine = sa.create_engine(conn)

class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50))

    def __repr__(self):
        return f"<User(name={self.name}, id={self.id})>"

# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
ed_user = User(name='ed')
print(ed_user)
print(ed_user.name, ed_user.id)
session.add(ed_user)
session.commit()
query = session.query(User).filter_by(name='ed')
print(query)
# for user in query.all():
#     session.delete(user)
users = query.all()
# print(dir(users[0]))
print(users[0].__getattribute__('name'))
session.commit()
session.close()