import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from textual.app import App, on
from textual.containers import Horizontal, Container, VerticalScroll
from textual.widgets import Footer, Header, Input, Label, Checkbox, RadioSet, RadioButton, Button
from avcore.compatcheck import codec_dict, video_sample_fmt_dict, audio_sample_fmt_dict
from avcore.audioprocessor import smpMediaProcessor


class SimpleMP(App):
	CSS_PATH = "styles.tcss"

	def compose(self):
		with VerticalScroll():
			yield Header(show_clock=True)
			yield Footer()

			yield Label("Enter input file name:", shrink=True)
			yield Input(id="input_file", placeholder="File name with extension...")

			yield Label("Enter output file name:", shrink=True)
			yield Input(id="output_input", placeholder="File name with extension...")

			with Horizontal():
				with Container():
					yield Label("Bitrate:", shrink=True)
					yield Input(id="bitrate_input", placeholder="Number only (0 - 1000000)...")

				with Container():
					yield Label("Sample Rate:", shrink=True)
					yield Input(id="samplerate_input", placeholder="Number only (0 - 1000000)...")

			with Horizontal():
				with Container():
					yield Label("Codec:", shrink=True)
					with RadioSet(id="codec_set"):
						yield Label("Write your output file name with extension first...", shrink=True)

				with Container():
					yield Label("Format:", shrink=True)
					with RadioSet(id="fmt_set"):
						yield Label("Select a Codec first...", shrink=True)

			with Horizontal():
				with Container():
					yield Label("Debug Mode:", shrink=True)
					yield Checkbox("Off", id="debug_mode", value=False)

			with Container(id="button_container"):
				yield Button("Submit", id="submit_btn", variant="primary")

	@on(Input.Changed)
	def on_input_changed(self, event: Input.Changed) -> None:
		if event.input.id == "output_input":
			filename = event.input.value
			ext = ""

			if '.' in filename:
				for c in filename[::-1]:
					if c == '.':
						break
					ext += c
				ext = "." + ext[::-1].lower()

			self.update_codec_set(ext)

		elif event.input.id == "samplerate_input" or event.input.id == "bitrate_input":
			value = event.input.value

			digits = ""
			for char in value:
				if char.isdigit():
					digits += char

			if digits != "":
				number = int(digits)
				if number > 1000000:
					number = 1000000
				event.input.value = str(number)
			else:
				event.input.value = ""

	@on(Checkbox.Changed)
	def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
		checkbox = self.query_one(Checkbox)
		checkbox.label = "On" if event.checkbox.value else "Off"

	def update_codec_set(self, ext: str):
		codec_set = self.query_one("#codec_set", RadioSet)
		fmt_set = self.query_one("#fmt_set", RadioSet)

		codec_set.value = None
		codec_set.remove_children()

		fmt_set.value = None
		fmt_set.remove_children()

		if ext in codec_dict:
			codecs = codec_dict[ext]
			if not codecs:
				codec_set.mount(Label("No codecs available.", shrink=True))
				fmt_set.mount(Label("Select a Codec first...", shrink=True))
				return
		else:
			codec_set.mount(Label("No codecs available.", shrink=True))
			fmt_set.mount(Label("Select a Codec first...", shrink=True))
			return

		for codec in codecs:
			codec_set.mount(RadioButton(codec))

		fmt_set.mount(Label("Select a Codec first...", shrink=True))

	@on(RadioSet.Changed, "#codec_set")
	def codec_changed(self, event: RadioSet.Changed):
		selected_button = event.pressed
		selected_codec = selected_button.label
		self.update_fmt_set(str(selected_codec))

	def update_fmt_set(self, selected_codec: str):
		fmt_set = self.query_one("#fmt_set", RadioSet)
		fmt_set.value = None
		fmt_set.remove_children()

		combined = {**video_sample_fmt_dict, **audio_sample_fmt_dict}

		if selected_codec in combined:
			fmts = combined[selected_codec]
			if not fmts:
				fmt_set.mount(Label("No format available.", shrink=True))
				return
		else:
			fmt_set.mount(Label("No format available.", shrink=True))
			return

		for fmt in fmts:
			fmt_set.mount(RadioButton(fmt))

	@on(Button.Pressed, "#submit_btn")
	def on_submit(self):
		input_file = self.query_one("#input_file", Input).value
		output_file = self.query_one("#output_file", Input).value
		bitrate_input = self.query_one("#bitrate_input", Input).value
		samplerate_input = self.query_one("#samplerate_input", Input).value
		codec_set = self.query_one("#codec_set", RadioSet).pressed_button.label
		fmt_set = self.query_one("#fmt_set", RadioSet).pressed_button.label
		debug_mode = self.query_one("#debug_mode", Checkbox).value

		smpMediaProcessor(
			inputfilename=input_file,
			outputfilename=output_file,
			bitrate=bitrate_input,
			samplerate=samplerate_input,
			codec=str(codec_set),
			sample_fmt=str(fmt_set),
			debug=debug_mode
		)


if __name__ == "__main__":
	app = SimpleMP()
	app.run()
