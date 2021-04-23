import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from siyu import application
from siyu import db

# app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(application, db)
manager = Manager(application)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
