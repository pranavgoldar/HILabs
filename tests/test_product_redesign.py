"""Reference-informed design checks; all case data stays frozen."""
import os,json
from playwright.sync_api import sync_playwright,expect
BASE=os.getenv('BASE','http://127.0.0.1:8765');ENGINE=os.getenv('ENGINE','chromium');out={'engine':ENGINE,'layouts':0,'checks':[]};errors=[]
with sync_playwright() as p:
 b=getattr(p,ENGINE).launch();page=b.new_page(viewport={'width':390,'height':844});page.add_init_script("localStorage.setItem('hilabs-welcome-v4','1')");page.on('pageerror',lambda e:errors.append(str(e)));page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
 page.goto(BASE)
 expect(page.locator('.focus-person h2')).to_contain_text('Pranav');expect(page.locator('.focus-card')).to_contain_text('09:00–11:00');assert 'reachable now' not in page.locator('.focus-card').inner_text().lower()
 visible=page.locator('#tabs a:visible').count()+page.locator('#tabs button:visible').count();assert visible==4,visible
 page.locator('[data-product=more]').click();page.locator('#dlg a[href="#trust"]').click();expect(page.locator('#app h1')).to_have_text('Data & trust')
 assert page.locator('.dataset-list button').count()==12
 page.locator('[data-product=dataset]').filter(has_text='Behavioral Health').click();expect(page.locator('#dlg')).to_contain_text('BH-004C');page.locator('[data-src=BH-004C]').click();expect(page.locator('#dlg')).to_contain_text('Current safety unknown');page.locator('[data-act=close]').click()
 page.locator('[data-product=trust-label][data-state=ok]').click();expect(page.locator('#dlg')).to_contain_text('independent');page.locator('[data-act=close]').click();out['checks'].append('four-item phone navigation, 12 datasets and source provenance')
 page.goto(BASE+'/#member-mridul');expect(page.locator('.medicine-compare')).to_contain_text('20 mg daily');expect(page.locator('.medicine-compare')).to_contain_text('40 mg daily');page.locator('[data-product=resolve-dose]').click();expect(page.locator('#what-dose')).to_be_visible();out['checks'].append('medication comparison opens original prescriber-gated review')
 page.goto(BASE+'/#outreach-mridul');page.locator('[data-act=sample]').click();page.locator('[data-act=autodraft]').click();page.locator('[data-product-review="0"]').check();expect(page.locator('.review-overview')).to_contain_text('1 / 10 reviewed');expect(page.locator('#approve-btn')).to_be_disabled();page.locator('[data-product=next-section][data-index="0"]').click();expect(page.locator('#section-1')).to_have_attribute('open','');page.reload();expect(page.locator('[data-product-review="0"]')).to_be_checked();page.locator('#ok-chk').check();page.locator('#approve-btn').click();expect(page.locator('.writes')).to_contain_text('received');page.goto(BASE+'/#saved');expect(page.locator('.saved-item')).to_contain_text('Mridul');expect(page.locator('.saved-item')).to_contain_text('CM receipt recorded');out['checks'].append('section review persists without approving; signed work retains receipt')
 page.goto(BASE+'/#team')
 for value,minutes,buffer in [('10','122','2'),('14','158','38'),('18','194','74')]:
  page.locator('[data-product=scenario][data-minutes="'+value+'"]').click();expect(page.locator('.impact-results')).to_contain_text(minutes+' min');expect(page.locator('.impact-results')).to_contain_text(buffer+' min')
 out['checks'].append('all three time scenarios reproduce the submitted register')
 routes=['queue','team','about','trust','saved']+[f'{s}-{n}' for s in ['member','outreach'] for n in ['pranav','mridul','vraj','shruti','shlok']]
 for width in [320,390,768,1366,1920]:
  page.set_viewport_size({'width':width,'height':900})
  for r in routes:
   page.goto(BASE+'/#'+r);assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),(width,r)
   out['layouts']+=1
 assert not errors,errors;out['console_errors']=errors;b.close()
print(json.dumps(out,indent=2))
