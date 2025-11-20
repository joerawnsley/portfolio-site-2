"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

def header(page_title):
    return rx.vstack(
            title(page_title),
            navbar(),
            # rx.color_mode.button(position="bottom-left"),
            )
    
def title(page_title):
    return rx.heading(f"Joe Rawnsley - {page_title}", size="8"),
    
def navbar():
    return rx.hstack(
                rx.link("Home", href="/", flex="1"),
                rx.link("About", href="/about", flex="1"),
                rx.link("Contact", href="https://reflex.dev/", flex="1"),
                rx.link("Projects", href="https://reflex.dev/", flex="1"),
                justify="center"
            )

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        header("Home"),
        rx.text("I'm Joe Rawnsley, an apprentice software developer and devops engineer based in Manchester. Check out the section links above for more info."),
        rx.image(src="/face.jpg")
        ),

def about() -> rx.Component:
    return rx.container(
        header("About"),
        rx.image(src="/face.jpg"),
        rx.text("I'm Joe Rawnsley, an apprentice software developer and devops engineer based in Manchester. Check out the section links above for more info."),
        rx.text("I'm Joe Rawnsley, an apprentice software developer and devops engineer based in Manchester. Check out the section links above for more info."),
        )

style = {
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
    rx.link: {
       "background-color": "lightgreen", 
    }
}





app = rx.App(
    style=style,
    stylesheets=[
        "new_style.css"
    ]
)

app.add_page(index)
app.add_page(about)
