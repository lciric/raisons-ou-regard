// Prints the links of the EA Funds form (budget template, tax info), after revealing the individual's questions.
const { chromium } = require('playwright');
const picks = ['Transformative AI Fund', 'I confirm that I have read the information about the scope', 'INDIVIDUAL – I am seeking funding as an individual'];
(async () => {
  const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
  const browser = await chromium.launch({ proxy, args: ['--ignore-certificate-errors'] });
  const page = await browser.newPage();
  await page.goto('https://av20jp3z.paperform.co/?fund=Transformative%20AI%20Fund', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForTimeout(3000);
  for (const p of picks) { try { await page.getByText(p, { exact: false }).first().click({ timeout: 5000 }); } catch (e) {} await page.waitForTimeout(1200); }
  await page.waitForTimeout(1500);
  const links = await page.evaluate(() => Array.from(document.querySelectorAll('a')).map(a => [a.innerText.trim().slice(0, 60), a.href]));
  for (const [t, h] of links) console.log(t, '|', h);
  await browser.close();
})().catch(e => { console.error('ERROR', e.message); process.exit(1); });
