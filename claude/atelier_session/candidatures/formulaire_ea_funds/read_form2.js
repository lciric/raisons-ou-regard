// Selects the Transformative AI Fund and ticks the scope confirmation, then prints the form's text.
// It never clicks a submit or next button: nothing is sent.
const { chromium } = require('playwright');
(async () => {
  const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
  const browser = await chromium.launch({ proxy, args: ['--ignore-certificate-errors'] });
  const page = await browser.newPage();
  await page.goto('https://av20jp3z.paperform.co/?fund=Transformative%20AI%20Fund', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForTimeout(3000);
  const before = await page.evaluate(() => document.body.innerText.length);
  try { await page.getByText('Transformative AI Fund', { exact: true }).first().click({ timeout: 5000 }); } catch (e) { console.error('fund click:', e.message.split('\n')[0]); }
  await page.waitForTimeout(1500);
  try { await page.getByText('I confirm that I have read the information about the scope', { exact: false }).first().click({ timeout: 5000 }); } catch (e) { console.error('confirm click:', e.message.split('\n')[0]); }
  await page.waitForTimeout(3000);
  const text = await page.evaluate(() => document.body.innerText);
  const buttons = await page.evaluate(() => Array.from(document.querySelectorAll('button')).map(b => b.innerText.trim()).filter(Boolean));
  console.log('chars before', before, 'after', text.length);
  const i = text.indexOf('Basic information');
  console.log(text.slice(i >= 0 ? i : 0, (i >= 0 ? i : 0) + 20000));
  console.log('BUTTONS:', JSON.stringify(buttons));
  await browser.close();
})().catch(e => { console.error('ERROR', e.message); process.exit(1); });
