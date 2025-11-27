import reflex as rx
from components.header import header




def contact() -> rx.Component:
    return rx.container(
        header("Contact"),
        rx.form(
            rx.vstack(
                rx.input(placeholder="First Name", name="first_name"),
                rx.input(placeholder="Last Name", name="last_name"),
                rx.text_area(placeholder="Your message"),
                rx.button("Submit", type="submit")
            )
        )
    )