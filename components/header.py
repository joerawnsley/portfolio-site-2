import reflex as rx


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