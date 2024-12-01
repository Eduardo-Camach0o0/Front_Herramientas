import flet as ft
import requests

def main(page):
    
    chat_log = ft.Column()

    def send_message(e):
        user_message = ft.Text(f"Tú: {user_input.value}", size=18)
        chat_log.controls.append(user_message)

        
        bot_response = ft.Text(f"Bot: {get_bot_response(user_input.value)}", size=18, text_align= ft.TextAlign.LEFT)
        chat_log.controls.append(bot_response)

      
        user_input.value = ""
        page.update()

    def get_bot_response(user_message):

        url = "http://127.0.0.1:5000/mensaje"  # Reemplaza con la URL de tu API
        data = {
            "mensaje": user_message
        }

        response = requests.post(url, json=data)
        print(response)
        if response.status_code == 200:
            print("Datos enviados correctamente:", response.json())

            respuesta = response.json()["respuesta"]
          
            return respuesta
           
        else:
            print("Error en la solicitud:", response.status_code)
        

            return "Gracias por tu mensaje. Por el momento estamos teniendo problemas de comunicacion"

    user_input = ft.TextField(label="Escribe tu mensaje", width=500)
    send_button = ft.ElevatedButton("Enviar", on_click=send_message, height=50, width=100)

    parent_container = ft.Container(
        width=page.width,
        height=800,
        alignment=ft.alignment.center
    )

    chat_container = ft.Container(
        width=700,
        height=900,
        bgcolor="#D3D3D3",
        padding=3,  
        alignment=ft.alignment.center,
        border_radius=10,
        content=ft.Column(
            controls=[
                ft.Container(
                    width=700,
                    height=700,
                    padding=30,
                    border_radius=10,
                    bgcolor=ft.colors.WHITE,
                    content=ft.Column(
                        controls=[chat_log],
                        scroll='auto'  
                    )
                ),
                ft.Row(
                    controls=[
                        user_input,
                        send_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ]
        )
    )

    parent_container.content = chat_container

    page.add(parent_container)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)



