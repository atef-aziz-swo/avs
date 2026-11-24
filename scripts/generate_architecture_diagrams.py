"""Generate editable architecture SVGs and 2x PNGs. Requires resvg-py and Pillow."""
from pathlib import Path
from html import escape
import base64
from PIL import ImageFont
import resvg_py

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/diagrams'
INK='#172B4D'; MUTED='#52657C'; BLUE='#0078D4'; LINE='#BACADD'
FONT=next((str(p) for p in [Path('C:/Windows/Fonts/segoeui.ttf'), Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')] if p.exists()), None)
if not FONT: raise RuntimeError('Install Segoe UI or DejaVu Sans for text-fit verification.')
class Drawing:
 def __init__(self,w,h,title,desc):
  self.w,self.h=w,h; self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(title)}</title><desc>{escape(desc)}</desc>',f'<rect width="{w}" height="{h}" fill="#F4F7FB"/>','<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0 L8 4 L0 8" fill="#0078D4"/></marker></defs>']
 def box(self,x,y,w,h,fill='white',stroke=LINE,r=14,dash=False):
  self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"'+(' stroke-dasharray="9 7"' if dash else '')+'/>')
 def text(self,x,y,s,size=24,color=INK,bold=False,maxw=None):
  if maxw:
   width=ImageFont.truetype(FONT,size).getlength(s)
   assert width<maxw, f'Text overflow: {s} ({width}>{maxw})'
  self.parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Segoe UI, Arial, sans-serif" font-size="{size}" font-weight="{600 if bold else 400}">{escape(s)}</text>')
 def icon(self,key,x,y,size=60):
  data=base64.b64encode((OUT/'icons'/f'{key}.svg').read_bytes()).decode()
  self.parts.append(f'<image x="{x}" y="{y}" width="{size}" height="{size}" preserveAspectRatio="xMidYMid meet" xlink:href="data:image/svg+xml;base64,{data}"/>')
 def card(self,x,y,w,h,title,lines=(),icon=None,fill='white',size=25):
  self.box(x,y,w,h,fill)
  tx=x+24
  if icon: self.icon(icon,x+22,y+22,54); tx=x+94
  self.text(tx,y+44,title,size,bold=True,maxw=w-(tx-x)-20)
  for i,line in enumerate(lines): self.text(x+24,y+89+i*30,line,22,MUTED,maxw=w-45)
 def line(self,points,arrow=True,dash=False,color=BLUE):
  self.parts.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{color}" stroke-width="3" stroke-linejoin="round"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="9 7"' if dash else '')+'/>')
 def badge(self,x,y,n):
  self.parts.append(f'<circle cx="{x}" cy="{y}" r="20" fill="{BLUE}"/>'); self.text(x-7,y+8,str(n),22,'white',True)
 def header(self,title,subtitle):
  self.text(60,68,'AVS  /  TECHNICAL ARCHITECTURE',21,BLUE,True)
  self.text(60,121,title,39,bold=True,maxw=self.w-120)
  self.text(60,162,subtitle,23,MUTED,maxw=self.w-120)
 def save(self,name):
  self.parts.append('</svg>'); svg='\n'.join(self.parts)
  (OUT/f'{name}.svg').write_text(svg,encoding='utf-8')
  (OUT/f'{name}.png').write_bytes(resvg_py.svg_to_bytes(svg_string=svg,zoom=2))
  print(f'{name}: {self.w} x {self.h}; PNG {self.w*2} x {self.h*2}')

# Page 1: deployment topology. Shared hub services are reused, not dedicated per AVS.
d=Drawing(2400,1710,'AVS Azure landing-zone reference design','Proposed private Azure hub-and-spoke hosting for AVS, with on-premises Citrix connectivity and local application data.')
d.header('Azure landing-zone reference design','Optional Azure hosting for the same Linux product  |  Private workload  |  NetScaler ADC & Gateway 14.1 first')
d.box(500,200,1840,195,'#EAF2FB','#98BADE')
d.text(526,235,'AZURE TENANT  /  LANDING-ZONE GUARDRAILS',23,BLUE,True)
d.card(525,253,565,120,'Azure Policy + RBAC',['Inherited policy, tags and least privilege'],icon='policy')
d.card(1110,253,565,120,'Microsoft Entra ID',['AVS OIDC + MFA; conditional on integration'],size=25)
d.card(1695,253,620,120,'Azure Monitor  ·  optional',['Host health; redact application telemetry'],icon='monitor')
# Site
d.box(60,435,390,900,'#FFFFFF','#A9BACD')
d.text(84,478,'CORPORATE / CITRIX SITE',22,bold=True)
d.card(85,520,340,155,'Operators & reviewers',['Internal browser access','HTTPS 443 to private VM'])
d.card(85,760,340,190,'NetScaler 14.1',['ADC / Gateway management','Restricted read-only identity','No user traffic through AVS'])
d.card(85,1050,340,185,'Source access',['Vendor advisories; NVD / KEV','Corporate egress or proxy','Offline import also supported'])
# Connectivity subscription
d.box(500,435,600,900,'#EFF6FE','#7FA9D4')
d.text(526,478,'PLATFORM  /  CONNECTIVITY SUBSCRIPTION',22,BLUE,True)
d.icon('vnet',528,498,40); d.text(585,530,'Shared hub virtual network',25,bold=True)
d.card(550,565,500,155,'Azure VPN Gateway',['GatewaySubnet','Private site-to-site connectivity'],icon='gateway')
d.card(550,790,500,185,'Azure Firewall',['AzureFirewallSubnet','Inspected hybrid and internet routes','Allowlisted destinations and ports'],icon='firewall')
d.card(550,1070,500,160,'Azure Bastion',['AzureBastionSubnet','Private VM administration'],icon='bastion')
d.text(526,1298,'Reuse existing hub services where available.',22,MUTED,maxw=550)
# Workload subscription
d.box(1150,435,1190,900,'#F0F8F6','#8FB9AE')
d.text(1178,478,'CORP MANAGEMENT GROUP  /  AVS WORKLOAD SUBSCRIPTION',22,'#26715F',True)
d.text(1178,520,'rg-avs-prod  /  spoke VNet  /  illustrative address plan: 10.40.0.0/24',24,bold=True,maxw=1110)
d.box(1190,550,1110,440,'#FFFFFF','#8FB9AE')
d.icon('nsg',1210,566,42); d.text(1270,597,'snet-avs  10.40.0.0/27  ·  NSG + route table',25,bold=True)
d.card(1230,630,1030,240,'AVS Linux virtual machine',['Private IP only; no VM public IP','Docker Compose: web, API, worker, optional collector and PostgreSQL','Protected local secret files; authenticated and audited approvals','Single host: controlled updates and tested recovery'],icon='vm',size=30)
d.text(1230,928,'Hub–spoke peering + gateway transit; explicit routes through Azure Firewall',23,MUTED,maxw=1020)
d.card(1190,1030,510,235,'Azure Managed Disks',['Local PostgreSQL + evidence volumes','Encrypted persistent disk storage','Separate OS and data lifecycle'],icon='disk')
d.card(1750,1030,550,235,'Azure Storage account',['Encrypted application backup sets','Blob PE in snet-pe + private DNS','Public network access disabled'],icon='storage')
d.icon('endpoint',2230,1210,42)
# Connectors in reserved gaps
d.line([(450,642),(550,642)],False); d.badge(500,642,1)
d.line([(800,720),(800,790)],False)
d.line([(1050,875),(1125,875),(1125,750),(1230,750)],False); d.badge(1125,810,2)
d.line([(1050,1150),(1125,1150),(1125,825),(1230,825)],True,dash=True)
d.line([(1445,990),(1445,1030)],False)
d.line([(2025,990),(2025,1030)],True); d.badge(2025,1008,3)
# legend and routing notes
d.box(60,1380,2280,245,'#FFFFFF',LINE)
d.text(86,1424,'TRAFFIC & RESPONSIBILITY',24,BLUE,True)
d.text(90,1468,'1  Corporate connectivity: users reach AVS privately; collector reads NetScaler management over the hybrid link.',24,maxw=2200)
d.text(90,1510,'2  Hub–spoke routing: configure peering, gateway transit, NSGs, UDRs and return paths; peering alone is insufficient.',24,maxw=2200)
d.text(90,1552,'3  Backup: host maintenance uploads a coordinated DB + evidence backup through a Blob private endpoint.',24,maxw=2200)
d.text(90,1594,'Solid blue = logical connectivity / data flow. Dashed blue = administration. Control-plane services are shown above.',23,MUTED,maxw=2200)
d.text(60,1670,'PROPOSED REFERENCE  ·  Addresses are illustrative  ·  Existing platform services assumed  ·  No high-availability claim',22,MUTED)
d.save('avs-azure-landing-zone')
# Page 2: VM internals, no Azure PaaS icons used for local containers.
d=Drawing(2400,1700,'AVS Linux VM and container boundaries','Linux Docker Compose runtime, credential boundary, PostgreSQL storage and evidence flows; usable locally or on an Azure VM.')
d.header('Linux VM and container boundaries','Same runtime on premises or in Azure  |  Local PostgreSQL, evidence and secrets  |  No public database endpoint')
d.box(60,205,2280,190,'#EAF2FB','#98BADE')
d.icon('vm',90,236,75); d.text(190,254,'HOST BOUNDARY  /  dedicated Linux VM',30,bold=True)
d.text(190,299,'Internal HTTPS endpoint; restricted host administration; encrypted persistent storage',25,MUTED)
d.text(190,343,'Azure placement: private NIC + NSG + managed data disk. Local placement: equivalent site network and disk controls.',24,MUTED,maxw=2100)
# left external lane
d.card(60,465,365,180,'Internal browser',['Operator / reviewer','Only published app port: 443'])
d.card(60,770,365,185,'Vendor sources',['Allowlisted HTTPS / proxy','Or reviewed offline import'])
d.card(60,1080,365,190,'NetScaler 14.1',['Management API only','Verified TLS; restricted reads','Discovery is separately gated'])
# runtime bounding
d.box(490,435,1390,885,'#FFFFFF','#89B3D7')
d.text(520,480,'APPLICATION RUNTIME  /  containers + host maintenance',25,BLUE,True)
d.card(540,530,570,180,'avs-web',['NGINX + static React interface','TLS termination; /api proxy only'])
d.card(1240,530,570,180,'avs-api',['Authentication + authorization','Inventory, reviews and reports'])
d.card(540,800,570,180,'avs-worker',['Source ingest; evaluate; export','Durable jobs and schedule leases'])
d.card(1240,800,570,180,'PostgreSQL container',['Records, revisions, jobs and audit','Private DB network; no host port'])
d.card(540,1090,570,180,'avs-collector  ·  optional',['Approved read operations only','Only app service with ADC secrets'],fill='#FFF8E8')
d.card(1240,1090,570,180,'Host maintenance  (host)',['Coordinated backup and restore','Controlled migrations and updates'])
# storage lane
d.box(1950,435,390,885,'#EFF6FE','#89B3D7')
d.text(1975,480,'PERSISTENT HOST DATA',23,BLUE,True)
d.card(1980,530,330,180,'Evidence files',['/var/lib/avs/evidence','Finalized artifacts + digests'])
d.card(1980,800,330,180,'PostgreSQL data',['Dedicated local volume','Not Azure Database for','PostgreSQL'])
d.card(1980,1090,330,180,'Secret files',['/etc/avs/secrets','Restricted read-only mounts','Vault integration later'],fill='#FFF8E8')
# Flows arrows explicit gaps
d.line([(425,555),(540,555)]); d.badge(480,555,1)
d.line([(1110,605),(1240,605)]); d.badge(1175,605,2)
d.line([(425,870),(540,870)],False); d.badge(480,870,3)
d.line([(1110,890),(1240,890)]); d.badge(1175,890,4)
d.line([(1525,710),(1525,800)]); d.badge(1525,755,4)
d.line([(1810,605),(1980,605)]); d.badge(1895,605,5)
d.line([(1810,890),(1980,890)],False)
d.line([(540,1160),(425,1160)]); d.badge(480,1160,6)
# collector to DB via horizontal gutter and vertical reserved alley
d.line([(1110,1150),(1165,1150),(1165,1025),(1510,1025),(1510,980)]); d.badge(1300,1025,4)
# secrets path bottom dedicated line, direction to collector
d.line([(2145,1270),(2145,1300),(820,1300),(820,1270)],True,dash=True)
# legend information
d.box(60,1370,2280,250,'white',LINE)
d.text(86,1412,'BOUNDARIES & NUMBERED FLOWS',24,BLUE,True)
for y,s in [(1454,'1  Browser HTTPS.  2  Private API proxy.  3  Worker fetch/import.  4  Private DB access.  5  Authorized evidence reads.  6  ADC reads.'),(1498,'Worker also writes finalized evidence; maintenance reads the coordinated DB + artifact set and sends encrypted backups off host.'),(1542,'Only the collector mounts ADC credentials. API stores opaque credential references. No container receives the Docker socket.'),(1586,'Networks and firewall policy enforce allowed paths; this is a logical component view, not a packet-level cabling diagram.')]: d.text(90,y,s,23,MUTED,maxw=2200)
d.text(60,1663,'INITIAL BASELINE  ·  Local file secrets + authenticated, audited approvals  ·  Cryptographic approval signing is a later option',22,MUTED)
d.save('avs-linux-components')
