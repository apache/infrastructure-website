
layout: post
Title: new hardware for apache.org
date: '2010-07-19T04:01:07+00:00'
permalink: new_hardware_for_apache_org

<p>This weekend we rolled out a new server, a Dell Power Edge R410, named Eos, to host the Apache.org websites and MoinMoin wiki:</p>
<ul>
<li>OS: FreeBSD 8.1-RC2</li>
<li>CPU: 2x Intel(R) Xeon(R) CPU X5550  @ 2.67GHz (2 package(s) x 4 core(s) x 2 SMT threads = 16 CPUs)</li>
<li>RAM: 48gb DDR3</li>
<li>Storage: 12x 15k RPM 300gb SAS, 2x 80gb SSD, configured in a ZFS raidz2 with the SSDs used for the L2ARC</li>
</ul>
<p>This new hardware replaces an older Sun T2000, also called eos, as the primary webserver for apache.org.  We hope everyone enjoys the increased performance, especially from the Wiki!</p>

<p>On the less visible infrastructure side, we are also upgrading Athena, one of our frontend mail servers.  The new Athena is a DPE r210 with a 4 core 2.67GHz processor, replacing a Sun X2200.</p>
