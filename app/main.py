import time,config

from flask import Flask
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response, render_template

import pymysql 
import json
import operator

app = Flask(__name__, static_url_path='')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/')
def home():
    #return '<b>hi</b>'
    return render_template('test.html', title='Home', msg='Welcome!!!!')


@app.route('/snowDepthPlot',methods = ['GET','POST'])
def snowDepthPlot():
    conn = pymysql.connect(host=config.DB['host'], 
        port=config.DB['port'], 
        user=config.DB['user'],
        passwd=config.DB['passwd'], 
        db=config.DB['db'], autocommit=True) 
    cur = conn.cursor(pymysql.cursors.DictCursor)
    qyear = request.args.get('year')
    if qyear is not None:
        sql = 'SELECT * FROM `snow_data` WHERE YEAR(`Date`) = %s ORDER BY `Date`';
        cur.execute(sql,(qyear))
    else:
        sql = 'SELECT * FROM `snow_data` ORDER BY `Date`';
        cur.execute(sql)
    jsx = []
    jsy = []
    
    for row in cur:
        jsx.append(row['Date'])
        jsy.append(row['Depth'])
    jsdata = {'x':jsx,'y':jsy}
    return render_template('snowPlot.html', title='Snow Plot', data=jsdata,plot='snow')

@app.route('/snowDepthForm')
def snowDepthForm():
    conn = pymysql.connect(host=config.DB['host'], 
        port=config.DB['port'], 
        user=config.DB['user'],
        passwd=config.DB['passwd'], 
        db=config.DB['db'], autocommit=True) 
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT YEAR(`Date`) AS `years` FROM `snow_data` GROUP BY YEAR(`Date`) ORDER BY `Date`;'
    cur.execute(sql)
    years = []
    for row in cur:
        years.append(row['years'])
        
    return render_template('snowForm.html', title='Filter data',years=years)


    
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
