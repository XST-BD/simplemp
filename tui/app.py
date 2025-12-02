import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from textual.app import App, ComposeResult, on
from textual.containers import Horizontal, Container, VerticalScroll
from textual.widgets import Footer, Header, Input, Label, Checkbox, RadioSet, RadioButton, Button, Switch
from textual_slider import Slider
from avcore.compatcheck import codec_dict, video_sample_fmt_dict, audio_sample_fmt_dict
from avcore.audioprocessor import smpMediaProcessor


def to_int(value, default=0) -> int:
	if value and value.isdigit():
		return int(value)
	return default


class SimpleMP(App):
	CSS_PATH = "styles.tcss"
	MAX_THREADS = os.cpu_count()

	@staticmethod
	def compose() -> ComposeResult:
		with VerticalScroll():
			yield Header(show_clock=True)
			yield Footer()

			with Container():
				yield Label("Enter input file name:", shrink=True)
				yield Input(id="input_file", placeholder="File name with extension...")

			with Container():
				yield Label("Enter output file name:", shrink=True)
				yield Input(id="output_file", placeholder="File name with extension...")

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
						yield Label("Write your output file name with extension first...", classes="info", shrink=True)

				with Container():
					yield Label("Format:", shrink=True)
					with RadioSet(id="fmt_set"):
						yield Label("Select a Codec first...", classes="info", shrink=True)

			with Horizontal():
				with Container():
					yield Label("FPS:", shrink=True)
					yield Input(id="fps_input", placeholder="Number only (0 - 60)...")

				with Container():
					yield Label("Threads:", shrink=True)
					yield Input(id="threads_input", placeholder=f"Number only (0 - {SimpleMP.MAX_THREADS})...")

			with Horizontal():
				with Container(classes="switch_container"):
					yield Label("Mute:", shrink=True)
					yield Switch(id="mute_mode", animate=False)

				with Container():
					yield Label("Volume: 50", id="volume_label", shrink=True)
					yield Slider(min=0, max=100, step=1, value=50, id="volume_input")

				with Container(classes="switch_container"):
					yield Label("Debug Mode:", shrink=True)
					yield Switch(id="debug_mode", animate=False)

			with Container(id="button_container"):
				yield Button("Submit", id="submit_btn", variant="primary")

	@on(Input.Changed)
	def on_input_changed(self, event: Input.Changed) -> None:
		if event.input.id == "output_file":
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

		elif event.input.id == "fps_input":
			value = event.input.value

			digits = ""
			for char in value:
				if char.isdigit():
					digits += char

			if digits != "":
				number = int(digits)
				if number > 60:
					number = 60
				event.input.value = str(number)
			else:
				event.input.value = ""

		elif event.input.id == "threads_input":
			value = event.input.value

			digits = ""
			for char in value:
				if char.isdigit():
					digits += char

			if digits != "":
				number = int(digits)
				if number > self.MAX_THREADS:
					number = self.MAX_THREADS
				event.input.value = str(number)
			else:
				event.input.value = ""

	@on(Slider.Changed, "#volume_input")
	def volume_changed(self, event: Slider.Changed):
		value = event.value
		label = self.query_one("#volume_label", Label)
		label.update(f"Volume: {value}")

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
		codec_set = self.query_one("#codec_set", RadioSet).pressed_button.label if self.query_one("#codec_set",
		                                                                                          RadioSet).pressed_button else None
		fmt_set = self.query_one("#fmt_set", RadioSet).pressed_button.label if self.query_one("#fmt_set",
		                                                                                      RadioSet).pressed_button else None
		fps_input = self.query_one("#fps_input", Input).value
		threads_input = self.query_one("#threads_input", Input).value
		mute_mode = self.query_one("#mute_mode", Switch).value
		volume_input = self.query_one("#volume_input", Slider).value
		debug_mode = self.query_one("#debug_mode", Switch).value

		smpMediaProcessor(
			inputfilename=input_file,
			outputfilename=output_file,
			bitrate=bitrate_input,
			samplerate=samplerate_input,
			codec=str(codec_set),
			sample_fmt=str(fmt_set),
			frame_rate=to_int(fps_input),
			threads=to_int(threads_input),
			mute=mute_mode,
			volume=volume_input,
			debug=debug_mode
		)


if __name__ == "__main__":
	app = SimpleMP()
	app.run()
