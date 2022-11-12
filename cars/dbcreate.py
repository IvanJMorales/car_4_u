#Imports for database
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

config = {
  "type": "service_account",
  "project_id": "car4u-dd0c1",
  "private_key_id": "2fb93c02e55ec68c0f511ddde81f00293db8a39a",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCcjphmv1PbFDm5\nMdes0T1lPQTQtgeXLe0VibEvLplXxsdxuElLEGua5J+nn673+hEh21/cyeo3R596\ni0zYUoWcYutQl64cbxwpF/9X9wrXAxKwrKnBWkl4eW3BGSnGnoUltJJcujXk5lzk\ntrRpGdlRJgBmSrsTQjZh5rdUwuGO4oMMek2Adh5i08dhIQ/BK9ri715pNsV2LmOn\nM4QGMH8GO42NBXmXvfjaMM7goxPpLhw8wSPkpT2Ezotm64iIPlnVepxnLaMuGEwh\nlTAY8mO9j5dYpmjeuWBWLPBuqUamkZ4EgNTBIcJS8RWx3h8F7/iRfzVjcjKjOS84\nzVs4ITwBAgMBAAECggEAB9LMZN4Mx7bkB5ApEfbG1adN9UwTZwehgGEIHK58dTl2\nwAUQjJK+fdgM7mh5auTxNDrtOHBSpv6KRqptZaYCDUWYMsfRqJQY2Sjc1r1+qi36\nIiAOv53ObBnNVUf3oXhMeQzj/4RCqzSj0b4bl+D1zitS+8miPZ0icJQB91dhxC0T\nioLBM4mcm9cDZwZioGmjvgl98Lm+xvuy5Ee8Y/OtKI5WllQdLDS2AHkfBB8qWNSn\nJswyMSSb9l/0oVjXZlZ1KoZhSItwp5pLZkpww1G5zOVDC/LFhSKolk2zTtVF7y8T\nsvTONPTHs1zm3pY59LcuOGodT2S0Lqij0qNfqI7pEQKBgQDUNi6+Pb/HnGA0642J\nmKnNdHnPWuhddSSDDrazkUrtYFi3+vnQmMOmCHF0d1vEXy0zUFS8L3JBfNsdWSly\nW67+Olm2nsluMH1fuXghUWF1FRIddUoSN0wkIXAcMa036sGFolFNzZDRUQL/YHbL\nYEJ8qevhiXQp3vt0HYasARY/DQKBgQC83IaFT3ffEJWOZD1VAaNDAHVnfGQtAiyD\n9+GtOi/55+YvLU94gcMK4/Nz9AMwlbqPYtIaN4VJfynVmkRpkLRKuRowrG3OWlD5\n9lBA52ujBW1MxM+tgYBUcOeKA+BnfydW/lNku4VSPL5O85g3qud9V+BsM0JO2th3\nPCthcXfTxQKBgGIxlB15SyVdKXMzT7HMjz2/WKHnCcA89SEjjMy4PThrrYGsQy4P\nkfBg1cazeCX8eFjXIe5V8gN1d5oz6Ka+39FJRLvo64HuNAU4N+sK0hKwJkq1PAoD\nxlqtkkepgOJv4Q4p1n8u0ITafI2YoD9pEjrHEZux06uQP0AybV9nvVh9AoGAK8Ay\ncYN9U3F2E+xowN6GQalDiVupoTuVsGSmJQkLwCrWiitG87Wrx0QTS9NFQeYNt9W+\nslAWUnZg7Ji2LHZXLdA/nvLy5RDLHXzQDpkNuFAzh8s4CQus/OLC4JgRTiiIpoB4\nNSeztN9ZftSzeIHg6oqG9MnTHI1aBBUuP36XsbkCgYBBGInbE1XckDOrOFx1d0pN\no8kI2AKLYUXqLTnz3skfXwK6wuGGEjMI7l+lsy5ZvwPt4QnfCM+ryJYuuMornLQc\n8/R/1sh6nAB5mRPcBIdgzKnhLBHK6OttoQESvrAZZpiqkehxNDrGzOace4y+LD/l\njHhU34ROFsrDEoQp302t8g==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-nz6s4@car4u-dd0c1.iam.gserviceaccount.com",
  "client_id": "117304315742518968871",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-nz6s4%40car4u-dd0c1.iam.gserviceaccount.com"
}

def dbcreate():
    cred = credentials.Certificate(config)
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


def dbinsert(database,carid,data):
    database.collection(u"Vehicles").document(f"Car #{carid}").set(data)

