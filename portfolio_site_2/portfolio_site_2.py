"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        # rx.color_mode.button(position="bottom-left"),
        rx.vstack(
            rx.heading("Joe Rawnsley - Home", size="8"),
            rx.hstack(
                rx.link("Home", href="https://reflex.dev/", flex="1"),
                rx.link("About", href="https://reflex.dev/", flex="1"),
                rx.link("Contact", href="https://reflex.dev/", flex="1"),
                rx.link("Projects", href="https://reflex.dev/", flex="1"),
                justify="center"
            ),
        rx.text("I'm Joe Rawnsley, an apprentice software developer and devops engineer based in Manchester. Check out the section links above for more info."),
        rx.image(src="/face.jpg")
        ),
    )


style = {
    "background-color": "lightyellow",
    rx.image: {
        "height": "20rem",
        "width": "auto",
        "margin": "auto",
        "border-radius": "5%"
    },
    rx.vstack: {
        "margin": "auto"
    },
    rx.hstack: {
        "width": "100%",
        "margin": "auto",
        "background-color": "lightgreen",
    },
    rx.heading: {
      "text-align": "center"  
    },
    # rx.link: {
    #    "background-color": "lightyellow", 
    # }
}





app = rx.App(
    style=style,
)

app.add_page(index)
