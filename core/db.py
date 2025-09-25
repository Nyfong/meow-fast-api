# fake DB connection provider
def get_db():
    db = {"users": ["Alice", "Bob", "Charlie"]}
    try:
        yield db
    finally:
        # cleanup if needed
        pass
def get_cyber_model():
    db = [
    {"id": 1, "question": "What is the primary goal of a phishing attack?"},
    {"id": 2, "question": "How does a firewall help protect a network?"},
    {"id": 3, "question": "What is the difference between symmetric and asymmetric encryption?"},
    {"id": 4, "question": "Why is multi-factor authentication (MFA) important for security?"},
    {"id": 5, "question": "What is a DDoS attack, and how can it be mitigated?"},
    ]
    try:
        yield db
    finally:
        # cleanup if needed
        pass
