from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import sessionmaker
import csv

engine = create_engine('sqlite://', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Output(Base):
	__tablename__ = 'output'

	ID = Column(Integer, primary_key=True)
	LINE_NUMBER = Column(Integer)
	ZONE_NUMBER = Column(Integer)
	TIME_RANGE = Column(String(20))
	DIRECTION = Column(String(8))
	SCHEDULED_RUN_TIME = Column(Integer)
	TOTAL_OPERATING_COST = Column(Float)
	FARE_COLLECTED = Column(Float)
	FAREBOX_RECOVERY = Column(Float)
	DATE_STORED = Column(String(20))
	PCNAME = Column(String(10))
	SIGN_ON_DATE = Column(String(20))
	OPERATING_COST_PER_HOUR = Column(Float)
	RECOVERY_PROCESSING_ID = Column(Integer)
	AGGREGATE_ID = Column(Integer)
	COUNTY = Column(String(20))
	TYPE = Column(String(10))

	def __init__(self, ID, LINE_NUMBER, ZONE_NUMBER, \
		TIME_RANGE, DIRECTION, SCHEDULED_RUN_TIME, TOTAL_OPERATING_COST, \
		FARE_COLLECTED, FAREBOX_RECOVERY, DATE_STORED, PCNAME, SIGN_ON_DATE, \
		OPERATING_COST_PER_HOUR, RECOVERY_PROCESSING_ID, AGGREGATE_ID, COUNTY, TYPE):
		self.ID = ID
		self.LINE_NUMBER = LINE_NUMBER
		self.ZONE_NUMBER = ZONE_NUMBER
		self.TIME_RANGE = TIME_RANGE
		self.DIRECTION = DIRECTION
		self.SCHEDULED_RUN_TIME = SCHEDULED_RUN_TIME
		self.TOTAL_OPERATING_COST = TOTAL_OPERATING_COST
		self.FARE_COLLECTED = FARE_COLLECTED
		self.FAREBOX_RECOVERY = FAREBOX_RECOVERY
		self.DATE_STORED = DATE_STORED
		self.PCNAME = PCNAME
		self.SIGN_ON_DATE = SIGN_ON_DATE
		self.OPERATING_COST_PER_HOUR = OPERATING_COST_PER_HOUR
		self.RECOVERY_PROCESSING_ID = RECOVERY_PROCESSING_ID
		self.AGGREGATE_ID = AGGREGATE_ID
		self.COUNTY = COUNTY
		self.TYPE = TYPE


Base.metadata.create_all(engine)
session = Session()

# read csv file into database
# unsure why primary key ID from csv file does not import correctly; used iterating ID instead
with open('temp.txt', 'rb') as csvfile:
	fb_reader = csv.DictReader(csvfile, delimiter=',')
	ID = 0
	for row in fb_reader:
		session.add(Output(ID, row['\xef\xbb\xbfLINE_NUMBER'], row['ZONE_NUMBER'], \
			row['TIME_RANGE'], row['DIRECTION'], row['SCHEDULED_RUN_TIME'], \
			row['TOTAL_OPERATING_COST'], row['FARE_COLLECTED'], \
			row['FAREBOX_RECOVERY'], row['DATE_STORED'], row['PCNAME'], \
			row['SIGN_ON_DATE'], row['OPERATING_COST_PER_HOUR'], \
			row['RECOVERY_PROCESSING_ID'], row['AGGREGATE_ID'], row['COUNTY'], \
			row['TYPE']))
		ID = ID + 1

# test database by querying for rows with Line number 1
for instance in session.query(Output).filter_by(LINE_NUMBER = 1):
	print instance.LINE_NUMBER, instance.ZONE_NUMBER, instance.FARE_COLLECTED
