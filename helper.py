import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from io import BytesIO
import base64

def load_data():
    # Read data
    insurance = pd.read_csv(_________)
    
    return(insurance)


def plot_age(data):
    
    # ---- Age group of customer

    def age_grouping(data):
        if(data.age <= __):
            return '19 - 24'
        elif(data.age > __ and data.age <= __) : 
            return '24 - 30'
        elif(data.age > __ and data.age <= __) : 
            return '31 - 35'
        elif(data.age > __ and data.age <= __) : 
            return '36 - 40'
        elif(data.age > __ and data.age <= __) : 
            return '41 - 45'
        elif(data.age > __ and data.age <= __) : 
            return '46 - 50'
        elif(data.age > __ and data.age <= __) : 
            return '51 - 55'
        elif(data.age > __ and data.age <= __) : 
            return '56 - 59'
        else : 
            return '60+'

    data['age group'] = data.apply(age_grouping,axis = 1)

    fraud_data = data[data['fraud_reported'] == ___]
    age_profile = pd.crosstab(index=fraud_data[_______],columns='count')

    ax = _______.plot.barh(title = "Fraud Reported by Age group", 
    legend= False, 
    color = '#c34454', 
    figsize = (8,6))
    
    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png', transparent=True)
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]

    return(result)

def plot_premium(data):

    def tocolor(data):
        if(data.fraud_reported == 'Y'):
            return '#53a4b1'
        else : 
            return '#c34454'
    
    data.fcolor = data.apply(tocolor,axis=1)
    
    # ---- Months as Customer per Policy Annual Premium

    ax = data.plot.scatter(x= ________, 
                       y = __________, 
                       c=data.fcolor,title = "Months as Customer per Policy Annual Premium",
                       figsize=(8, 6))


    # Plot Configuration
    lab_y = mpatches.Patch(color='#53a4b1', label='Y')
    lab_n = mpatches.Patch(color='#c34454', label='N')
    plt.legend(handles = [lab_y ,lab_n])
    plt.xlabel("Months as Customer")
    plt.ylabel("Policy Annual Premium")

    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]

    return(result)



def plot_incident(data):

    def tonum(data):
        if(data.fraud_reported == 'Y'):
            return 1
        else : 
            return 0
    
    data['fnum'] = data.apply(tonum,axis=1)

    timeseries = ______.pivot_table(
                index=_______,
                values=_______,
                aggfunc='count').ffill()

    # ---- Number of Report per Day

    ax = timeseries.plot(legend=False, title = "Number of Fraud per Day",color='#c34454', figsize=(8, 6))

    # Plot Configuration
    plt.xlabel('')

    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]

    return(result)

def plot_report(data):

    df_fraud = data[data.fraud_reported == ___].pivot_table(index=_______,values=______,aggfunc=______)
    
    df_nfraud = data[data.fraud_reported == ____].pivot_table(index=________, values=_______,aggfunc=_______)

    # ---- Police Report Availability

    ax = pd.concat([______,_______],axis=1).plot.bar(stacked = ____,color =['#c34454','#53a4b1'],title = "Police Report Availability", figsize=(8, 6))
    
    # Plot Configuration
    plt.legend(['fraud','not fraud'], bbox_to_anchor=(1, 1))
    plt.xlabel("police report available'")

    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]

    return(result)

