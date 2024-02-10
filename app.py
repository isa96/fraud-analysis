from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
#from helper import ____

matplotlib.use('Agg')

app = Flask(__name__)

data = load_data()

@app.route("/")
def index():
	# generate value for cards

	# percent_fraud = float(pd.crosstab(index=________,columns='count',normalize=_____).loc['Y']*100)
	# fraud_loss = ___.groupby(________).sum()['total_claim_amount'].loc['Y']
	# average_claim = ___.________.median()

	# compile card values as card_data
	 
	card_data = dict(
		percent_fraud = f'{percent_fraud}%',
		fraud_loss = f'US$ {fraud_loss:,}',
		average_claim = f'US$ {average_claim:,}'
	)

	# generate plot
	# plot_age_res = plot_age(raw)
	# plot_premium_res = plot_premium(raw)
	# plot_incident_res = plot_incident(raw)
	# plot_report_res = plot_report(raw)

	# render to html
	return render_template('index.html',
		#  card_data = card_data, 
		#  plot_age_res=plot_age_res,
		#  plot_premium_res=plot_premium_res,
		#  plot_incident_res=plot_incident_res,
		#  plot_report_res=plot_report_res
		)


if __name__ == "__main__": 
    app.run(debug=True)
