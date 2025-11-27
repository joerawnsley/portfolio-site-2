import reflex as rx
from components.header import header


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        header("Home"),
        rx.text("I'm Joe Rawnsley, an apprentice software developer and devops engineer based in Manchester. Check out the section links above for more info."),
        rx.image(src="/face.jpg", class_name="home")
        ),
