// Imprime le HTML de la carte en PDF A4, par le Chromium de Playwright.
// Usage : NODE_PATH=<modules globaux> node html_vers_pdf.js <carte.html> <sortie.pdf>
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const [source, cible] = process.argv.slice(2);
  const html = fs.readFileSync(source, 'utf8');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: 'load' });
  await page.pdf({
    path: cible,
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate:
      '<div style="font-family: DejaVu Sans, sans-serif; font-size: 7pt; width: 100%; text-align: center; color: #555;">' +
      'La carte des angles déjà pris — 2 octobre 2026 — page <span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    margin: { top: '16mm', bottom: '16mm', left: '15mm', right: '15mm' },
  });
  await browser.close();
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
