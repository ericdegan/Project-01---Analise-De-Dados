import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt
from tkinter import ttk





tabela_clientes = pd.read_csv('CadastroClientes.csv', sep=';')
tabela_funcionarios = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
servicos_prest_df = pd.read_excel('BaseServiçosPrestados.xlsx')



def custo_salarios():
    texto_resposta = Text(janela)
    texto_resposta.place(x=130, y=220, width=350, height=100)
    salarioBase = tabela_funcionarios['Salario Base'].sum()
    beneficios = tabela_funcionarios['Beneficios'].sum()
    impostos = tabela_funcionarios['Impostos'].sum()
    valorTotal = salarioBase + beneficios + impostos
    #printando = f'Valor gasto com salario de funcionarios é de R${valorTotal:,.2f}'
    resp = f'Valor gasto com salario de funcionarios é de R${valorTotal:,.2f}'
    texto_resposta.insert(1.0, resp)

def faturamento_empresa():
    texto_resposta = Text(janela)
    texto_resposta.place(x=130, y=220, width=350, height=100)

    servicos_prest_df['Faturamento da Empresa'] = servicos_prest_df['Tempo Total de Contrato (Meses)'] * \
                                                  tabela_clientes['Valor Contrato Mensal']
    faturamento = servicos_prest_df['Faturamento da Empresa'].sum()

    resp = f'Faturamento Total da Empresa foi de R$:{faturamento:,.2f}'
    texto_resposta.insert(1.0, resp)

def porcent_vendas():
    texto_resposta = Text(janela)
    texto_resposta.place(x=130, y=220, width=350, height=100)
    fechou_contrato = 0
    qnt_funcionarios = 0
    qnt_vendas = servicos_prest_df['ID Funcionário'].value_counts()
    for v in qnt_vendas:
        fechou_contrato += 1
    for f in tabela_funcionarios['Nome Completo']:
        qnt_funcionarios += 1

    resp = f'{fechou_contrato / qnt_funcionarios:.2%} dos funcionarios fez alguma venda.'
    texto_resposta.insert(1.0, resp)

def funcionarios_area():
    texto_resposta = Text(janela)
    texto_resposta.place(x=130, y=220, width=350, height=100)

    funcionario_area = tabela_funcionarios[['Area']].value_counts()
    resp = funcionario_area
    texto_resposta.insert(1.0, resp)

    labels = tabela_funcionarios['Area'][0], tabela_funcionarios['Area'][1], tabela_funcionarios['Area'][2], tabela_funcionarios['Area'][3],tabela_funcionarios['Area'][4]
    sizes =  [funcionario_area[0],funcionario_area[1],funcionario_area[2],funcionario_area[3],funcionario_area[4]]
    explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('scaled')
    plt.show()

def media_faturamento_mes():
    texto_resposta = Text(janela)
    texto_resposta.place(x=130, y=220, width=350, height=100)
    tiket_medio = tabela_clientes['Valor Contrato Mensal'].mean()
    resp = f'A média do faturamento mesal é R$:{tiket_medio:,.2f}'
    texto_resposta.insert(1.0, resp)

def salario_real_funcionario():
    def Func_nome():
        texto_resposta = Text(janela)
        texto_resposta.place(x=130, y=220, width=350, height=100)
        tabela_funcionarios['Salario Real'] = tabela_funcionarios['Salario Base'] + tabela_funcionarios['Beneficios'] - tabela_funcionarios['Impostos']
        nome = cb_janela.get()
        salarioReal = tabela_funcionarios[tabela_funcionarios['Nome Completo'] == nome]
        resp = salarioReal[['Nome Completo','Salario Real']]
        texto_resposta.insert(1.0, resp)


    sc_janela = Tk()
    sc_janela.title('Search')
    sc_janela.geometry('200x100')
    lista_funcionarios = tabela_funcionarios['Nome Completo'].to_list()
    lista_funcionarios.sort()

    cb_janela = ttk.Combobox(sc_janela,values = lista_funcionarios)
    cb_janela.set("Adelino Gomes")
    cb_janela.grid (column = 0, row = 0)
    cb_janela.pack()



    bt_combobox = Button(sc_janela, text ='Selecionar', command = Func_nome, font = 'Raleway',bg = '#20bebe',fg = 'white')
    bt_combobox.place(x = 210, y = 204, width = 200, height = 20)
    bt_combobox.pack()

    sc_janela.mainloop()

def venderam_mais():
    texto_resposta = Text(janela)
    texto_resposta.place(x=130, y=220, width=350, height=100)
    venderam_mais_df = servicos_prest_df[['ID Funcionário','Codigo do Servico']].merge(tabela_funcionarios[['Nome Completo','ID Funcionário' ]] , on = 'ID Funcionário')
    venderam_mais = venderam_mais_df[['Nome Completo']].value_counts()
    venderam_mais = venderam_mais.head()
    resp = venderam_mais
    texto_resposta.insert(1.0, resp)



janela = Tk()
janela.geometry('600x400')
janela.title('Analyser')



janela.configure(background = '#2B3648')


botao1 = Button(janela,text = 'Custo Salarios', command = custo_salarios,font = 'Helvetica',bg = '#007f9d',fg = 'white') ## passar sempre a função sem parentes.

botao1.place(x = 90, y = 50, width = 200, height = 20 )

botao2 = Button(janela,text = 'Funcionarios por Area', command = funcionarios_area,font = 'Raleway',bg = '#007f9d',fg = 'white')

botao2.place(x = 90, y = 80, width = 200, height = 20 )

botao3 = Button(janela,text = 'Faturamento Total', command = faturamento_empresa,font = 'Raleway',bg = '#007f9d',fg = 'white')

botao3.place(x = 90, y = 110, width = 200, height = 20 )

botao4 = Button(janela,text = 'Faturamento Mensal', command = media_faturamento_mes,font = 'Raleway',bg = '#007f9d',fg = 'white')

botao4.place(x = 90, y = 140, width = 200, height = 20)

botao5 = Button(janela,text = 'MDV Funcionarios', command = porcent_vendas,font = 'Raleway',bg = '#007f9d',fg = 'white')

botao5.place(x = 315, y = 50, width = 200, height = 20 )

botao6 = Button(janela,text = 'Funcionarios Top Seller', command = venderam_mais,font = 'Raleway',bg = '#007f9d',fg = 'white')

botao6.place(x = 315, y = 80, width = 200, height = 20 )

botao7 = Button(janela,text = 'Salario dos Funcionarios', command = salario_real_funcionario,font = 'Raleway',bg = '#007f9d',fg = 'white')

botao7.place(x = 315, y = 110, width = 200, height = 20 )

botao0 = Button(janela,text = 'Fechar', command = janela.quit,font = 'Raleway',bg = '#007f9d',fg = 'white')

botao0.place(x = 315, y = 140, width = 200, height = 20 )

texto_resposta = ''
resp = ''

janela.mainloop()



