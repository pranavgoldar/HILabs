"""Deterministic active-time, retry and tour-placement checks."""
import os
from playwright.sync_api import sync_playwright,expect
BASE=os.environ.get('BASE','http://127.0.0.1:8765')
with sync_playwright() as p:
 b=p.chromium.launch();page=b.new_page();page.add_init_script("localStorage.setItem('hilabs-welcome-v4','1')");page.clock.install();page.goto(BASE+'/#member-mridul');page.clock.fast_forward(3000);page.locator('.mhead a').click();page.clock.fast_forward(1000);page.locator('#notes').fill('Member requests transport.');page.clock.fast_forward(2000);page.locator('[data-callstep=review]').first.click();page.locator('#ok-chk').check();page.locator('#approve-btn').click();page.clock.fast_forward(1000)
 state=lambda:page.evaluate("JSON.parse(localStorage.getItem('hilabs-workbench-session-v4')).state")
 x=state()['stats']['members']['mridul'];assert 2500<=x['prep']<5000;assert 1500<=x['doc']<4000
 page.goto(BASE+'/#member-vraj');page.clock.fast_forward(70000);x=state()['stats']['members']['vraj'];assert 59000<=x['prep']<=61000
 page.evaluate("Object.defineProperty(document,'hidden',{get:()=>true,configurable:true});document.dispatchEvent(new Event('visibilitychange'))");page.clock.fast_forward(20000);assert state()['stats']['members']['vraj']['prep']==x['prep'];page.close()
 page=b.new_page(viewport={'width':390,'height':844});page.goto(BASE);page.locator('[data-extra=welcome-tour]').click()
 for i in range(12):
  page.wait_for_timeout(100);target=page.locator('.spot');assert target.count(),i
  a=target.last.bounding_box();c=page.locator('#tour').bounding_box();assert a is not None,(i,'hidden target');assert a['y']+a['height']<=c['y'] or c['y']+c['height']<=a['y'] or a['x']+a['width']<=c['x'] or c['x']+c['width']<=a['x'],(i,a,c);page.locator('[data-act=tour-next]').click()
 page.goto(BASE+'/#about')
 with page.expect_download() as download:page.locator('a[download]').nth(1).click()
 assert download.value.suggested_filename=='HiLabs_Workbench_Prototype_V3.html'
 b.close()
print('PASS: prep / documentation boundaries, 60-second idle cap, hidden-tab pause, all 12 phone tour positions, full HTML download')
