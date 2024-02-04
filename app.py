import streamlit as st
import requests
import base64
import json
from PIL import Image

"""
# Cognitive Platforms

## Detecção de Foto para Documentos

Este aplicativo visa detectar face para emissão de documentos, 
validando as seguintes condições e características:

* Existência de face
* Verificação de neutralidade via análise sentimental

Estando as duas condições validadas, a foto está aprovada para emissão de documento.

"""



foto = st.camera_input("Tire sua foto. Procure centralizar seu rosto.")

if foto:

    with st.spinner('Validando condições...'):
        
        bytes_data = foto.getvalue()
        img_base64 = base64.b64encode(bytes_data).decode('utf-8')
 
        payload = {
            "image_base64": img_base64
        }

        payload = json.dumps(payload)

        # URL da sua API Gateway
        endpoint = st.secrets["API-ENDPOINT"]

        response = requests.post(endpoint, json=payload)
        

        # Verifique se a solicitação foi bem-sucedida
        if response.status_code == 200:
            response_data = json.loads(response.text)

            imagem = Image.open(foto)

            largura_total, altura_total = imagem.size

            # Define as coordenadas do retângulo de corte com base nas medidas fornecidas
            left = int(response_data["boundingBox"]["Left"] * largura_total)
            top = int(response_data["boundingBox"]["Top"] * altura_total)
            width = int(response_data["boundingBox"]["Width"] * largura_total)
            height = int(response_data["boundingBox"]["Height"] * altura_total)

            # Recorta a região de interesse (ROI) da imagem
            regiao_recortada = imagem.crop((left, top, left+width, top+height))

            st.image(regiao_recortada)

            st.success('Foto validada com sucesso! Emissão autorizada.', icon="✅")
        else:
            st.error(response.text, icon="🚨")



       