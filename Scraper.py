from fogbugz import FogBugz
from datetime import datetime, timedelta
import csv


S_FOGBUGZ_URL   = 'https://fogbugz.com/'
S_EMAIL         = ''
S_PASSWORD      = ''
	
fb = FogBugz(S_FOGBUGZ_URL)
fb.logon(S_EMAIL, S_PASSWORD)


resp = fb.search(q='sFixFor="2018.2"',cols='ixBug, ixBugParent, fOpen, sTitle, ixProject, ixArea, sArea, ixStatus, ixPriority,sFixFor, dtFixFor, sVersion, sComputer, c, ixCategory, dtOpened, dtClosed')

filename = "fogbugzData.csv"

csv = open(filename, "w")

columnTitleRow = "ixBug,ixBugParent,fOpen,sTitle,dtDue"
csv.write(columnTitleRow)

for case in resp.cases:
	bugID = case.ixBug.string
	title = case.sTitle.string
	open = case.fOpen.string
	version = case.ixProject.string
	priority = case.ixPriority.string
	status = case.ixStatus.string
	
	row = bugID + "," + title + "," + open + "," + version + "," + priority + "," + status
