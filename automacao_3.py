import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.expandtesting.com/")
    page.click("a.btn.btn-outline-primary[href='/add-remove-elements']")

   
    def bloqueador(rota, site):
        if "google_vignette" in site.url:
            rota.abort()
        else:
            rota.continue_()

    page.route("**/*", bloqueador)  


    for elemento in range(10):
        page.click("text=Add Element")
        page.wait_for_timeout(500) 

    botoes_delete = page.query_selector_all("button:has-text('Delete')")
    
    for botao in botoes_delete:
        botao.click()
        page.wait_for_timeout(500) 





    page.pause()
    input('Teste Finalizado!')
    # ---------------------



with sync_playwright() as playwright:
    run(playwright)
