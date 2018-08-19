import os
import sys

print os.getcwd()
sys.path.append(os.getcwd())

from app import create_app


app = create_app()

if __name__ == '__main__':
	print "I am running run"
	app.run()
	print "I am failed"

