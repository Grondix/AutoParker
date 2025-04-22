from sqlalchemy.orm import Session
from shared.models.audit import AuditLog

def get_all_logs(db: Session):
    return db.query(AuditLog).all()

def get_logs_for_entity(db: Session, entity: str, entity_id: int):
    return db.query(AuditLog).filter_by(entity=entity, entity_id=entity_id).all()
