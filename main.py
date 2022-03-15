import os
import pandas as pd
import requests
from flask import Flask, request, jsonify, json

app = Flask(__name__)

#Construir as funcionalidades
@app.route('/')
def homepage():
    return 'A API está no ar'
    
@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('./advertising.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)



#rodar a nossa api
app.run(host='0.0.0.0', port = 2000, debug = False)



#tabela = pd.read_csv("advertising.csv")
#total_vendas = tabela['Vendas'].sum()
#print(total_venda
