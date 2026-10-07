// Progressive reading of the EA Funds form: selects the fund, the scope confirmation and "INDIVIDUAL", then prints
// every question that appears. Never types an answer, never clicks submit: nothing is sent.
const { chromium } = require('playwright');
const picks = ['Transformative AI Fund', 'I confirm that I have read the information about the scope', 'INDIVIDUAL – I am seeking funding as an individual'];
(async () => {
  const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
  const browser = await chromium.launch({ proxy, args: ['--ignore-certificate-errors'] });
  const page = await browser.newPage();
  await page.goto('https://av20jp3z.paperform.co/?fund=Transformative%20AI%20Fund', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForTimeout(3000);
  for (const p of picks) {
    try { await page.getByText(p, { exact: false }).first().click({ timeout: 5000 }); } catch (e) { console.error('click failed:', p, e.message.split('\n')[0]); }
    await page.waitForTimeout(1500);
  }
  await page.waitForTimeout(2000);
  const text = await page.evaluate(() => document.body.innerText);
  const i = text.indexOf('Funding from Coefficient Giving');
  console.log(text.slice(i >= 0 ? i : 0));
  await browser.close();
})().catch(e => { console.error('ERROR', e.message); process.exit(1); });
