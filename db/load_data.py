from db.db import db_session
from db.models import Price


def save_user_data(report):
    data = Price(
        offer_id=report['offer_id'], price=report['price'],
        old_price=report['old_price'], min_price=report['min_price'],
        rate = report['rate']
    )
    db_session.add(data)
    db_session.commit()

    