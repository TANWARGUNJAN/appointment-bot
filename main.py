from fastapi import FastAPI
from backend import calendar_utils

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Appointment Booking API is running!"}

@app.get("/free-slots")
def get_slots():
    return {"available_slots": calendar_utils.get_free_slots()}

@app.post("/book")
def book():
    return {"status": calendar_utils.book_slot()}

