# Simple Auditor

This is a way to gather information from all my computers at once by running the `audit.py` script. The web service returns a snapshot of every machine statistics.

## Run service
`uvicorn app:app --reload --host 0.0.0.0a`

## Run auditor
`python3 audit.py <config>`

## Config example
```
{
	"ips": [
		"1.2.3.4",
		"5.6.7.8"
	]
}
```
