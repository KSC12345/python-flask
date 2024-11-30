from app import create_app
from config import load_config

envConfig = load_config()

app = create_app()

if __name__ == '__main__':
    app.run(debug=envConfig.DEBUG,port=envConfig.port)