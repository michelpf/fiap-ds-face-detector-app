[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://face-validation.streamlit.app)

# Aplicação para Preparação de Foto para Documentos

Esta aplicação (frontend) fornece uma camada de entrada para avaliação de fotos como medida de segurança para on-boarding de aplicações bancárias ou afins.

Os seguintes requisitos precisam estar presentes para a foto ser aceita:

* Uma única foto na imagem
* Ausência de emoções

Após a análise de emoções, a imagem deve ser recortada somente para a região onde se encontra a face.

## Componentes utilizados:

* Frontend: [Streamlit](https://streamlit.io/)
* Serverless backend (AWS Lambda)[https://aws.amazon.com/pt/lambda/]

## Uso

Esta aplicação está configurada no Streamlit Cloud de tal forma que qualquer modificação na branch ```master``` será lançada uma nova atualização.

Para realizar depuração local utilizando o VSCode, utilze o ```launch.json``` que possui as configurações necessárias.
