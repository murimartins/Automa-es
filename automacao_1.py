import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.expandtesting.com/")
    page.click("div:nth-child(4) > div:nth-child(2) > .card > .card-footer > div > .btn")
    
    def bloqueador(rota, site):
        if "google_vignette" in site.url:
            rota.abort()
        else:
            rota.continue_()

    page.route("**/*", bloqueador)  


    page.goto("https://practice.expandtesting.com/radio-buttons")
    
    botoes = page.query_selector_all("input[type='radio']")
    page.wait_for_selector("input[type='radio']")
    for botao in botoes:
        botao.click()
        page.wait_for_timeout(500)
       


    page.pause()
    input('Teste Finalizado!')




with sync_playwright() as playwright:
    run(playwright)
