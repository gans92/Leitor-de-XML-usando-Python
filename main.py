import xmltodict
import os
import pandas as pd

def get_info(file_name, values):
    with open(f"nfs/{file_name}", "r") as xml_file:
        xml_dict = xmltodict.parse(xml_file.read())

        if "NFe" in xml_dict:
            nf_info = xml_dict["NFe"]["infNFe"]
        else: 
            nf_info = xml_dict["nfeProc"]["NFe"]["infNFe"]
            
        numero_nota = nf_info["@Id"]
        empresa_emissora = nf_info["emit"]["xNome"]
        nome_cliente = nf_info["dest"]["xNome"]
        endereco = nf_info["dest"]["enderDest"]
        
        if "vol" in nf_info["transp"]:
            peso = nf_info["transp"]["vol"]["pesoB"]
        else: 
            peso = "Not specified"

        values.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso])
        

file_list = os.listdir("nfs")

columns = ["numero_nota", "empresa_emissora", "nome_cliente", "endereco", "peso"]
values = []

for file in file_list:
    get_info(file, values)

table = pd.DataFrame(columns=columns, data=values)
table.to_excel("table_nfs.xlsx", index=False)
