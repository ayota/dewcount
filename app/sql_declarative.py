import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class QCEW(Base):
	__tablename__ = 'qcew'
	id = Column(Integer, primary_key=True)
	area_fips= Column(String(250), nullable=False)
	own_code= Column(String(250), nullable=False)
	industry_code= Column(String(250), nullable=False)
	agglvl_code= Column(String(250), nullable=False)
	size_code= Column(String(250), nullable=False)
	year= Column(String(250), nullable=False)
	qtr= Column(String(250), nullable=False)
	disclosure_code= Column(String(250), nullable=False)
	annual_avg_estabs_count= Column(String(250), nullable=False)
	annual_avg_emplvl= Column(String(250), nullable=False)
	total_annual_wages= Column(String(250), nullable=False)
	taxable_annual_wages= Column(String(250), nullable=False)
	annual_contributions= Column(String(250), nullable=False)
	annual_avg_wkly_wage= Column(String(250), nullable=False)
	avg_annual_pay= Column(String(250), nullable=False)
	lq_disclosure_code= Column(String(250), nullable=False)
	lq_annual_avg_estabs_count= Column(String(250), nullable=False)
	lq_annual_avg_emplvl= Column(String(250), nullable=False)
	lq_total_annual_wages= Column(String(250), nullable=False)
	lq_taxable_annual_wages= Column(String(250), nullable=False)
	lq_annual_contributions= Column(String(250), nullable=False)
	lq_annual_avg_wkly_wage= Column(String(250), nullable=False)
	lq_avg_annual_pay = Column(String(250), nullable=False)


engine = create_engine(
                'postgresql+psycopg2://USER@localhost/DBNAME'
                )

Base.metadata.create_all(engine)
Base.metadata.bind = engine

#q = QCEW.query.filter(QCEW.area_fips[1] == 11)
# This is just to demonstrate how compiled query would look like.
#print q.statement.compile(dialect=postgresql.dialect())