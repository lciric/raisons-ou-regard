// Imprime une page HTML locale en PDF A4, avec un pied de page numéroté.
// Usage : node imprimer_pdf.js <page.html> <sortie.pdf> <gabarit du pied>
const path = require('path');
let chromium;
try { ({ chromium } = require('playwright')); }
catch (e) { ({ chromium } = require('/opt/node22/lib/node_modules/playwright')); }

(async () => {
  const [src, out, pied] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(src), { waitUntil: 'load' });
  await page.pdf({
    path: out,
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: pied,
    margin: { top: '17mm', bottom: '18mm', left: '16mm', right: '16mm' },
  });
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
