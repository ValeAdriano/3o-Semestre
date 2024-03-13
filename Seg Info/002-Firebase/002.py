import pyrebase  # importar o pyrebase4 no pip

firebaseConfig = {
    "apiKey": "AIzaSyCP1-iygG6gUyTRWrCxHUsOkc6Nfjh5U0Y",
    "authDomain": "adrianopucpr-6a9db.firebaseapp.com",
    "projectId": "adrianopucpr-6a9db",
    "databaseURL": "https://" + "<ID_APP>" + ".firebaseio.com",
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