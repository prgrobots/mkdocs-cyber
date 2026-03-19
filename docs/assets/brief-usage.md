# How to use brief.html in any session

## The URL pattern

Drop an iframe at the top of any session page:

```markdown
<iframe 
  src="../../assets/brief.html?week=8&title=WiFi+Attack+Lab&ref=RBS-2025-008&dest=%23mission-objectives&body=Redback+Systems+management+suspects+an+employee+laptop+was+compromised+via+a+rogue+access+point+at+a+local+café.+Your+team+has+been+tasked+with+replicating+the+attack+in+a+controlled+lab.+Today+you+are+the+attacker.+Next+week%2C+you+write+the+advisory.&objectives=Explain+how+a+deauthentication+attack+works|Set+up+an+evil+twin+AP+on+the+isolated+lab+network|Capture+a+client+reconnect|Document+the+attack+as+an+incident+report"
  width="100%" 
  height="600px"
  style="border:none; background:#050505;"
></iframe>
```

## URL Parameters Reference

| Param | Description | Example |
|---|---|---|
| `week` | Week number | `8` |
| `title` | Mission title | `WiFi+Attack+Lab` |
| `ref` | Incident reference | `RBS-2025-008` |
| `dest` | Where ACCEPT goes | `#mission-objectives` or a full URL |
| `body` | Mission situation text (URL encoded) | `Redback+Systems+suspects...` |
| `intel` | Optional extra intel line | `ACSC+advisory+AA-2024-001` |
| `objectives` | Pipe-separated objective list | `Do+thing+1\|Do+thing+2` |
| `org` | Header org name | `Redback+Systems+%2F%2F+SOC` |

## Tips

- `dest` can point to an anchor on the same page (`#lab-setup`) so the 
  brief and the lab instructions live on one page — brief scrolls away when 
  they click accept.

- URL-encode your body text. Spaces = `+`, commas = `%2C`, slashes = `%2F`,
  apostrophes = `%27`. Use any online URL encoder.

- Keep `body` under ~300 characters for best typing effect timing.

- The `objectives` param uses `|` as separator — no encoding needed for the pipe.

## Week 8 — complete working example

```
brief.html
  ?week=8
  &title=WiFi+Attack+Lab
  &ref=RBS-2025-008
  &dest=%23lab-setup
  &body=Redback+Systems+management+suspects+a+staff+laptop+was+compromised+via+a+rogue+AP+at+a+local+café.+Your+team+must+replicate+the+attack+in+a+controlled+lab+to+understand+the+threat.+Today+you+are+the+attacker.
  &intel=ACSC+Advisory+2024-002%3A+Evil+twin+attacks+targeting+remote+workers+increased+340%25+in+FY24.
  &objectives=Explain+how+deauthentication+attacks+work|Stand+up+an+evil+twin+AP+on+the+lab+network|Capture+a+client+reconnect|Write+a+client+advisory+incident+report
```
