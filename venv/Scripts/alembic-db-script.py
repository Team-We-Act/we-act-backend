#!d:\programming\hackathon\we-act-backend\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'alembic-migrate==2.5.9.dev0','console_scripts','alembic-db'
__requires__ = 'alembic-migrate==2.5.9.dev0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('alembic-migrate==2.5.9.dev0', 'console_scripts', 'alembic-db')()
    )
