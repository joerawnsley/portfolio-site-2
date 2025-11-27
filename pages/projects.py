import reflex as rx
from components.header import header

def projects() -> rx.Component:
    return rx.container(
        header("Projects")
    )
    