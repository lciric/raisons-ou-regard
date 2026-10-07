const { chromium } = require('playwright');
(async () => {
  const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
  const browser = await chromium.launch({ proxy, args: ['--ignore-certificate-errors'] });
  const page = await browser.newPage();
  await page.goto('https://funds.effectivealtruism.org/faq', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForTimeout(2500);
  const links = await page.evaluate(() => Array.from(document.querySelectorAll('a')).map(a => [a.innerText.trim(), a.href]));
  for (const [t, h] of links) if (t) console.log(t.slice(0, 100), '|', h);
  await browser.close();
})().catch(e => { console.error('ERROR', e.message); process.exit(1); });
