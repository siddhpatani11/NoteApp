from website import create_app

app = create_app()

# only run the app if this file is run directly
# if we import main.py in another file, we don't want to run the app

if __name__ == '__main__':
    # debug=True means that we don't have to restart the server every time we make a change
    app.run(debug=True)