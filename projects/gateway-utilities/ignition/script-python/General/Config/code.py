logger = system.util.getLogger("General.Config")

try:
	if not hasattr(General, "Files"):
		raise NameError("General.Files not found")
	if not hasattr(General, "Utilities"):
		raise NameError("General.Utilities not found")
except NameError as e:
	logger.warn("Some Features of this script module require other modules, please ensure that each required module is properly loaded or some functionality might not work: %s" % e.message)

CONFIG_SOURCE_DIRECTORY = "data/configs/"


class ConfigException(Exception):
    pass

def getConfigValue(config_name, config_key=None, force_refresh=False):
	"""
	DESCRIPTION: Get the value of a specific key in a config file
	PARAMETERS: config_name (REQ, str) - the name of the config file to be retrieved, unincluding extension.
				config_key (REQ, str) - the key to retrieve from the config file (if omitted, the entire thresholds file is returned)
				force_refresh (OPT, bool) - force a refresh of the config file
	"""
	
	file_path = '%s/%s.json' % (CONFIG_SOURCE_DIRECTORY, config_name)
	
	config = General.Files.getGatewayFileContents(file_path, force_refresh=force_refresh)
	
	if config_key is None:
		return config
	
	return General.Utilities.read_json_path(config, config_key)
