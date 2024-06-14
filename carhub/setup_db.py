from lib.models import init_db

def main():
    init_db()
    print("Database initialized successfully!")

if __name__ == "__main__":
    main()