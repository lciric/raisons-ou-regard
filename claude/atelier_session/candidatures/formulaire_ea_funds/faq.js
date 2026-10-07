// Renders the EA Funds FAQ and prints its full text, hidden accordion answers included (textContent).
const { chromium } = require('playwright');
(async () => {
  const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
  const browser = await chromium.launch({ proxy, args: ['--ignore-certificate-errors'] });
  const page = await browser.newPage();
  await page.goto('https://funds.effectivealtruism.org/faq', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForTimeout(3000);
  // open every collapsed element we can find
  for (const sel of ['details', 'button[aria-expanded="false"]']) {
    const els = await page.$$(sel);
    for (const el of els) { try { if (sel === 'details') await el.evaluate(e => e.open = true); else await el.click({ timeout: 1000 }); } catch (e) {} }
  }
  await page.waitForTimeout(2000);
  const text = await page.evaluate(() => document.body.innerText);
  console.log(text);
  await browser.close();
})().catch(e => { console.error('ERROR', e.message); process.exit(1); });
