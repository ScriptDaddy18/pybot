from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/pybot', methods=['POST'])
######
def pybot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'tramites' in incoming_msg:
        msg.body(
            "Que tramite desea consular? 1.Ampliacion de creditos, 2. Matricula, 3. Retiro de curso, 4. Rectificacion de matricula"
        )
        responded = True
    elif '1' in incoming_msg:
        msg.body(
            "Preguntas frecuentes de ampliacion de creditos: 1. Cuales son los requisitos?, 2. Codigo de pago, 3. Que documentos se presentan? 4. A quien se entrega"
        )
        responded = True
    elif '0' in incoming_msg:
        msg.body(
            "Se ejecuta posteriormente a la matricula regular y se requiere que ele alumno tenga un promedio ponderado no menor a trece, la condicion de que no tenga asignatura desaprobada en el ultimo ciclo academico anterior."
        )
        responded = True
    elif '2' in incoming_msg:
        msg.body("No cuento con la teconolgia necesaria para poder hacer eso.")
        responded = True
    elif '3' in incoming_msg:
        msg.body(
            "Los documentos a presentar son un FUT dirigido Decano, boleta de notas del ciclo anterior o record academico y voucher de pago."
        )
        responded = True
    elif '4' in incoming_msg:
        msg.body(
            "Los documentos deben ser entregados en la Escuela profesional de Ingeniera de Sistemas"
        )
        responded = True
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
