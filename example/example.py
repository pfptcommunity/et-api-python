from distutils.command.clean import clean

from et_api.common import *
from et_api.v1 import *

if __name__ == '__main__':
    api_key_file = open("et.api_key", "r")
    api_key = api_key_file.read()
    client = Client(api_key)

    # print(client.malware._uri)
    # print(client.malware["Balada"]._uri)
    # data = client.malware["Balada"]()
    # print(data.name, "-->", data.description)

    print(client.cve._uri)
    print(client.cve["CVE-2022-30525"]._uri)
    cve_info = client.cve["CVE-2022-30525"]()

    print(f"CVE: {cve_info.cve}")
    print(f"Description: {cve_info.description}")
    print(f"Config Operator: {cve_info.config_operator}")
    print(f"Source Identifier: {cve_info.source_identifier}")
    print(f"Vulnerability Status: {cve_info.vuln_status}")
    print(f"CISA Exploit Add Date: {cve_info.cisa_exploit_add}")
    print(f"CISA Vulnerability Name: {cve_info.cisa_vulnerability_name}")
    print(f"Known Exploited Vulnerabilities: {cve_info.known_exploited_vulnerabilities}")
    print(f"PFPT Recent Observed: {cve_info.pfpt_recent_observed}")
    print(f"PFPT Ever Observed: {cve_info.pfpt_ever_observed}")
    print(f"PFPT First Observed: {cve_info.pfpt_first_observed}")
    print(f"PFPT Last Observed: {cve_info.pfpt_last_observed}")
    print(f"Seven Day Trend: {cve_info.seven_day_trend}")
    print(f"Publish Date: {cve_info.publisheddate}")
    print(f"Last Modified Date: {cve_info.lastmodifieddate}")

    print("BaseMetricV3:")
    print(f"  Type: {cve_info.basemetricv3.type if cve_info.basemetricv3 else None}")
    print(f"  Source: {cve_info.basemetricv3.source if cve_info.basemetricv3 else None}")
    print(f"  CVSS Data:")
    if cve_info.basemetricv3 and cve_info.basemetricv3.cvss_data:
        print(f"    Scope: {cve_info.basemetricv3.cvss_data.scope}")
        print(f"    Version: {cve_info.basemetricv3.cvss_data.version}")
        print(f"    Base Score: {cve_info.basemetricv3.cvss_data.base_score}")
        print(f"    Attack Vector: {cve_info.basemetricv3.cvss_data.attack_vector}")
        print(f"    Base Severity: {cve_info.basemetricv3.cvss_data.base_severity}")

    print("BaseMetricV2:")
    print(f"  Type: {cve_info.basemetricv2.type if cve_info.basemetricv2 else None}")
    print(f"  Source: {cve_info.basemetricv2.source if cve_info.basemetricv2 else None}")
    print(f"  CVSS Data:")
    if cve_info.basemetricv2 and cve_info.basemetricv2.cvss_data:
        print(f"    Version: {cve_info.basemetricv2.cvss_data.version}")
        print(f"    Base Score: {cve_info.basemetricv2.cvss_data.base_score}")
        print(f"    Access Vector: {cve_info.basemetricv2.cvss_data.access_vector}")
    print(f"  Impact Score: {cve_info.basemetricv2.impact_score}")
    print(f"  Exploitability Score: {cve_info.basemetricv2.exploitability_score}")
    print(f"  AC Insufficient Info: {cve_info.basemetricv2.ac_insuf_info}")
    print(f"  Base Severity: {cve_info.basemetricv2.base_severity}")
    print(f"  Obtain All Privilege: {cve_info.basemetricv2.obtain_all_privilege}")
    print(f"  Obtain User Privilege: {cve_info.basemetricv2.obtain_user_privilege}")
    print(f"  Obtain Other Privilege: {cve_info.basemetricv2.obtain_other_privilege}")
    print(f"  User Interaction Required: {cve_info.basemetricv2.user_interaction_required}")

    print("Weaknesses:")
    if cve_info.weaknesses:
        for weakness in cve_info.weaknesses:
            print(f"  Type: {weakness.type}")
            print(f"  Source: {weakness.source}")
            if weakness.description:
                for desc in weakness.description:
                    print(f"    Lang: {desc.get('lang', '')}, Value: {desc.get('value', '')}")

    exit(0)
    # Get all the reputation categories
    for category in client.reputation_categories():
        print(category.name, "-->", category.description)

    # Get Domain information
    for reputation in client.domains["yahoo"].reputation():
        print(reputation)

    for url in client.domains["yahoo"].urls():
        print("URL: ", url)

    for sample in client.domains["yahoo"].samples():
        print("Sample: ", sample)

    for ips in client.domains["yahoo"].ips():
        print("IPs: ", ips)

    data = client.domains["yahoo"].events()
    for event in data:
        print("Event: ", event)

    for ns in client.domains["yahoo"].nameservers():
        print("Nameserver: ", ns)

    for key, value in client.domains["yahoo"].whois().items():
        print("{} = {}".format(key, value))

    # Get IP Information
    ip = "98.137.11.164"

    for reputation in client.ips[ip].reputation():
        print("Reputation: ", reputation)

    for url in client.ips[ip].urls():
        print("URL: ", url)

    for sample in client.ips[ip].samples():
        print("Sample: ", sample)

    for domain in client.ips[ip].domains():
        print("Domain: ", domain)

    for event in client.ips[ip].events():
        print("Event: ", event)

    for geo in client.ips[ip].geo_location():
        print("Geo: ", geo)

    # Get Malware Samples
    md5 = "cd88c95ca03b86d9ca32f322d69a7ee9"

    details = client.samples[md5]()
    print("details:", details)

    for connection in client.samples[md5].connections():
        print("Connection:", connection)

    for event in client.samples[md5].ids_events():
        print("Event:", event)

    for dns in client.samples[md5].dns():
        print("DNS:", dns)

    for http in client.samples[md5].http():
        print("HTTP:", http)

    sid = "2012199"

    info = client.sids[sid]()
    print("SigInfo:", info.sid, '-->', info.name)

    f = IPFilter()
    f.sort_by = SortBy.LAST_SEEN
    f.sort_direction = SortOrder.ASCENDING

    for ip in client.sids[sid].ips(f):
        print("IP:", ip)

    for domain in client.sids[sid].domains():
        print("Domain:", domain)

    for sample in client.sids[sid].samples():
        print("Sample:", sample)

    sig = client.sids[sid].signature()
    # Normal dictionary
    for key, value in sig.items():
        print("{} = {}".format(key, value))
    # Helpers
    print("Sid:", sig.sid)
    print("Suricata:", sig.suricata)
    print("Snort:", sig.snort)

    doc = client.sids[sid].documentation()
    # Normal dictionary
    for key, value in doc.items():
        print("{} = {}".format(key, value))
    # Helpers
    print("Sid:", doc.sid)
    print("Summary:", doc.summary)
    print("Description:", doc.description)
    print("Impact:", doc.impact)

    for ref in client.sids[sid].references():
        print("Type:", ref.type)
        print("Description:", ref.description)
        print("Urls:", ref.urls)
