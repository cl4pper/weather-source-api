from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import DateTime, Integer
from sqlalchemy.sql import func
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
CORS(app)

class Weather(db.Model):
	id = Column(Integer, primary_key=True)
	temperature = Column(Integer, primary_key=False)
	humidity = Column(Integer, primary_key=False)
	created_at = Column(DateTime(timezone=True), server_default=func.now())

	def __repr__(self):
		return f"Registered at: {self.created_at} - Temperature: {self.temperature}C, humid: {self.humidity}"


@app.route('/')
def home():
	return '<h1>Flask REST API</h1>'

if __name__=='__main__':
	app.run(debug=True)
