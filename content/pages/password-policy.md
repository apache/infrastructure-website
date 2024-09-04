Title: Committer password policy
license: https://www.apache.org/licenses/LICENSE-2.0

This page outlines the policy on committer passwords for LDAP accounts, and explains a bit 
about the logic behind it.

### Minimum password length: eight characters
All passwords must have eight or more characters. You can use any combination of letters, numbers, special characters, and spaces, and there is no upper limit to the password length.

### Minimum password entropy size: 54 bits
Entropy size is a measure of how many attempts if would potentially take to crack the password, whether 
through brute-forcing, dictionary attacks or simply guessing. It is measured in bits that 
correspond to the size of the maximum number of attempts required in binary format. Thus, 
a password with an entropy size of 24 bits would require up to `2^24` == 16,777,216 attempts 
to crack. Entropy size is calculated as the length of the password (in characters/bytes), 
multiplied by the binary logarithmic (log2) of the alphabetical cardinality of the password, 
meaning the number of unique characters in the password. 

In the example password `I am Groot`, there are 10 characters in the string, and 8 unique 
characters in total (`I,a,m,G,r,o,t, and a whitespace), thus the entropy size is:

![entropy=10*\log{2}(8) => entropy=10 * 3 => entropy=30](../images/pwdpolicy-1.svg)

At the ASF, we require a minimum entropy size of **54 bits**, meaning it should require more than 
approximately 18 quadrillion attempts to brute-force a password.

### Minimum password complexity: 0.60
We also require a complexity degree of 0.60. Password complexity ranges from 0 to 1, where 0 is 
a password consisting of only the same letters over and over, and 1 means a password is 
long enough and with enough entropy to require quadrillions of computations to crack, and also 
has enough sequential variety to negate any speed improvements a malicious actor might employ in 
order to simplify or otherwise optimize an attempt at cracking a password.

The exact formula we use is as follows:

![complexity=1-\frac{2}{3}(2^{(-\frac{-\log_{2}(\frac{1-0.950}{1-\frac{1}{3}})}{90}*(entropy-30)})](../images/pwdpolicy-2.svg)

Our <a href="https://id.apache.org" target="_blank">self-serve page for (re)setting passwords</a> can provide you with 
an instant assessment of your password strength using these requirements, to help you find a 
password that is sufficiently strong.
