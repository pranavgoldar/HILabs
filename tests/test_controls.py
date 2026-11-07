"""Audit every enabled button/link/checkbox/radio in enumerated route states.
Downloads are verified as downloads; selected radios are verified as selected.
Disabled controls are counted separately. Functional state transitions are covered
by test_submission_features.py. No control count is presented as pilot evidence.
"""
import json,os
from playwright.sync_api import sync_playwright
BASE=os.environ.get('BASE','http://127.0.0.1:8765')
ROUTES=['queue','team','about']+[f'{s}-{n}' for s in ['member','outreach'] for n in ['pranav','mridul','vraj','shruti','shlok']]
results=[];disabled=0;errors=[]
failed_only=json.load(open(os.environ['AUDIT_FAILED_FROM']))['failed'] if os.environ.get('AUDIT_FAILED_FROM') else None
with sync_playwright() as p:
 b=p.chromium.launch();page=b.new_page(viewport={'width':1366,'height':900});page.set_default_timeout(2000);page.add_init_script("localStorage.removeItem('hilabs-workbench-session-v4');localStorage.setItem('hilabs-welcome-v4','1');for(const k of ['pranav','mridul','vraj','shruti','shlok'])localStorage.removeItem('hilabs-draft-'+k)")
 page.on('pageerror',lambda e:errors.append(str(e)));page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
 def setup(route,phase):
  page.goto(BASE+'/#'+route)
  page.evaluate("localStorage.removeItem('hilabs-workbench-session-v4');for(const k of ['pranav','mridul','vraj','shruti','shlok'])localStorage.removeItem('hilabs-draft-'+k)")
  page.reload()
  if route=='queue':page.locator('[data-filter=all]').click()
  if phase=='review':page.locator('[data-act=sample]').click();page.locator('[data-act=autodraft]').click()
  page.locator('details').evaluate_all('(els)=>els.forEach(e=>e.open=true)')
  page.locator('button,a,input[type=checkbox],input[type=radio]').evaluate_all('(els)=>els.forEach((e,i)=>e.dataset.auditId=i)')
 def signature():
  return page.evaluate("""()=>{const app=document.querySelector('#app').cloneNode(true);app.querySelector('#session-panel')?.remove();return app.innerHTML+'|'+document.querySelector('#dlg').innerHTML+'|'+document.querySelector('#dlg').open+'|'+document.querySelector('#toast').textContent+'|'+location.hash+'|'+[...document.querySelectorAll('input')].map(e=>e.checked).join(',')}""")
 for route in ROUTES:
  for phase in (['notes','review'] if route.startswith('outreach') else ['base']):
   print('Auditing',route,phase,flush=True)
   setup(route,phase)
   controls=page.locator('button,a,input[type=checkbox],input[type=radio]').evaluate_all("els=>els.map(e=>({id:e.dataset.auditId,label:e.innerText||e.getAttribute('aria-label')||e.id,href:e.getAttribute('href'),disabled:e.disabled,visible:!!e.getClientRects().length,download:e.hasAttribute('download'),type:e.type}))")
   for item in controls:
    if failed_only is not None and not any(r['route']==route and r['phase']==phase and r['control']==item['label'].strip()[:100] for r in failed_only):continue
    if not item['visible']:continue
    if item['disabled']:disabled+=1;continue
    setup(route,phase);el=page.locator('[data-audit-id="'+item['id']+'"]');before=signature();selected=(item['type']=='radio' and el.is_checked()) or el.get_attribute('aria-pressed')=='true'
    try:
     if item['href']=='#app':el.focus()
     if item['download']:
      with page.expect_download(timeout=5000):el.click()
      ok=True
     elif item['href']=='CHANGELOG.md':
      response=page.request.get(BASE+'/CHANGELOG.md');assert response.status==200;el.click();ok='Changelog' in page.locator('body').inner_text() or page.url.endswith('CHANGELOG.md')
     else:
      el.click();page.wait_for_timeout(35);ok=before!=signature() or (selected and page.locator('[data-audit-id="'+item['id']+'"]').count()>0)
     results.append({'route':route,'phase':phase,'control':item['label'].strip()[:100],'pass':bool(ok)})
    except Exception as e:results.append({'route':route,'phase':phase,'control':item['label'].strip()[:100],'pass':False,'error':str(e)[:300]})
 b.close()
out={'responded':sum(r['pass'] for r in results),'tested':len(results),'disabled':disabled,'console_errors':errors,'failed':[r for r in results if not r['pass']],'controls':results}
open(os.environ.get('AUDIT_OUTPUT','/workspace/work/prompt_refresh/controls.json'),'w').write(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k!='controls'},indent=2))
assert out['responded']==out['tested'] and not errors
