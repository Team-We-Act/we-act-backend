from . import create_app

app = create_app()
print(1)
if __name__ == '__main__':
  app.run()