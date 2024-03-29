import datetime

import data
from models import *

db.drop_all()

db.create_all()

for user in data.USERS:
    db.session.add(User(
        id=user['id'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        age=user['age'],
        email=user['email'],
        role=user['role'],
        phone=user['phone']
    ))

for order in data.ORDERS:
    mont_start, day_start, year_start = [int(_) for _ in order['start_date'].split('/')]
    mont_end, day_end, year_end = order['end_date'].split('/')
    db.session.add(Order(
        id=order['id'],
        name=order['name'],
        description=order['description'],
        start_date=datetime.date(year=year_start, month=mont_start, day=day_start),
        end_date=datetime.date(year=int(year_end), month=int(mont_end), day=int(day_end)),
        address=order['address'],
        price=order['price'],
        customer_id=order['customer_id'],
        executor_id=order['executor_id']
    ))

for offer in data.OFFERS:
    db.session.add(Offer(
        id=offer['id'],
        order_id=offer['order_id'],
        executor_id=offer['executor_id']
    ))

db.session.commit()