---
created: 2026-10-27
tags: [moc, curl, cli-tools, http]
aliases: [curl roadmap]
---

`curl` from first request to endpoint probing: shaping a request, reading the response, making it reliable, and formatting metadata into clean one-line reports.

The target is reading and writing commands like this one without a cheat sheet:

```bash
curl -s -o /dev/null -w "test eds/token %{http_code} %{time_total}s\n" --max-time 20 https://auth.io/api/auth/eds/token
```

> Teaching Progress: not started. Next topic is the first bullet of "Where curl's output goes".

## Overview

- [[curl transfers data to and from servers over many protocols|curl: transfer data over many protocols]]

## Where curl's output goes

- [ ] curl writes the response body to stdout and progress and errors to stderr
- [ ] -o writes the body to a file, and -o /dev/null throws it away
- [ ] -s silences the progress meter and -S brings errors back

## Shaping the request

- [ ] -X sets the HTTP method, and -d implies POST
- [ ] -H adds a request header, repeatable for each header
- [ ] -d and --json send a request body inline or from a file
- [ ] -u and a Bearer header authenticate a request

## Seeing the response

- [ ] -i prints response headers and -I sends a HEAD request
- [ ] -v traces the full request, response and TLS handshake

## Making requests reliable

- [ ] -L follows redirects
- [ ] -f turns HTTP 4xx and 5xx into a failing exit code
- [ ] --max-time and --connect-timeout bound how long curl waits
- [ ] --retry repeats a request after transient failures
- [ ] curl's exit code reports transport failure, not the HTTP status

## Formatting output with -w

- [ ] -w prints transfer metadata after the response using write-out variables
- [ ] time_namelookup to time_total breaks a request's latency into phases
- [ ] -w @file loads a multi-line report template
- [ ] %{json} dumps every write-out variable as JSON for jq

## Probing endpoints

- [ ] A health probe combines -s, -o /dev/null, -w and --max-time
- [ ] A bash loop over endpoints with printf builds an aligned status table
- [ ] Repeating a request and summarising time_total measures latency spread

### Read more

- [[Linux MOC]]
- [[jq parses, filters, and transforms JSON data on the command line]]
- [[Output redirection operators write command output to files in Linux]]
- [[Bash loops iterate over lists with for or repeat while conditions are true]]
