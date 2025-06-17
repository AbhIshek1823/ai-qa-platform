import json
import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

fake = Faker()

def generate_user_data(num_users: int = 100) -> list:
    """Generate synthetic user data"""
    users = []
    for _ in range(num_users):
        user = {
            "user_id": fake.uuid4(),
            "name": fake.name(),
            "email": fake.email(),
            "age": random.randint(18, 70),
            "location": fake.city(),
            "registration_date": str(fake.date_between(start_date='-2y', end_date='today'))
        }
        users.append(user)
    return users

def generate_query_data(num_queries: int = 1000) -> list:
    """Generate synthetic query data"""
    queries = []
    categories = ["finance", "healthcare", "technology", "education", "travel"]
    
    for _ in range(num_queries):
        query = {
            "query_id": fake.uuid4(),
            "text": fake.sentence(nb_words=10),
            "category": random.choice(categories),
            "timestamp": str(fake.date_time_between(start_date='-1y', end_date='today')),
            "user_id": fake.uuid4()
        }
        queries.append(query)
    return queries

def generate_document_data(num_docs: int = 500) -> list:
    """Generate synthetic document data"""
    docs = []
    for _ in range(num_docs):
        doc = {
            "doc_id": fake.uuid4(),
            "title": fake.sentence(nb_words=5),
            "content": " ".join(fake.sentences(nb=5)),
            "tags": [fake.word() for _ in range(random.randint(2, 5))],
            "author": fake.name(),
            "created_at": str(fake.date_time_between(start_date='-1y', end_date='today'))
        }
        docs.append(doc)
    return docs

def save_to_json(data: list, filename: str):
    """Save generated data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    # Generate and save user data
    users = generate_user_data()
    save_to_json(users, "data/users.json")
    
    # Generate and save query data
    queries = generate_query_data()
    save_to_json(queries, "data/queries.json")
    
    # Generate and save document data
    documents = generate_document_data()
    save_to_json(documents, "data/documents.json")

if __name__ == "__main__":
    main()
