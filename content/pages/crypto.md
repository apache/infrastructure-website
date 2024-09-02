Title: Handling cryptography within an ASF release
license: https://www.apache.org/licenses/LICENSE-2.0

This page provides PMC members with the information they need to ensure U.S. export control laws are satisfied for ASF product distributions that contain, or are designed or modified to use, cryptography for data confidentiality.

**This page is not intended for users of Apache products**. Users should consult the <a href="https://www.apache.org/licenses/exports/" target="_blank">export control status of our products</a>.

**Note**: The regulations covering US export control laws for encryption are continuously changing, and the latest modification of this page, to describe the current state of regulations, was May 24, 2019. 

This page describes the process which should be continued until the Apache VP Legal Affairs approves an updated version.

<h4 id="updates">Notification of Updates to this Page<a class="headerlink" href="#updates" title="Permanent link">&para;</a></h4>

Notices of updates to this page appear on the <a href="https://www.apache.org/foundation/mailinglists.html#foundation-legal" target="_blank">legal-discuss</a> mailing list.

<h2 id="contents">Contents<a class="headerlink" href="#contents" title="Permanent link">&para;</a></h2>

  - <a href="#overview">Overview</a>
  - <a href="#faq">Frequently Asked Questions</a>

<h2 id="overview">Overview<a class="headerlink" href="#overview" title="Permanent link">&para;</a></h2>

The U.S. Government places <a href="https://www.bis.doc.gov/index.php/regulations/commerce-control-list-ccl" target="_blank">restrictions on the export</a> of some types of software, including software employing cryptographic functions. Fortunately, EAR Section 742.15(b) applies to most of the cryptography of concern to the ASF.

PMCs considering including cryptographic functionality within their products, or designing their products to use other software with cryptographic functionality, should take the following steps **before** placing such code on any ASF server, including commits to subversion or git.

  - <a href="#classify">Check the Export Control Classification Number (ECCN)</a>.
  - <a href="#sources">Update the exports page with source links</a>.
  - <a href="#notify">Notify the U.S. Government of the new code</a>.
  - <a href="#inform">Inform users</a>.

<h3 id="classify">Check the Export Control Classification Number (ECCN)<a class="headerlink" href="#classify" title="Permanent link">&para;</a></h3>

Section 742.15(b) of the <a href="https://www.trade.gov/us-export-regulations" target="_blank">Export Administration Regulations (EAR)</a> authorizes exports and reexports, without review, of encryption source and object code provided the following conditions are met:

  - the encryption source code is controlled by ECCN 5D002.
  - the encryption source code will be publicly available (published and made available to the public without restrictions upon its further dissemination).
  - a notification is sent to the U.S. Government's Bureau of Industry and Security (BIS) and the ENC Encryption Request Coordinator at or before making the code publicly available. Current ASF processes satisfy the "publicly available" requirement. The notification requirement is described <a href="#notify">below</a>. However, it is important to ensure the included cryptographic functionality meets the definition of <a href="https://cr.yp.to/export/ear2001/ccl5-pt2.pdf" target="_blank">ECCN D002</a>, which can be summarized as:
    - Software specially designed or modified for the development, production or use of any of the other software of this list, or software designed to certify other software on this list; or
    - Software using a "symmetric algorithm" employing a key length in excess of 56-bits; or
    - Software using an "asymmetric algorithm" where the security of the algorithm is based on: factorization of integers in excess of 512 bits (e.g., RSA), computation of discrete logarithms in a multiplicative group of a finite field of size greater than 512 bits (e.g., Diffie-Hellman over Z/pZ), or other discrete logarithms in a group in excess of 112 bits (e.g., Diffie-Hellman over an elliptic curve).
    - Software designed or modified to perform cryptanalytic functions If the cryptographic functionality is limited to one of the above definitions, it should be classified as ECCN 5D002, and the remaining two steps should be taken (described below). If the release may contain cryptographic functionality beyond what is described above, please contact
the <a href="https://www.apache.org/foundation/leadership" target="_blank">ASF Vice President for Legal Affairs</a>.

<h3 id="sources">Update the Exports Page with Source Links<a class="headerlink" href="#sources" title="Permanent link">&para;</a></h3>

To satisfy the BIS requirements to make source code available for inspection, while minimizing the number of <a href="#notify">notification emails</a> needed to be sent, the ASF maintains a single web page at <a href="https://www.apache.org/licenses/exports/" target="_blank">https://www.apache.org/licenses/exports/</a> with links to the applicable source code for each version of each ASF product classified as ECCN 5D002.

To make updates to this ASF-wide Exports page as simple and consistent as possible, the <a href="https://github.com/apache/www-site/blob/main/data/eccn/eccnmatrix.yaml" target="_blank">source matrix</a> is a .yaml file that anyone with site-dev karma (which includes all PMC chairs) can update. The exports web page is generated from this .yaml file.

Test any edits to the exports page using both the site build process (view `index.html` before committing any changes) and by running the `bisnotice.xsl` transform on the product added/changed (see below). You can probably figure out how to format the information for your project's product by following the example of other projects and reading the page. If you have any further questions about the content, or if you are not sure that a BIS notice is required, please check the <a href="#faq">FAQs</a> first and then bring any remaining questions to the `legal-discuss` mailing list. Note that the product data should only be version-specific if the classification changes (e.g., Apache HTTP Server version 1.3 vs 2.0) or if the link to the controlled source code needs to change, such as if the encryption library included in the product for different releases came from different manufacturers. In addition, it is possible to include both controlled and non-controlled (ECCN "n/a") products in the list, but a BIS notice is only necessary for the products that have at least one version classified as ECCN 5D002.

<h3 id="notify">Notify the U.S. Government of the release<a class="headerlink" href="#notify" title="Permanent link">&para;</a></h3>

After ensuring the distribution's cryptography qualifies for an exemption  under Section 742.15(b) and after ensuring the applicable source code is linked from the
ASF-wide export page, but <strong>before publicly posting the distribution or committing the controlled code</strong>, send an email using the template below.

An XSLT transformer called <a href="https://svn.apache.org/repos/asf/infrastructure/site/trunk/content/licenses/exports/bisnotice.xsl" target="_blank">bisnotice.xsl</a>
can generate the BIS notice for a product based on the XML data. For example, running it as:

```
$ cd {SVNROOT}/infrastructure/site/trunk/</li>
$ svn up</li>
$ cd content/licenses/exports/</li>
$ java -Xbootclasspath/p:../../../lib/xalan.jar org.apache.xalan.xslt.Process \
          -in index.page/eccnmatrix.xml -xsl bisnotice.xsl \
          -param product 'Apache HTTP Server'
```

will result in text output that looks like an email template for the PMC chair to send to the appropriate addresses. A generic example is below. Note that the product parameter selects which product(s) to print based on matching a substring of the product name. The template output is only correct when a single product is matched.

There are also some sample script files in the top-level directory (site/trunk): `bisnotice.cmd` (Windows) and `bisnotice.sh` (Un*x).

```
TO: crypt AT bis.doc.gov, 
       enc AT nsa.gov, 
       web_site AT bis.doc.gov
CC: {applicable project list}
SUBJ: Section 742.15 NOTIFICATION - Encryption</p>

SUBMISSION TYPE:      Section 742.15
SUBMITTED BY:         {PMC member sending email}
SUBMITTED FOR:        Apache Software Foundation
POINT OF CONTACT:     Secretary, Apache Software Foundation
MANUFACTURER(S)       {list of origin of all crypto code, e.g.
                         "OpenSSL Project" or "Apache Software Foundation."
                         If product includes multiple crypto items from 
                         different origins, list all origins.}
PRODUCT NAME/MODEL #: {Apache product name(s) that include the source
                          code found at the URL below, or any binaries
                          that were created by compiling that source code
                          -- do not specify version numbers if the 
                          future versions will use source code found at 
                          the same URL (even if the source is updated at
                          that URL) }
ECCN:                 5D002
NOTIFICATION:         http://www.apache.org/licenses/exports/
```

<h3 id="inform">Inform users by including a crypto notice in the distribution's README file<a class="headerlink" href="#inform" title="Permanent link">&para;</a></h3>

Should the software qualify for the Section 742.15(b) exemption, place the following notice into each distribution's README file:

```
   This distribution includes cryptographic software.  The country in 
   which you currently reside may have restrictions on the import, 
   possession, use, and/or re-export to another country, of 
   encryption software. BEFORE using any encryption software, please 
   check your country's laws, regulations and policies concerning the
   import, possession, or use, and re-export of encryption software, to 
   see if this is permitted. See http://www.wassenaar.org for
   more information.
The Apache Software Foundation has classified this software as Export Commodity 
   Control Number (ECCN) 5D002, which includes information security
   software using or performing cryptographic functions with asymmetric
   algorithms. The form and manner of this Apache Software Foundation
   distribution makes it eligible for export under the "publicly available"
   Section 742.15(b) exemption (see the BIS Export Administration Regulations, 
   Section 742.15(b)) for both object code and source code.
The following provides more details on the included cryptographic
   software:
```

Be sure to add some information at the bottom of the notice about the components of the release including cryptography.

<h2 id="faq">Frequently Asked Questions<a class="headerlink" href="#faq" title="Permanent link">&para;</a></h2>

<h4 id="faq-productname">What is the "PRODUCT NAME/MODEL #" for my product?<a class="headerlink" href="#faq-productname" title="Permanent link">&para;</a></h4>

The product name is the name of the ASF product (e.g. "Apache Foo"), even if the notification is being made about another manufacturer's cryptography included in the ASF product. Do not list the ASF product's version number.

<h4 id="faq-manufacturer">What is the MANUFACTURER?<a class="headerlink" href="#faq-manufacturer" title="Permanent link">&para;</a></h4>The manufacture is the name of the individual/organization that built the crypto item included in the ASF product, whether that is the ASF itself or some other open source project or organization.

<h4 id="faq-notification">What is the NOTIFICATION?<a class="headerlink" href="#faq-notification" title="Permanent link">&para;</a></h4>

the notification is a URL that directly or indirectly points to the source code for the crypto item built by the listed <a href="#faq-manufacturer">manufacturer</a> that is
distributed within the ASF <a href="#faq-productname">product</a>. At the ASF, we indirectly point to the source code by having all products list `www.apache.org/licenses/exports/` as the NOTIFICATION url, and ensuring that this page is refreshed with the set of links to the crypto source code for the notifying product. If the product contains more than one crypto item, the exports page simply points to the source for each crypto item included in the product.

<h4 id="faq-firstnotification">When is the first time a notification email must be sent?<a class="headerlink" href="#faq-firstnotification" title="Permanent link">&para;</a></h4>

You must send the notification email prior to exporting/posting online. **Note**: this even includes distribution of code through publicly accessible servers/repositories before there has been any official release.

<h4 id="faq-public">What are examples of when a crypto item is publicly accessible through ASF servers?<a class="headerlink" href="#faq-public" title="Permanent link">&para;</a></h4>

The **obvious example** is including something like an OpenSSL binary within a product distribution from a /dist URL. The **less-obvious example** is the point at which a software repository starts to include code that is specially designed to work with any other 5D002 item, whether that item is ever to be included within a product distribution or not. In other words, a project should send out a notification email just after making the decision to include code that is specially designed to work with crypto APIs but
before actually committing such code. No need to worry about surprise Jira attachments with such code -- only the event of committing the code to the ASF product repository.

<h4 id="faq-publicemails">Are public contributions of crypto items to the mailing list, Jira or Bugzilla databases considered exports?<a class="headerlink" href="#faq-publicemails" title="Permanent link">&para;</a></h4>

No. We do not need to worry about surprise Jira attachments with such code -- only code committed to the ASF product repository. The actual poster of these attachments would be the one 'exporting' the crypto, since it would not be an act of the ASF project as it addressed <a href="#faq-public">above</a>.

<h4 id="faq-previouslyexported">If we distribute previously exported crypto items, must we still qualify the same item for export?<a class="headerlink" href="#faq-previouslyexported" title="Permanent link">&para;</a></h4>

Yes. The ASF is responsible for complying with the EAR, regardless of whether the item we are exporting has been previously exported under the Section 742.15(b) publicly available exemption or any license exception by another manufacturer/company/open source project.

<h4 id="faq-manyproducts">If the ASF distributes a particular crypto item within one product under the Section 742.15(b) publicly available exemption, must the same item requalify when distributed in a different ASF product?<a class="headerlink" href="#faq-manyproducts" title="Permanent link">&para;</a></h4>

Yes. Each product must qualify separately, which includes sending notifications for each.

<h4 id="faq-versions">If the ASF distributes/exports a crypto item after qualifying it under the Section 742.15(b) publicly available exemption, must the same product requalify for release of future versions?<a class="headerlink" href="#faq-versions" title="Permanent link">&para;</a></h4>

No. As long as the email's notification URL for the source location still (directly or indirectly) points to the applicable source for each version's crypto item, no additional process is required.

<h4 id="faq-notificationurl">Where must the email's notification URL point to?<a class="headerlink" href="#faq-notificationurl" title="Permanent link">&para;</a></h4>

The notification URL for all products should point to `https://www.apache.org/licenses/exports/`, which should be refreshed to include the project's cryptography data
before the email is sent.

<h4 id="faq-additionalemails">If the notification URL never changes, when are additional notification emails required?<a class="headerlink" href="#faq-additionalemails" title="Permanent link">&para;</a></h4>

Each product needs to send only one notification email until information previously submitted is no longer accurate, e.g. a change in the manufacturer.

<h4 id="faq-infousers">Is there any BIS requirement to tell users and/or redistributors of our products about the crypto within our products?<a class="headerlink" href="#faq-infousers" title="Permanent link">&para;</a></h4>

No, but it's a good idea to do so. See our self-imposed requirement to <a href="#inform">inform users</a>.

<h4 id="faq-twocryptos">When exporting a product that is not only designed to use some third-party crypto item, but also includes the third-party crypto item, does this require two notifications or one notification with two manufacturers?<a class="headerlink" href="#faq-twocryptos" title="Permanent link">&para;</a></h4>

When multiple crypto items exist within a single product, one email should be sent listing all manufacturers of encryption items in the product and the <a href="/licenses/exports/">standard notification URL</a> to the ASF-wide exports page with detailed information, including the location of the corresponding source code.

<h4 id="faq-nonasfsource">Can the ultimate link to the crypto item's source code point to a non-ASF web page?<a class="headerlink" href="#faq-nonasfsource" title="Permanent link">&para;</a></h4>

Yes, as long as the PMC is reasonably confident that the non-ASF location is likely to remain available for BIS inspection for the foreseeable future. If this is not the case at some point, the ASF should update the link to a location that will remain available.

<h4 id="faq-compilerswitch">What if the object/binary code being distributed was built with a particular compiler switch?<a class="headerlink" href="#faq-compilerswitch" title="Permanent link">&para;</a></h4>

It is fine to use whatever compiler switches you like. There is no need to provide compiler switch information, as long as the pointed source code is a superset of all the controlled source that ends up being distributed within the object/binary file.

<h4 id="faq-binaryurl">Do we need to notify the BIS of the location of object/binary files?<a class="headerlink" href="#faq-binaryurl" title="Permanent link">&para;</a></h4>

No, but whether we are distributing source or object/binary files, we must always make sure a notification has been made pointing (directly or indirectly) to the associated source.

<h4 id="faq-includedlibssl">If my project ships a binary that includes libssl/libcrypto, what notifications must be made?<a class="headerlink" href="#faq-includedlibssl" title="Permanent link">&para;</a></h4>

Within the single notification email (**sent prior to either hosting libssl/libcrypto or committing code that binds to it**), the ASF and the OpenSSL project should be listed as manufacturers, since both organizations produce encryption items included in the product. See the more generic <a href="#faq-twocryptos">Q&amp;A on this topic.</a>

<h4 id="faq-linkedtolibssl">If my project ships a binary that provides bindings to OpenSSL, but does not include its source or binaries, what notifications must be made?<a class="headerlink" href="#faq-linkedtolibssl" title="Permanent link">&para;</a></h4>

The only required notification for an Apache project that is specially designed to use, but doesn't include, such crypto, is the notification for the ASF product code.

<h4 id="faq-nonamerican">Why should I, who am not a U.S. citizen nor resident, be constrained by some U.S. law?<a class="headerlink" href="#faq-nonamerican" title="Permanent link">&para;</a></h4>

The ASF is a U.S.-based corporation and must comply with U.S. export controls. Incidentally, the U.S. is not the only country with controls on cryptography. Many other nations have similar restrictions, primarily driven by the <a href="https://www.wassenaar.org" target="_blank"> Wassenaar Arrangement</a>.

<h4 id="faq-digest">Do digest algorithms such as MD5 and SHA1 require notification?<a class="headerlink" href="#faq-digest" title="Permanent link">&para;</a></h4>
No. One-way algorithms such as MD5 or SHA1, or more sophisticated implementations, do not require notification. Only encryption algorithms do.
