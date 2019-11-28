import sublime
import sublime_plugin
import json

s = sublime.load_settings("MapFormat.sublime-settings")
charList = ['{', '[', "=", "]", "}", ",", " "]

class MapFormatCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print("run...")
		# 获取输入的文本
		file_text = self.view.substr(sublime.Region(0, self.view.size()))
		print(file_text)
		# print(s.get('token', '123'))
		finaltext = ""
		textlist = list(file_text)
		isStr = 0;
		for c in textlist:
			if (c in charList):
				if (isStr == 1):
					 finaltext += "\""
				isStr = 0
			else:
				if (isStr == 0):
					finaltext += "\""
				isStr = 1
			if (c == '=') :
				c = ':'
			finaltext += c

		textJson = json.loads(finaltext)
		js = json.dumps(textJson, sort_keys=True, indent=4, separators=(',', ':'))

		# 替换最后的文本
		self.view.replace(edit, sublime.Region(0, self.view.size()), js)
