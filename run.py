from clanscore import app

# If run directly __name__ should equal __main__
# If it would be imported, it would return import file name instead
if __name__ == '__main__':
    app.run(debug=True)
