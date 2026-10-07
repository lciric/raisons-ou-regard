const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + process.argv[2]);
  await page.pdf({ path: process.argv[3], format: 'A4', printBackground: true,
                   displayHeaderFooter: true, headerTemplate: '<span></span>',
                   footerTemplate: '<div style="font-size:7pt;width:100%;text-align:center;color:#666"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
                   margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' } });
  await browser.close();
})();
