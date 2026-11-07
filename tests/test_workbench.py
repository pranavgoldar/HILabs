"""Browser regression checks. Run against localhost; never edits source Excel files.
Requires: playwright, openpyxl; browser install via `python -m playwright install chromium webkit`.
Set WORKBENCH_URL for a deployed smoke test and BROWSER_ENGINE for an engine.
"""
import os,json,hashlib
from pathlib import Path
from playwright.sync_api import sync_playwright, expect
ROOT=Path(__file__).resolve().parents[1]
BASE=os.environ.get('WORKBENCH_URL','http://127.0.0.1:8765')
ENGINE=os.environ.get('BROWSER_ENGINE','chromium')
NAMES=['pranav','mridul','vraj','shruti','shlok']
ROUTES=['queue']+[f'{s}-{p}' for s in ['member','outreach'] for p in NAMES]
results={'engine':ENGINE,'layouts':0,'source_records':0,'flows':[]}
with sync_playwright() as p:
 browser=getattr(p,ENGINE).launch()
 page=browser.new_page(viewport={'width':390,'height':844},has_touch=True)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(BASE)
 raw=page.evaluate('window.ANNEX_DATA')
 assert len(raw['records'])==75 and len({r['dataset'] for r in raw['records'].values()})==12
 assert [raw['monday'][x]['Score /100'] for x in ['SYN-004','SYN-001','SYN-003','SYN-005','SYN-002']]==[100,100,90,90,50]
 assert raw['records']['RX-002R']['Transaction status']=='Reversed'
 assert raw['records']['LAB-002B']['Value']==9.6
 # Source controls must always lead to a real annex record.
 for width in [320,390,430,768,1024,1440]:
  page.set_viewport_size({'width':width,'height':900})
  for r in ROUTES:
   page.goto(BASE+'/#'+r)
   page.locator('#app h1').wait_for()
   page.locator('main details').evaluate_all('(els)=>els.forEach(e=>e.open=true)')
   if r.startswith('outreach'):
    page.locator('[data-callstep=review]').first.click()
    page.locator('main details').evaluate_all('(els)=>els.forEach(e=>e.open=true)')
   assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+1'),(width,r,'page overflow')
   unknown=page.locator('[data-src]').evaluate_all('(els)=>els.map(e=>e.dataset.src).filter(id=>!window.ANNEX_DATA.records[id])')
   assert not unknown,(r,unknown)
   assert not page.locator('#app').inner_text().find('undefined')>=0,r
   results['layouts']+=1
 # Every raw record is reachable from its member profile and opens its provenance.
 page.set_viewport_size({'width':390,'height':844})
 for name in NAMES:
  page.goto(BASE+'/#member-'+name)
  page.locator('#evidence').evaluate('(e)=>e.open=true')
  page.locator('.record-directory').evaluate('(e)=>e.open=true')
  ids=page.locator('.record-directory [data-src]').evaluate_all('(els)=>els.map(e=>e.dataset.src)')
  for rid in ids:
   page.locator(f'.record-directory [data-src="{rid}"]').click()
   expect(page.locator('#dlg')).to_be_visible()
   expect(page.locator('#dlg-t')).to_have_text(rid)
   assert str(raw['records'][rid]['member_name']) in page.locator('#dlg').inner_text()
   page.locator('[data-act=close]').click();results['source_records']+=1
 # Queue filtering/search and explicit score explanation.
 page.goto(BASE+'/#queue');page.locator('[data-filter=all]').click()
 assert page.locator('.qrow').count()==5
 page.locator('#q').fill('shlok');assert page.locator('.qrow').count()==1
 page.locator('[data-sel=shlok]').click();expect(page.locator('#pane')).to_contain_text('Shlok')
 page.locator('#q').fill('zzzz');expect(page.locator('.empty')).to_contain_text('No members match')
 page.locator('[data-act=clear]').click()
 # Action accept/edit/dismiss/undo must work, including index 0.
 page.locator('[data-sel=mridul]').click();page.locator('[data-accept="0"]').click()
 expect(page.locator('.act').first).to_contain_text('Added to Maria')
 page.locator('[data-undo="0"]').click();page.locator('[data-edit="0"]').click()
 page.locator('#ed-0').fill('Confirm pills with member and dose with prescriber');page.locator('[data-save="0"]').click()
 expect(page.locator('.act').first).to_contain_text('Confirm pills with member')
 page.locator('[data-dismiss="1"]').click();page.locator('[data-reason="1"]').first.click()
 expect(page.locator('.act').nth(1)).to_contain_text('Dismissed')
 results['flows'].append('queue search, filters, actions and selection')
 # Medication conflict cannot be cleared by member confirmation alone.
 page.goto(BASE+'/#member-mridul');page.locator('[data-fold=resolve-mridul]').evaluate('(e)=>e.open=true')
 page.locator('[data-pick=dose][data-v=a]').click();page.locator('#what-dose').fill('Prescriber confirms 40 mg daily')
 page.locator('[data-who=dose][data-w=Member]').click();expect(page.locator('[data-confirm=dose]')).to_be_disabled()
 page.locator('[data-who=dose][data-w=Prescriber]').click();page.locator('[data-confirm=dose]').click()
 expect(page.locator('#banner')).to_contain_text('Dose conflict resolved')
 results['flows'].append('prescriber-gated dose resolution')
 # Pranav: PCP does not close BH gap; stale safety screen; neutral shared-line script.
 page.goto(BASE+'/#member-pranav');page.locator('#evidence').evaluate('(e)=>e.open=true')
 row=page.locator('.ev tr').filter(has_text='Current safety').last
 expect(row).to_contain_text('Stale');expect(page.locator('#banner')).to_contain_text('does not count')
 page.goto(BASE+'/#outreach-pranav');expect(page.locator('.script')).to_contain_text('Could you please ask Pranav')
 assert page.locator('[data-out=connected]').count()==0
 results['flows'].append('BH evidence, follow-up gap and shared-phone restriction')
 # Vraj: bad phone blocked, unavailable appointment remains unknown.
 page.goto(BASE+'/#outreach-vraj');expect(page.locator('#rt-0')).to_be_disabled()
 page.goto(BASE+'/#member-vraj');page.locator('#evidence').evaluate('(e)=>e.open=true')
 expect(page.locator('.ev')).to_contain_text('Feed down')
 page.locator('[data-fold=investigate-vraj]').evaluate('(e)=>e.open=true')
 page.locator('[data-inv-choice="Could not reach"]').click();page.locator('[data-inv=s1]').click()
 assert 'Setting verified' not in page.locator('#banner').inner_text()
 results['flows'].append('disconnected phone and missing context')
 # All five note journeys: draft remains pending; approve gated; sample counts preserved.
 counts=[]
 for name in NAMES:
  page.goto(BASE+'/#outreach-'+name)
  page.locator('[data-callstep=notes]').first.click()
  page.locator('[data-act=sample]').click();page.locator('[data-act=autodraft]').click()
  expect(page.locator('#assess')).to_be_visible();expect(page.locator('#approve-btn')).to_be_disabled()
  count=page.locator('.arow').evaluate_all('(els)=>els.filter(e=>!e.classList.contains("emp")).length');counts.append(count)
  # Review a real pending value and its source phrase.
  pending=page.locator('.arow.ai').first
  pending.evaluate('(e)=>e.closest("details").open=true');expect(pending.locator('.from')).to_contain_text('From your note:')
  page.locator('#ok-chk').check();page.locator('#approve-btn').click()
  expect(page.locator('.writes')).to_contain_text('received',timeout=5000)
  assert 'demo receipt' in page.locator('#assess').inner_text().lower()
 assert counts==[24,24,15,24,21],counts
 results['flows'].append('all five draft/review/approval journeys: '+str(counts))
 # Saving a partial draft survives reload but never signs it.
 page.goto(BASE+'/#outreach-mridul');page.locator('[data-act=newnote]').click()
 page.locator('#notes').fill('Spoke with member; needs transport to clinic.')
 page.locator('[data-act=savepartial]').click();page.reload()
 expect(page.locator('#notes')).to_have_value('Spoke with member; needs transport to clinic.')
 page.locator('[data-callstep=review]').first.click();expect(page.locator('#approve-btn')).to_be_disabled()
 results['flows'].append('local draft restore without approval')
 # Editing notes invalidates old AI suggestions and approval.
 page.locator('[data-callstep=notes]').first.click();page.locator('[data-act=autodraft]').click()
 page.locator('#ok-chk').check();page.locator('[data-callstep=notes]').first.click();page.locator('#notes').fill('No successful contact.')
 page.locator('[data-callstep=review]').first.click();expect(page.locator('#approve-btn')).to_be_disabled();assert page.locator('.arow.ai').count()==0
 # Manual path still works with AI paused; feed outage changes evidence to unknown.
 page.locator('#demo-options').evaluate('(e)=>e.open=true');page.locator('#t-ai').check()
 page.locator('[data-callstep=notes]').first.click();expect(page.locator('#draft-btn')).to_be_disabled()
 page.goto(BASE+'/#member-shlok');page.locator('#t-pbm').check();page.locator('#evidence').evaluate('(e)=>e.open=true')
 expect(page.locator('.ev')).to_contain_text('Unknown · pharmacy feed down')
 results['flows'].append('stale draft invalidation, manual fallback and feed failure')
 assert not errors,errors
 results['script_errors']=errors
 browser.close()
print(json.dumps(results,indent=2))
