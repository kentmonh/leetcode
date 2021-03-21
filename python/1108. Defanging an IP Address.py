"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        split_address = address.split(".")
        result = ""
        for nummber in split_address:
            result += nummber + "[.]"
        return result.removesuffix("[.]")

# solution 2
class Solution2:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))