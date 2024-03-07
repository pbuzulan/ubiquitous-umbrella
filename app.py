import os
from app.main import create_app

app = create_app()

if __name__ == '__main__':
    # app.secret_key = os.environ['APP_SECRET_KEY']
    # os.environ['FLASK_ENV'] = os.environ['ENVIRONMENT']
    app.run(
        port=int(os.getenv("PORT", "5001")),
        host=os.getenv("HOST", "0.0.0.0"),
        use_reloader=False
    )
