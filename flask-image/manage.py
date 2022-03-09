import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
#from alchemydumps import AlchemyDumps, AlchemyDumpsCommand
migrate = Migrate(app, db)
manager = Manager(app)
#alchemydumps = AlchemyDumps(app, db)

manager.add_command('db', MigrateCommand)
#manager.add_command('alchemydumps', AlchemyDumpsCommand)

if __name__ == '__main__':
    manager.run()