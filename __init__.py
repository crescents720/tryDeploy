from app import app

if __name__ == '__main__':
    app.run(debug=True, port=3000)

def getApp():
    return app