# fake DB connection provider
def get_db():
    db = {"users": ["Alice", "Bob", "Charlie"]}
    try:
        yield db
    finally:
        # cleanup if needed
        pass
