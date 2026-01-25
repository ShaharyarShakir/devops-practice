# DNS && its types

#### DNS stands for Domain Name System.

- Think of it as the phonebook of the internet.

- When you type a website name like google.com into your browser...

- Your computer doesn't understand names — it understands IP addresses like 142.250.190.14.

- So DNS translates the name to the IP address — just like how a phonebook gives you the number when you know the name.

## Types of DNS Servers

#### 1. Recursive Resolver (The Middleman)

- First one your computer talks to.

- Goes and finds the answer for you, if it doesn’t already know.

- Like asking a friend: "Hey, what’s Google’s number?"

#### 2. Root DNS Server (The Boss of the Internet)

- Knows where to find the main directories for all websites.

- Doesn't know the final answer but points you in the right direction.

- Like saying: “I don’t know, but try asking the .com directory.”

#### 3. TLD Server (Top-Level Domain Server)

- Knows about all domains that end in things like .com, .org, .net, etc.

- Helps narrow down the search.

- Like saying: “For google.com, talk to the .com team.”

#### 4. Authoritative DNS Server (The Final Answer)

- Knows the actual IP address of the website.

- This is where the correct answer comes from.

- Like saying: “Here’s the exact number for Google.”

##### In Short:

- Typing google.com → Your computer → Recursive DNS → Root DNS → TLD DNS → Authoritative DNS → IP Address Found

## Common DNS Record Types

DNS records are like instructions or notes that tell the internet what to do with a domain name.

Here are the most common ones:

📌 A Record (Address)
What it does: Points a domain to an IPv4 address (e.g., 192.0.2.1)

Think of it as: “Send visitors to this exact street address.”

Example:

Copy
Edit
example.com → 192.0.2.1
📌 AAAA Record (IPv6 Address)
What it does: Points a domain to an IPv6 address (e.g., 2001:0db8::1)

Think of it as: Like an A record, but for newer, longer IP addresses.

Example:

cpp
Copy
Edit
example.com → 2001:0db8::1
🔗 CNAME Record (Canonical Name)
What it does: Points a domain to another domain name, not an IP.

Think of it as: A nickname or shortcut.

Example:

Copy
Edit
www.example.com → example.com
📬 MX Record (Mail Exchange)
What it does: Directs email for the domain to the correct mail server.

Think of it as: “Send all emails to this mail handler.”

Example:

less
Copy
Edit
example.com → mail.example.com (Priority: 10)
🧭 NS Record (Name Server)
What it does: Tells the internet which DNS servers are in charge of your domain.

Think of it as: “Ask these servers for any info about this domain.”

Example:

Copy
Edit
example.com → ns1.nameserver.com
📝 TXT Record (Text)
What it does: Stores text info for the domain.

Used for: SPF (email validation), domain verification, etc.

Think of it as: “Here’s some extra info about my domain.”

Example:

arduino
Copy
Edit
"v=spf1 include:\_spf.google.com ~all"
🕓 TTL (Time to Live)
Not a record type, but part of every record.

Tells DNS how long to cache the record.

Think of it as: “Remember this info for X seconds before checking again.”

### Others (Less Common but Useful)

| Record| Use|
|------ |--|
|**SRV**|Used for services like VoIP; tells where a service is located|
|**PTR**|Reverse DNS lookup (IP → domain name)|
|**SOA**|Info about the domain’s DNS zone (admin email, update time, etc.)|

