from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from databases import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks/{task_id}", response_model=schemas.tasks)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.get("/discription/{task_id}", response_model=schemas.tasks)
def read_discription(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_discription(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Discription not found")
    return db_task

@app.get("/status/{task_id}", response_model=schemas.tasks)
def read_status(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_status(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return db_task

@app.post("/tasks/", response_model=schemas.tasks)
def create_task(task: schemas.tasksCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.put("/tasks/", response_model=schemas.tasks)
def update_task(task: schemas.tasksUpdate, db: Session = Depends(get_db)):
    return crud.update_task(db=db, task=task)

@app.delete("/tasks/", response_model=schemas.tasks)
def delete_task(task: schemas.tasksDelete, db: Session = Depends(get_db)):
    return crud.delete_task(db=db, task=task)