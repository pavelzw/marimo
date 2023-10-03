# Copyright 2023 Marimo. All rights reserved.
import marimo

__generated_with = "0.1.21"
app = marimo.App(width="full")


@app.cell
def __():
    import marimo as mo
    import requests
    return mo, requests


@app.cell
def __(mo):
    mo.md("# PDFs")
    return


@app.cell
def __(mo):
    page = mo.ui.number(1, 10, label="Starting page number")
    page
    return page,


@app.cell
def __(mo, page):
    mo.pdf(
        src="https://arxiv.org/pdf/2104.00282.pdf",
        initial_page=page.value,
        width="100%",
        height="60vh"
    )
    return


@app.cell
def __(mo, page, requests):
    downloaded = requests.get("https://arxiv.org/pdf/2104.00282.pdf")
    # This is still performant as it does not pass the full PDF to the frontend,
    # and instead creates a VirtualFile
    mo.pdf(
        src=downloaded.content,
        initial_page=page.value,
        width="100%",
        height="60vh"
    )
    return downloaded,


if __name__ == "__main__":
    app.run()
