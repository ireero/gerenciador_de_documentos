from app import db

class Requisitions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_of_model = db.Column(db.String(50), nullable=False)
    date_and_time_init_of_requisition = db.Column(db.String(20), nullable=False)
    date_and_time_end_of_requisition = db.Column(db.String(20))
    time_to_end_process = db.Column(db.String(30))
    log = db.Column(db.Text)

    def __init__(self, type_of_model, date_and_time_init_of_requisition) -> None:
        self.type_of_model = type_of_model
        self.date_and_time_init_of_requisition = date_and_time_init_of_requisition