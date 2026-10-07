// Renders the EA Funds application form (Paperform) and prints its visible questions, help texts and limits.
const { chromium } = require('playwright');
(async () => {
  const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
  const browser = await chromium.launch({ proxy, args: ['--ignore-certificate-errors'] });
  const page = await browser.newPage();
  await page.goto('https://av20jp3z.paperform.co/?fund=Transformative%20AI%20Fund', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForTimeout(4000);
  const text = await page.evaluate(() => document.body.innerText);
  console.log(text.slice(0, 20000));
  await browser.close();
})().catch(e => { console.error('ERROR', e.message); process.exit(1); });
