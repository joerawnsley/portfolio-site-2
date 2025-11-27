"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

from pages.index import index
from pages.about import about
from pages.contact import contact
from pages.projects import projects


class State(rx.State):
    """The app state."""

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
app.add_page(contact)
app.add_page(projects)
