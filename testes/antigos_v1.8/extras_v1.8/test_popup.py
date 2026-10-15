import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width':390,'height':844})
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: errors.append(m.text) if m.type=="error" else None)
        await page.goto("http://localhost:8899/index.html")
        await page.wait_for_timeout(1000)

        # Force nuvemAtiva + NuvemSync to simulate configured cloud without a real Firebase
        await page.evaluate("""() => {
            window.NuvemSync = {
                pronta: () => false,
                configurada: () => true,
                status: () => ({configurada:true, estado:'sem-codigo', temFamiliaNoArquivo:false}),
                definirFamilia: (c) => {
                    const norm = c.toLowerCase().trim().replace(/\\s+/g,'-').replace(/[^a-z0-9-]/g,'');
                    if (norm.length < 6) return false;
                    return norm;
                }
            };
            window.__nuvemCfgArq = 'ok';
        }""")

        # Case 1: normal input mode
        await page.evaluate("pedirCodigoFamilia(false)")
        await page.wait_for_timeout(200)
        visible = await page.eval_on_selector('#codigoOv', 'el => el.classList.contains("open")')
        print("modal open (input mode):", visible)
        inp_display = await page.eval_on_selector('#codigoInput', 'el => getComputedStyle(el).display')
        print("input display:", inp_display)

        # Type a short code -> expect inline error, no alert dialog
        dialog_fired = []
        page.on("dialog", lambda d: (dialog_fired.append(d.message), asyncio.create_task(d.dismiss())))
        await page.fill('#codigoInput', 'ab')
        await page.click('#codigoOkBtn')
        await page.wait_for_timeout(200)
        err_text = await page.eval_on_selector('#codigoErro', 'el => el.textContent')
        print("error text after short code:", repr(err_text))
        still_open = await page.eval_on_selector('#codigoOv', 'el => el.classList.contains("open")')
        print("modal still open after invalid:", still_open)

        # Now valid code
        await page.fill('#codigoInput', 'familia123')
        await page.click('#codigoOkBtn')
        await page.wait_for_timeout(300)
        closed = await page.eval_on_selector('#codigoOv', 'el => !el.classList.contains("open")')
        print("modal closed after valid code:", closed)
        toast_text = await page.eval_on_selector('#toast', 'el => el.textContent')
        print("toast text:", toast_text)

        # Case 2: already in file -> info-only mode
        await page.evaluate("""() => {
            window.NuvemSync.status = () => ({configurada:true, estado:'ok', temFamiliaNoArquivo:true, familia:'familia123'});
        }""")
        await page.evaluate("pedirCodigoFamilia(false)")
        await page.wait_for_timeout(200)
        inp_display2 = await page.eval_on_selector('#codigoInput', 'el => getComputedStyle(el).display')
        cancel_display2 = await page.eval_on_selector('#codigoCancelBtn', 'el => getComputedStyle(el).display')
        ok_text2 = await page.eval_on_selector('#codigoOkBtn', 'el => el.textContent')
        print("info-mode input display:", inp_display2, "cancel display:", cancel_display2, "ok btn text:", ok_text2)

        await page.click('#codigoOkBtn')
        await page.wait_for_timeout(200)
        closed2 = await page.eval_on_selector('#codigoOv', 'el => !el.classList.contains("open")')
        print("info modal closed after Entendi:", closed2)

        print("dialogs fired (should be empty, no native prompt/alert):", dialog_fired)
        print("console/page errors:", errors)

        await page.screenshot(path="/tmp/claude-0/-home-claude/c5588723-0915-55bd-8d56-0ebc0d29b168/scratchpad/popup_shot.png")
        await browser.close()

asyncio.run(main())
