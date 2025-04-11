from pydoc import pager
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.expandtesting.com/")
    page.click("a.btn.btn-outline-primary[href='/drag-and-drop']")


    def bloqueador(rota, site):
        if "google_vignette" in site.url:
            rota.abort()
        else:
            rota.continue_()

    page.route("**/*", bloqueador)  



    elemento_a = page.locator("#column-a")  
    elemento_b = page.locator("#column-b") 
    
    for elemento in range(10):
        elemento_a.drag_to(elemento_b) 
        page.wait_for_timeout(700)



    page.pause()
    input('Teste Finalizado!')
    # ---------------------



with sync_playwright() as playwright:
    run(playwright)

