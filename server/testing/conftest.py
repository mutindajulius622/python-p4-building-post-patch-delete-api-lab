#!/usr/bin/env python3

import pytest
from app import app
from models import db, Bakery, BakedGood

@pytest.fixture(scope='session', autouse=True)
def setup_database():
    with app.app_context():
        db.create_all()
        
        # Seed initial data
        bakery1 = Bakery(name='Test Bakery')
        bakery2 = Bakery(name='Another Bakery')
        db.session.add(bakery1)
        db.session.add(bakery2)
        db.session.commit()
        
        yield
        db.drop_all()

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))