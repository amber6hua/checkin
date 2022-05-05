from quart import Quart, request, Response

app = Quart(__name__)

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run()