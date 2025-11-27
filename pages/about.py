import reflex as rx
from components.header import header

def about() -> rx.Component:
    return rx.container(
        header("About"),
        rx.image(src="/face.jpg", class_name="about"),
        rx.text("I'm Joe Rawnsley, a dedicated software developer and devops engineer with a passion for building clean, efficient, and user-focused applications. With experience across both front-end and back-end technologies, he enjoys transforming complex problems into simple, elegant solutions. John takes pride in writing high-quality code, learning new tools and frameworks, and collaborating with others to create software that genuinely improves people’s lives."),
        rx.text("Curious by nature and committed to continuous improvement, I value teamwork, clear communication, and thoughtful design. Whether working on a small feature or a large-scale system, I bring reliability, creativity, and a calm, analytical approach to every project."),
        
    )