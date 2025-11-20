import reflex as rx

config = rx.Config(
    app_name="portfolio_site_2",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)