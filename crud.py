from sqlalchemy.orm import Session
import models, schemas

def get_task(db: Session, task_id: int):
    return db.query(models.tasks).filter(models.tasks.id == task_id).first()

def get_discription(db: Session, task_id: int):
    db_task = db.query(models.tasks).filter(models.tasks.id == task_id).first()
    if db_task :
        return db_task.description
    return None

def get_status(db: Session, task_id: int):
    db_task = db.query(models.tasks).filter(models.tasks.id == task_id).first()
    if db_task :
        return db_task.status
    return None

def create_task(db: Session, task: schemas.tasksCreate):
    db_task = models.tasks(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task: schemas.tasksUpdate):
    db_task = db.query(models.tasks).filter(models.tasks.id == task.id).first()
    if task.title != None:
        db_task.title = task.title
    if task.description != None:
        db_task.description = task.description
    if task.status != None:
        db_task.status = task.status
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task: schemas.tasksDelete):
    db_task = db.query(models.tasks).filter(models.tasks.id == task.id).first()
    db.delete(db_task)
    db.commit()
    return db_task