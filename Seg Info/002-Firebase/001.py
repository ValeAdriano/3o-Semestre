import pyrebase  # importar o pyrebase4 no pip

firebaseConfig = {
    "apiKey": "AIzaSyCP1-iygG6gUyTRWrCxHUsOkc6Nfjh5U0Y",
    "authDomain": "adrianopucpr-6a9db.firebaseapp.com",
    "projectId": "adrianopucpr-6a9db",
    "storageBucket": "adrianopucpr-6a9db.appspot.com",
    "messagingSenderId": "1066925779209",
    "appId": "1:1066925779209:web:12380ab9a054c4a9a84bd8",
    "measurementId": "G-M8JW7ER2QM"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
user = input("Digite seu e-mail: ")
password = input("Digite sua senha, com pelo menos 6 caracteres: ")
status = auth.create_user_with_email_and_password(user,password)
print("Resultado: ", status)
pausa = input('Pressione ENTER para finalizar...')
# Baseado em código de https://aicodeconvert.com/
'''

import pyrebase
import getpass

# Configuração do Firebase para sua aplicação web
firebaseConfig = {
    "apiKey": "AIzaSyCP1-iygG6gUyTRWrCxHUsOkc6Nfjh5U0Y",
    "authDomain": "adrianopucpr-6a9db.firebaseapp.com",
    "projectId": "adrianopucpr-6a9db",
    "storageBucket": "adrianopucpr-6a9db.appspot.com",
    "messagingSenderId": "1066925779209",
    "appId": "1:1066925779209:web:12380ab9a054c4a9a84bd8",
    "measurementId": "G-M8JW7ER2QM"
}

# Inicialização do Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Solicita ao usuário o email e a senha
user_email = input("Digite seu e-mail: ")
user_password = input("Digite sua senha, com pelo menos 6 caracteres: ")

try:
    # Tentativa de criar um novo usuário
    auth.create_user_with_email_and_password(user_email, user_password)
    print("Usuário criado com sucesso!")
except Exception as e:
    # Se ocorrer um erro, imprime a mensagem de erro
    print("Erro ao criar o usuário:", e)

# Aguarda o usuário pressionar ENTER antes de finalizar
input('Pressione ENTER para finalizar...')
'''