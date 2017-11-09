# instance/config.py

POSTGRES = {
    'user': 'odoo',
    'pw': 'odoo',
    'db': 'dream',
    'host': 'localhost',
    'port': '5432',
}

SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES