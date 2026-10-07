// Clicks each FAQ question about applying and prints the text that the click reveals.
const { chromium } = require('playwright');
const qs = ['How do I apply for funding?', 'What is your process for evaluating applications?', 'How long will it take to receive an application decision?',
  'My request is time-sensitive. Can my application evaluation be expedited?', 'Can I receive feedback on my application?',
  'Can I reapply if my proposal was rejected?', 'Can I get tax advice from EV relating to my grant?',
  'Is there a deadline for completing due diligence after my proposal is recommended for funding?'];
(async () => {
  const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
  const browser = await chromium.launch({ proxy, args: ['--ignore-certificate-errors'] });
  const page = await browser.newPage();
  await page.goto('https://funds.effectivealtruism.org/faq', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForTimeout(2500);
  for (const q of qs) {
    const before = await page.evaluate(() => document.body.innerText);
    try { await page.getByText(q, { exact: true }).first().click({ timeout: 4000 }); } catch (e) { console.log('## ' + q + '\n(click failed)'); continue; }
    await page.waitForTimeout(1200);
    const after = await page.evaluate(() => document.body.innerText);
    const i = after.indexOf(q);
    const added = after.length - before.length;
    console.log('## ' + q + `  (+${added} chars)`);
    console.log(after.slice(i + q.length, i + q.length + Math.max(0, added) + 50).trim());
    console.log();
  }
  await browser.close();
})().catch(e => { console.error('ERROR', e.message); process.exit(1); });
