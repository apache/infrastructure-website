Title: CSP builder
slug: tools/csp

<script type="application/ecmascript">
  const reserved_csp_words = ["'wasm-unsafe-eval'", "'unsafe-eval'", "'self'", "'unsafe-inline'", "'unsafe-hashes'", "'inline-speculation-rules'", "'strict-dynamic'", "'report-sample'", "'nonce-[a-f0-9]+'"]
  const csp_entry_re = new RegExp(/(\s*(\S+)\s+(([^; ]+\s*)+);)/gim)
  const all_elements = [
          "script-src",
          "style-src",
          "img-src",
          "frame-ancestors",
          "frame-src",
          "worker-src",
          "default-src"
  ]
  const standard_changed_elems = ["script-src", "style-src", "img-src"]
  async function make_csp(addl_host) {
    const rnd = Math.random().toString(20).substring(0, 8)
    const resp = await fetch(`?csp-${rnd}`, {method: 'HEAD'})
    const current_csp = resp.headers.get("Content-Security-Policy")
    current_csp.matchAll(csp_entry_re).map(x => {console.log(x[1], x[2])})
    if (current_csp) {
      // Turn CSP into a dictionary of key -> list(values)
      const csp_dict = Object.fromEntries(current_csp.matchAll(csp_entry_re).map(x => [x[2], x[3].split(/\s+/)]));
      const res = document.getElementById("csp_log")
      res.innerText = "Current default rules:\n";
      for (const key in csp_dict) {
        res.innerText += `  ${key}: ${csp_dict[key].join(" ")}\n`
      }

      res.innerText += "\n\nSuggested new rules:\n"
      let htaccess = "";
      for (const key in csp_dict) {
        if (document.getElementById(`chk_${key}`) && document.getElementById(`chk_${key}`).checked === true) {
          csp_dict[key].push(addl_host)
        }
        res.innerText += `  ${key}: ${csp_dict[key].join(" ")}\n`
        htaccess += `${key} ${csp_dict[key].join(" ")}; `
      }
      document.getElementById("csp_result").style.display = "block"
      const csptxt = document.getElementById("csp_htaccess");
      csptxt.innerText = `Header Set Content-Security-Policy: ${htaccess}\n`
    }

  }

  function prime_boxes() {
    const wrapper = document.getElementById('sources');
    for (const srcname of all_elements) {
      const element_wrapper = document.createElement('div');
      const chkbox = document.createElement('input');
      chkbox.type = "checkbox";
      chkbox.id = `chk_${srcname}`;
      const label = document.createElement('label');
      label.setAttribute("for", chkbox.id);
      if (standard_changed_elems.includes(srcname)) chkbox.checked = true
      label.innerHTML = `Add hostname to <kbd>${srcname}</kbd>`
      element_wrapper.appendChild(chkbox);
      element_wrapper.appendChild(label);
      wrapper.appendChild(element_wrapper)
    }
  }

</script>
<body onload="prime_boxes()">
<p>This tool allows you to create a custom Content-Security-Policy header for your project website.</p>
<h3>
  Attention: do not reconfigure CSP headers without prior express permission from either VP Data Privacy or the Infrastructure team.
  See our <a href="https://privacy.apache.org/policies/website-policy.html">Website Privacy Policy</a> for a more in-depth rationale.
</h3>
<hr/>
<form onsubmit="make_csp(document.getElementById('addl_host').value); return false;">
  Enter a web URL to add to your project's CSP header: <input id="addl_host" type="text" placeholder="https://some.hostname/"/><br/><br/>
  <hr/>
  <div id="sources">

  </div>
  <br/><br/>
  <input type="submit" value="Generate CSP header">
</form>
<!-- parser log -->
<pre id="csp_log">
  </pre>
<!-- suggested output -->
<div id="csp_result" style="display: none;">
  <h4>Suggested .htaccess contents for updated CSP:</h4>
  <pre id="csp_htaccess" style="color: darkslateblue; background-color: lightgoldenrodyellow; white-space: wrap; max-width: 800px;">
  </pre>
  <b>Note: This is a single line directive.</b>
</div>
</body>
