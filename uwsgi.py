import env
from app import app

if __name__ == "__main__":
  app.run("0.0.0.0", port=env.PORT, debug=env.DEBUG_MODE)