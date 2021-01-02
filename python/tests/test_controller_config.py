from scc.config import Config
import pytest, os, sys, shutil, platform

suffix = 99 # os.getpid()


class TestControllerConfig(object):

	@classmethod
	def __init__(self):
		if platform.system() == "Windows":
			import winreg
			reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
			software_key = winreg.OpenKey(reg, "Software")
			scc_key = winreg.CreateKey(software_key, "SCController-c-test-%s" % suffix)
			devs_key = winreg.CreateKey(scc_key, "devices")
			winreg.CloseKey(winreg.CreateKey(devs_key, "test_empty"))
			winreg.CloseKey(winreg.CreateKey(devs_key, "test_changeme"))

			test_key = winreg.CreateKey(devs_key, "test")
			axes_key = winreg.CreateKey(test_key, "axes")
			buttons_key = winreg.CreateKey(test_key, "buttons")
			dpads_key = winreg.CreateKey(test_key, "dpads")
			gui_key = winreg.CreateKey(test_key, "gui")
			axis_key = winreg.CreateKey(axes_key, "1")
			winreg.SetValueEx(axis_key, "axis", None, winreg.REG_SZ, "stick_y")

			winreg.SetValueEx(buttons_key, "305", None, winreg.REG_SZ, "B")
			winreg.SetValueEx(buttons_key, "307", None, winreg.REG_SZ, "X")
			winreg.SetValueEx(buttons_key, "308", None, winreg.REG_SZ, "Y")

			winreg.SetValueEx(gui_key, "icon", None, winreg.REG_SZ, "test-01")
			winreg.SetValueEx(gui_key, "background", None, winreg.REG_SZ, "psx")
			winreg.SetValueEx(gui_key, "buttons", None, winreg.REG_MULTI_SZ,
					["A","B","X","Y","BACK","C","START","LB","RB","LT","RT","LG","RG"])

			for x in (axis_key, buttons_key, dpads_key, gui_key, axes_key,
							test_key, devs_key, scc_key, software_key, reg):
				winreg.CloseKey(x)

			# ^^ see? and this is why Config class exists
			filename = "Software\\SCController-c-test-%s" % suffix
			self.c = Config(filename)
		else:
			self.prefix = "/tmp/test_config_%i" % suffix
			try:
				os.makedirs("%s/devices" % self.prefix)
			except OSError:
				pass
			open("%s/devices/test_empty.json" % self.prefix, "w").write("{}")
			open("%s/devices/test_changeme.json" % self.prefix, "w").write("{}")
			open("%s/devices/test.json" % self.prefix, "w").write("""{
				"axes": { "1": { "axis": "stick_y" }},
				"buttons": { "305": "B", "307": "X", "308": "Y" },
				"dpads": {},

				"gui": {
					"icon": "test-01",
					"background": "psx",
					"buttons": ["A","B","X","Y","BACK","C","START","LB","RB","LT","RT","LG","RG"]
				}
			}""")
			filename = "%s.json" % (self.prefix)
			self.c = Config(filename)
			#self.c.set_prefix(self.prefix)

	@classmethod
	def teardown_class(cls):
		pass
		#if platform.system() != "Windows":
		#	shutil.rmtree(self.prefix)

	def x_test_get_controllers(self):
		assert "test" in self.c.get_controllers()

	def test_defaults(self):
		""" Tests if defaults are provided to both daemon and gui-specific values """
		ccfg = self.c.get_controller_config("test_empty")
		assert len(list(ccfg["axes"])) == 0
		assert len(list(ccfg["buttons"])) == 0
		assert len(list(ccfg["dpads"])) == 0

		assert type(ccfg["input_rotation"]["right"]) is float
		assert type(ccfg["input_rotation/left"]) is float
		assert type(ccfg["idle_timeout"]) in (int, int)

		assert ccfg["gui"]["icon"] == ""
		assert ccfg["gui/icon"] == ""
		assert type(ccfg["gui/name"]) in (str, str)
		assert len(ccfg["gui"]["buttons"]) == 0

	def test_same_object(self):
		""" Tests that repeated requests to some types of key return same object """
		ccfg = self.c.get_controller_config("test")
		a = ccfg["gui"]
		assert ccfg["gui"] is ccfg["gui"]
		assert ccfg["gui"] is a

		b = a["buttons"]
		assert ccfg["gui"]["buttons"] is b
		a["buttons"] = ["A", "B"]
		assert ccfg["gui"]["buttons"] is not b

	def test_gui_related(self):
		""" Tests loading values typicaly used by GUI """
		gcfg = self.c.get_controller_config("test")["gui"]
		assert gcfg["background"] == "psx"
		assert gcfg["buttons"][1] == "B"
		assert gcfg["icon"] == "test-01"

	def test_get_invalid(self):
		""" Tests whether opening non-existing config fails """
		with pytest.raises(OSError):
			ccfg = self.c.get_controller_config("notexisting")

	def test_write_errors(self):
		""" Tests error that may arrise when writing stuff """
		ccfg = self.c.get_controller_config("test_changeme")
		# Setting non-string to strarray
		with pytest.raises(TypeError):
			ccfg["gui"]["buttons"] = ["X", "Y", 1, "A"]
		with pytest.raises(TypeError):
			ccfg["gui"]["buttons"] = ["X", True, "B", "A"]

	def test_write(self):
		""" Tests changing config values """
		ccfg = self.c.get_controller_config("test_changeme")
		ccfg["gui/icon"] = "icon1"
		ccfg["gui"]["buttons"] = ["X", "Y", "A", "B"]
		ccfg["gui"]["buttons"][1] = "C"
		ccfg["gui"]["buttons"].append("Z")
		ccfg.save()
		ccfg = self.c.get_controller_config("test_changeme")
		assert ccfg["gui"]["icon"] == "icon1"
		assert ccfg["gui"]["buttons"][1] == "C"
		assert ccfg["gui"]["buttons"][2] == "A"

	def test_create_config(self):
		with pytest.raises(OSError):
			self.c.get_controller_config("test_notexisting_create")
		ccfg = self.c.create_controller_config("test_notexisting_create")
		ccfg["gui/icon"] = "Changed"
		ccfg.save()
		del ccfg

		ccfg = self.c.get_controller_config("test_notexisting_create")
		assert ccfg["gui"]["icon"] == "Changed"

	def test_load_invalid(self):
		""" Tests loading file that's not json """
		if platform.system() == "Windows":
			return
		open("%s/devices/test_notjson.json" % self.prefix, "w").write("X")
		with pytest.raises(OSError):
			ccfg = self.c.get_controller_config("test_notjson")
			print(ccfg)

	def test_create_values(self):
		""" Tests creating new values """
		ccfg = self.c.create_controller_config("test_create")
		ccfg["buttons"][10] = "C"
		ccfg["buttons"][15] = "X"
		ccfg["axes/1/deadzone"] = 2
		ccfg.save()
		self.c.save()


if __name__ == "__main__":
	from scc.tools import init_logging, set_logging_level
	init_logging()
	set_logging_level(True, True)

	TestControllerConfig().test_create_values()
	TestControllerConfig.teardown_class()
