import flet as ft

def main(page):
    
    chat_log = ft.Column()

    # Función para manejar el envío de mensajes
    def send_message(e):
        user_message = ft.Text(f"Tú: {user_input.value}", size=18)
        chat_log.controls.append(user_message)

        # Respuesta del bot
        bot_response = ft.Text(f"Bot: {get_bot_response(user_input.value)}", size=18)
        chat_log.controls.append(bot_response)

        # Limpiar el campo de entrada
        user_input.value = ""
        page.update()


    def get_bot_response(user_message):
       
        if "hola" in user_message.lower():
            return "¡Hola! ¿Cómo puedo ayudarte hoy?"
        elif "adiós" in user_message.lower():
            return "¡Adiós! Que tengas un buen día."
        else:
            return "Lo siento, no entiendo tu mensaje."

    user_input = ft.TextField(label="Escribe tu mensaje", width=500)

    send_button = ft.ElevatedButton("Enviar", on_click=send_message, height=50, width=100)

    parent_container = ft.Container(
        width=page.width,
        height=page.height,
        alignment=ft.alignment.center
    )

    chat_container = ft.Container(
        width=700,
        height=800,
        bgcolor="#D3D3D3",
        padding=3,  
        alignment=ft.alignment.center,
        border_radius=10,
        content=ft.Column(
            controls=[
                ft.Container(
                    width=700,
                    height=700,
                    padding =30,
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
    