import re


class CssParser:

    def parse_string(self, css_string):
        rulesets = []

        while len(css_string):
            raw_ruleset, css_string = self.extract_raw_ruleset(css_string)
            if raw_ruleset:
                ruleset = self.parse_ruleset(raw_ruleset)
                rulesets.append(ruleset)

        return rulesets

    @staticmethod
    def extract_raw_ruleset(css_string):

        ruleset = None

        ruleset_regex = "^[ \n\r]*?(.+?\{.+?\})"

        result = re.match(ruleset_regex, css_string, re.RegexFlag.DOTALL)

        if result:
            css_string = css_string[len(result.group(0)):]
            ruleset = result.group(1)
        else:
            css_string = ""

        return ruleset, css_string

    def parse_ruleset(self, raw_ruleset):

        ruleset = CssRuleset()

        regex = "[ \r\n]*(.+?) *\{(.+?)\}"

        result = re.match(regex, raw_ruleset, re.RegexFlag.DOTALL)

        if result:
            ruleset.set_selector(result.group(1))
            rules = self.parse_rules(result.group(2))
            for rule in rules:
                ruleset.add_rule(rule)
            return ruleset
        else:
            return None

    def parse_rules(self, rules_string):

        rules = []

        while len(rules_string):
            raw_rule, rules_string = self.extract_raw_rule(rules_string)
            if raw_rule:
                rule = self.parse_rule(raw_rule)
                rules.append(rule)

        return rules

    @staticmethod
    def extract_raw_rule(rules_string):

        rule = None

        regex = "[ \r\n]*(.+?;)[ \r\n]*"

        result = re.match(regex, rules_string, re.RegexFlag.DOTALL)
        if result:
            rules_string = rules_string[len(result.group(0)):]
            rule = result.group(1)
        else:
            rules_string = ""

        return rule, rules_string

    @staticmethod
    def parse_rule(raw_rule):

        rule = CssRule()

        regex = "[ \r\n]*(.+?): *(.+) *;"

        result = re.match(regex, raw_rule, re.RegexFlag.DOTALL)

        if result:
            rule.set_property(result.group(1))
            rule.set_value(result.group(2))
            return rule
        else:
            return None


class CssRuleset:

    def __init__(self):
        self.selector = None
        self.rules = []

    def __str__(self):
        return f"{self.selector} | {len(self.rules)} rules"

    def set_selector(self, selector_string):
        self.selector = selector_string

    def add_rule(self, css_rule):
        self.rules.append(css_rule)


class CssRule:

    def __init__(self):
        self.property = None
        self.value = None

    def __str__(self):
        return f"{self.property}: {self.value}"

    def set_property(self, property_string):
        self.property = property_string

    def set_value(self, value):
        self.value = value
