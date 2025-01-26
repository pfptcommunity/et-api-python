from typing import Dict, Optional

from requests import Response

from et_api.web.dictionary import Dictionary

class CVSSDataV3(Dict):
    @property
    def scope(self) -> Optional[str]:
        return self.get("scope")

    @property
    def version(self) -> Optional[str]:
        return self.get("version")

    @property
    def base_score(self) -> Optional[float]:
        return self.get("baseScore")

    @property
    def attack_vector(self) -> Optional[str]:
        return self.get("attackVector")

    @property
    def base_severity(self) -> Optional[str]:
        return self.get("baseSeverity")

    @property
    def vector_string(self) -> Optional[str]:
        return self.get("vectorString")

    @property
    def integrity_impact(self) -> Optional[str]:
        return self.get("integrityImpact")

    @property
    def user_interaction(self) -> Optional[str]:
        return self.get("userInteraction")

    @property
    def attack_complexity(self) -> Optional[str]:
        return self.get("attackComplexity")

    @property
    def availability_impact(self) -> Optional[str]:
        return self.get("availabilityImpact")

    @property
    def privileges_required(self) -> Optional[str]:
        return self.get("privilegesRequired")

    @property
    def confidentiality_impact(self) -> Optional[str]:
        return self.get("confidentialityImpact")


class CVSSDataV2(Dict):
    @property
    def version(self) -> Optional[str]:
        return self.get("version")

    @property
    def base_score(self) -> Optional[float]:
        return self.get("baseScore")

    @property
    def access_vector(self) -> Optional[str]:
        return self.get("accessVector")

    @property
    def vector_string(self) -> Optional[str]:
        return self.get("vectorString")

    @property
    def authentication(self) -> Optional[str]:
        return self.get("authentication")

    @property
    def integrity_impact(self) -> Optional[str]:
        return self.get("integrityImpact")

    @property
    def access_complexity(self) -> Optional[str]:
        return self.get("accessComplexity")

    @property
    def availability_impact(self) -> Optional[str]:
        return self.get("availabilityImpact")

    @property
    def confidentiality_impact(self) -> Optional[str]:
        return self.get("confidentialityImpact")


class BaseMetricV3(Dict):
    @property
    def type(self) -> Optional[str]:
        return self.get("type")

    @property
    def source(self) -> Optional[str]:
        return self.get("source")

    @property
    def cvss_data(self) -> Optional[CVSSDataV3]:
        cvss = self.get("cvssData")
        return CVSSDataV3(cvss) if cvss else None

    @property
    def impact_score(self) -> float:
        return self.get("impactScore", 0.0)

    @property
    def exploitability_score(self) -> float:
        return self.get("exploitabilityScore", 0.0)


class BaseMetricV2(Dict):
    @property
    def type(self) -> Optional[str]:
        return self.get("type")

    @property
    def source(self) -> Optional[str]:
        return self.get("source")

    @property
    def cvss_data(self) -> Optional[CVSSDataV2]:
        cvss = self.get("cvssData")
        return CVSSDataV2(cvss) if cvss else None

    @property
    def impact_score(self) -> float:
        return self.get("impactScore", 0.0)

    @property
    def exploitability_score(self) -> float:
        return self.get("exploitabilityScore", 0.0)

    @property
    def ac_insuf_info(self) -> bool:
        return self.get("acInsufInfo", False)

    @property
    def base_severity(self) -> Optional[str]:
        return self.get("baseSeverity")

    @property
    def obtain_all_privilege(self) -> bool:
        return self.get("obtainAllPrivilege", False)

    @property
    def obtain_user_privilege(self) -> bool:
        return self.get("obtainUserPrivilege", False)

    @property
    def obtain_other_privilege(self) -> bool:
        return self.get("obtainOtherPrivilege", False)

    @property
    def user_interaction_required(self) -> bool:
        return self.get("userInteractionRequired", False)


class Weakness(Dict):
    @property
    def type(self) -> Optional[str]:
        return self.get("type")

    @property
    def source(self) -> Optional[str]:
        return self.get("source")

    @property
    def description(self) -> Optional[list]:
        return self.get("description")


class CVEInfo(Dictionary):
    def __init__(self, response: Response):
        super().__init__(response)

    @property
    def cve(self) -> str:
        return self.get("cve", "")

    @property
    def description(self) -> str:
        return self.get("description", "")

    @property
    def config_operator(self) -> str:
        return self.get("config_operator", "")

    @property
    def source_identifier(self) -> str:
        return self.get("source_identifier", "")

    @property
    def vuln_status(self) -> str:
        return self.get("vuln_status", "")

    @property
    def cisa_exploit_add(self) -> Optional[str]:
        return self.get("cisa_exploit_add")

    @property
    def cisa_vulnerability_name(self) -> Optional[str]:
        return self.get("cisa_vulnerability_name")

    @property
    def known_exploited_vulnerabilities(self) -> bool:
        return self.get("known_exploited_vulnerabilities", False)

    @property
    def pfpt_recent_observed(self) -> bool:
        return self.get("pfpt_recent_observed", False)

    @property
    def pfpt_ever_observed(self) -> bool:
        return self.get("pfpt_ever_observed", False)

    @property
    def pfpt_first_observed(self) -> Optional[str]:
        return self.get("pfpt_first_observed")

    @property
    def pfpt_last_observed(self) -> Optional[str]:
        return self.get("pfpt_last_observed")

    @property
    def seven_day_trend(self) -> Optional[str]:
        return self.get("seven_day_trend")

    @property
    def basemetricv3(self) -> Optional[BaseMetricV3]:
        basemetric = self.get("basemetricv3")
        return BaseMetricV3(basemetric) if basemetric else None

    @property
    def basemetricv2(self) -> Optional[BaseMetricV2]:
        basemetric = self.get("basemetricv2")
        return BaseMetricV2(basemetric) if basemetric else None

    @property
    def weaknesses(self) -> Optional[list]:
        weaknesses = self.get("weaknesses")
        return [Weakness(w) for w in weaknesses] if weaknesses else None

    @property
    def publisheddate(self) -> Optional[str]:
        return self.get("publisheddate")

    @property
    def lastmodifieddate(self) -> Optional[str]:
        return self.get("lastmodifieddate")
