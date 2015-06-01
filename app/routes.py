from flask import Flask, render_template, request, jsonify
import pandas as pd
import json 

app = Flask(__name__)

counties = pd.read_csv('county.csv')
counties['FIPS'] = counties.FIPS.map('{:05}'.format)
unemp = pd.read_csv('unemp.csv')

@app.route('/')
def index():
	return render_template('index.html')
  

@app.route('/data/<year>')
def data(year):
	fips = counties['FIPS'].unique()
	dat = []
	unempByYear = []
	data = unemp.set_index('Year').T
	data = data[int(year)]
	data.columns = ['id', 'rate']
	unempYear = json.dumps([{"id": f.lstrip("0"), "rate": r} for f, r in zip(list(data.index), data.get_values())  ])

	return unempYear

@app.route('/<year>')
def timeseries(year):
	fips = counties['FIPS'].unique()
	dat = []
	unempByYear = []
	data = unemp.set_index('Year').T
	data = data[int(year)]
	data = data.fillna('NA')

	for fip in fips:
		#create a list of county names + FIPS codes
		county = counties[counties['FIPS'] == fip]['FIPS'].get_values()[0]
		num = counties[counties['FIPS'] == fip]['CountyName'].get_values()[0]
		final = {'FIPS':county, 'CountyName':num}
		dat.append(final)

		#create a list of data by FIPS for given year
		# rate = data['fips' == str(fip)]
		# new = {'id':str(fip), 'rate': rate}
		# unempByYear.append(new)
	countyName = json.dumps(dat)
	unempYear = json.dumps([{"id": f.lstrip("0"), "rate": r} for f, r in zip(list(data.index), data.get_values())  ])
	yr = json.dumps(int(year))

	return render_template('year.html', title = 'Year View', county = countyName, unemp = unempYear, year = yr)

@app.route('/county/<fips>')
def county(fips):
	fips = str(fips)
	county = counties[counties['FIPS'] == fips]
	dat2 = {'FIPS':county.iloc[0]['FIPS'], 'CountyName':county.iloc[0]['CountyName']}

	data = pd.concat([unemp['Year'], unemp[fips]],axis=1)
	data.columns = ['year', 'rate']
	years = data['year'].unique()
	final = []
	for year in years:
		new = {'year': year, 'rate':data[data['year'] == year]['rate'].get_values()[0]}
		final.append(new)

	dat = json.dumps(final)
	return render_template('county.html', title= 'County View', county = dat2, unemp = dat )
  
if __name__ == '__main__':
  app.run(debug=True, threaded=True)