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
                rx.link("Contact", href="/contact", flex="1"),
                rx.link("Projects", href="/projects", flex="1"),
                justify="center"
            )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        header("Home"),
        rx.text("I'm Joe Rawnsley, an apprentice software developer and devops engineer based in Manchester. Check out the section links above for more info."),
        rx.image(src="/face.jpg", class_name="home")
        ),

def about() -> rx.Component:
    return rx.container(
        header("About"),
        rx.image(src="/face.jpg", class_name="about"),
        rx.text("I'm Joe Rawnsley, a dedicated software developer and devops engineer with a passion for building clean, efficient, and user-focused applications. With experience across both front-end and back-end technologies, he enjoys transforming complex problems into simple, elegant solutions. John takes pride in writing high-quality code, learning new tools and frameworks, and collaborating with others to create software that genuinely improves people’s lives."),
        rx.text("Curious by nature and committed to continuous improvement, I value teamwork, clear communication, and thoughtful design. Whether working on a small feature or a large-scale system, I bring reliability, creativity, and a calm, analytical approach to every project."),
        rx.hstack(
            rx.heading("rate me!", flex="1"),
            rx.slider(flex="1"),
            rx.button(type="button", flex="1")
        )
        
    )
    

def contact() -> rx.Component:
    return rx.container(
        header("Contact")
    )

def projects() -> rx.Component:
    return rx.container(
        header("Projects")
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
app.add_page(contact)
app.add_page(projects)
