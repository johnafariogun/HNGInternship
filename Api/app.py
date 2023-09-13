from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, insert
from sqlalchemy.orm import declarative_base, sessionmaker
from databases import Database
from typing import List

# FastAPI app
app = FastAPI()

# Database setup

# DATABASE_URL = "postgres://john:a2s1iEDyu4ZXWgr9l5u1GxNlslCRVlly@dpg-cju33jh5mpss73bf9n50-a.oregon-postgres.render.com/dbapi_bho2"
# "postgresql://username:password@localhost/dbname"
DATABASE_URL = "postgresql://bmhgtdbw:9ZqVIv8Q6E1OLZjt_V0uCoSjwqnAF7Wk@stampy.db.elephantsql.com/bmhgtdbw"
database = Database(DATABASE_URL)
print(database)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy models
Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    track = Column(String)
    slack_username = Column(String)

Base.metadata.create_all(bind=engine)
# Pydantic models for request and response
class PersonCreate(BaseModel):
    name: str
    age: int
    track: str
    slack_username: str

class PersonResponse(PersonCreate):
    id: int

# # API endpoints
# @app.post("/person/", response_model=PersonResponse)
# async def create_person(person: PersonCreate):
#     query = Person.insert().values(**person.dict())
#     last_record_id = await database.execute(query)
#     return {"id": last_record_id, **person.dict()}


@app.post("/person/", response_model=PersonResponse)
async def create_person(person: PersonCreate):
    db = SessionLocal()
    try:
        # Create a dictionary containing the data to insert
        person_data = person.model_dump()

        # Use the SQLAlchemy insert construct to perform the INSERT operation
        result = db.execute(insert(Person).values(**person_data))

        # Retrieve the last inserted ID
        last_record_id = result.inserted_primary_key[0]

        # Commit the transaction
        db.commit()

        # Return the created person
        created_person = PersonResponse(id=last_record_id, **person_data)
        return created_person
    except Exception as e:
        # Handle exceptions as needed
        db.rollback()
        raise e
    finally:
        db.close()

@app.get("/person/{name}", response_model=List[PersonResponse])
async def read_person(name: str):
    db = SessionLocal()
    people = db.query(Person).filter(Person.name == name).all()
    db.close()
    return people

@app.get("/person/{id}", response_model=PersonResponse)
async def read_person(id: int):
    db = SessionLocal()
    person = db.query(Person).filter(Person.id == id).first()
    db.close()
    return person

@app.put("/person/{id}", response_model=PersonResponse)
async def update_person(id: int, person: PersonCreate):
    db = SessionLocal()
    try:
        # Retrieve the person record to update
        db_person = db.query(Person).filter(Person.id == id).first()

        if db_person is None:
            raise HTTPException(status_code=404, detail="Person not found")

        # Update the person record with the new data
        for key, value in person.dict().items():
            setattr(db_person, key, value)

        # Commit the transaction
        db.commit()

        # Return the updated person
        updated_person = PersonResponse(id=id, **person.dict())
        return updated_person
    except Exception as e:
        # Handle exceptions as needed
        db.rollback()
        raise e
    finally:
        db.close()

@app.delete("/person/{id}", response_model=PersonResponse)
async def delete_person(id: int):
    db = SessionLocal()
    try:
        # Retrieve the person record to delete
        db_person = db.query(Person).filter(Person.id == id).first()

        if db_person is None:
            raise HTTPException(status_code=404, detail="Person not found")

        # Delete the person record
        db.delete(db_person)

        # Commit the transaction
        db.commit()

        # Return the deleted person
        deleted_person = PersonResponse(id=id, **db_person.__dict__)
        return deleted_person
    except Exception as e:
        # Handle exceptions as needed
        db.rollback()
        raise e
    finally:
        db.close()

# Main function for running with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
