import procmon_parser

from procmon_parser import load_configuration, dump_configuration, Rule

with open("C:\\Users\\test_sym\\Desktop\\initiative\\1.pmc", "rb")as f:
  config = load_configuration(f)
new_rules = [ Rule('User', 'is_not', '##username', 'include'), Rule('Process_name', 'contains', '##processname', 'include'), Rule('Operation', 'is', 'WriteFile', 'include')]
config["FilterRules"] = new_rules + config["FilterRules"]

with open("C:\\Users\\test_sym\\Desktop\\initiative\\2.pmc", "wb")as f:
  dump_configuration(config, f)
