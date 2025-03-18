Title: CSP builder
slug: tools/csp


<script type="application/ecmascript">
  // These are reserved words, they can have single quotes around them. TODO: use them?
  const reserved_csp_words = ["'wasm-unsafe-eval'", "'unsafe-eval'", "'self'", "'unsafe-inline'", "'unsafe-hashes'", "'inline-speculation-rules'", "'strict-dynamic'", "'report-sample'", "'nonce-[a-f0-9]+'"]
  const csp_entry_re = new RegExp(/(\s*(\S+)\s+(([^; ]+\s*)+);)/gim)  // Each CSP element follows this pattern
  const standard_changed_elems = ["script-src", "style-src", "img-src"] // Standard headers we might want to edit
  // TODO: checkboxes for more advanced edits?
  async function make_csp(addl_host) {
    const resp = await fetch("https://www.apache.org/CSPTEST", {method: 'HEAD'})
    const current_csp = resp.headers.get("Content-Security-Policy")
    if (current_csp) {
      // Turn CSP into a dictionary of key -> list(values)
      const csp_dict = Object.fromEntries(current_csp.matchAll(csp_entry_re).map(x => [x[2], x[3].split(/\s+/)]));
      const res = document.getElementById("csp_result")
      res.innerText = "Current default rules:\n";
      for (const key in csp_dict) {
        res.innerText += `  ${key}: ${csp_dict[key].join(" ")}\n`
      }

      res.innerText += "\n\nSuggested new rules:\n"
      let htaccess = "";
      for (const key in csp_dict) {
        if (standard_changed_elems.includes(key)) {
          csp_dict[key].push(addl_host)
        }
        res.innerText += `  ${key}: ${csp_dict[key].join(" ")}\n`
        htaccess += `${key} ${csp_dict[key].join(" ")}; `
      }
      document.getElementById("csp_htaccess_title").style.display = "block"
      const csptxt = document.getElementById("csp_htaccess");
      csptxt.innerText += `Header Set Content-Security-Policy: ${htaccess}\n`
    }

  }

</script>


<form onsubmit="make_csp(document.getElementById('addl_host').value); return false;">
  Enter a web URL to add to your project's CSP header: <input type="text" id="addl_host">
</form>
<pre id="csp_result">

</pre>
<h4 id="csp_htaccess_title" style="display: none;">Suggested .htaccess contents for updated CSP:</h4>
<pre id="csp_htaccess" style="color: orangered;">

</pre>
