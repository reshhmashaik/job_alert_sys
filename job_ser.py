job_data = [
    {"title": "Data Analyst", "location": "Remote", "company": "ABC Corp"},
    {"title": "Python Developer", "location": "New York", "company": "XYZ Inc"},
    {"title": "ML Engineer", "location": "San Francisco", "company": "Tech Giants"}
]

subscribers = []

def get_jobs():
    """Return the list of jobs."""
    return job_data

def subscribe_user(email, preferences):
    """Add a user to the subscription list."""
    subscribers.append({"email": email, "preferences": preferences})
    print(f"Subscribed: {email} for {preferences}")
