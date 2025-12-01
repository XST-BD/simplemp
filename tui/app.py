from textual.app import App, on
from textual.containers import Horizontal, Container, VerticalScroll
from textual.widgets import Footer, Header, Input, Label, Checkbox, RadioSet, RadioButton, Button


class SimpleMP(App):
	CSS_PATH = "styles.tcss"

	CODECS = {

		# Audio

		"3gp": ["aac", "aac (fdk)"],
		"aac": ["aac", "aac (fdk)"],
		"adts": ["aac", "aac (fdk)"],
		"aif": ["pcm_s8", "pcm_s16be", "pcm_s24be", "pcm_s32be", "pcm_f32be", "pcm_f64be"],
		"aifc": ["pcm_s8", "pcm_s16be", "pcm_s24be", "pcm_s32be", "pcm_f32be", "pcm_f64be"],
		"aiff": ["pcm_s8", "pcm_s16be", "pcm_s24be", "pcm_s32be", "pcm_f32be", "pcm_f64be"],
		"alac": ["alac"],
		"amr": ["amr_nb", "amr_wb"],
		"awb": ["amr_wb"],
		"flac": ["flac"],
		"m4a": ["aac", "aac (fdk)"],
		"mp3": ["mp3"],
		"mp4": ["aac", "aac (fdk)"],
		"oga": ["vorbis", "opus", "flac", "speex"],
		"ogg": ["vorbis", "opus", "flac", "speex"],
		"opus": ["opus"],
		"wav": ["pcm_alaw", "pcm_mulaw", "pcm_s16le", "pcm_s24le", "pcm_s32le", "pcm_f32le", "pcm_f64le", "pcm_s16be",
		        "pcm_s24be", "pcm_s32be", "pcm_f32be", "pcm_f64be", "pcm_u8"],
		"wma": ["wmav1", "wmav2", "wmapro", "wmalossless"],

		# Images

		"png": ["png"],
		"jpg": ["mjpeg"],
		"jpeg": ["mjpeg"],
		"webp": ["webp"],
		"bmp": ["bmp"],
		"tiff": ["tiff"],
		"tif": ["tiff"],
		"gif": ["gif"],
		"ico": ["ico"],
		"pbm": ["pbm"],
		"pgm": ["pgm"],
		"ppm": ["ppm"],
		"pnm": ["pnm"],
		"svg": [],

		# Subtitles

		"srt": ["subrip"],
		"ass": ["ass"],
		"ssa": ["ssa"],
		"vtt": ["webvtt"],
		"sub": ["microdvd"],
		"sup": ["pgssub"],
		"scc": ["scc"],
		"ttml": ["ttml"],
		"dfxp": ["ttml"],
		"stl": ["ebu_stl"],
		"idx": ["vobsub"],

		# Video

		"mp4": ["h264", "hevc", "mpeg4", "libx264", "libx265", "libopenh264", "av1"],
		"mkv": ["h264", "hevc", "mpeg4", "vp8", "vp9", "av1"],
		"mov": ["h264", "hevc", "prores", "mpeg4"],
		"webm": ["vp8", "vp9", "av1"],
		"avi": ["mpeg4", "h264", "hevc"],
		"flv": ["flv", "h264"],
		"ts": ["h264", "hevc", "mpeg2video"],
		"mpeg": ["mpeg1video", "mpeg2video"],
		"mpg": ["mpeg1video", "mpeg2video"],
		"m4v": ["h264", "mpeg4"],
		"3gp": ["h264", "mpeg4"],
		"wmv": ["wmv1", "wmv2", "wmv3"],
		"asf": ["wmv1", "wmv2", "wmv3"],
	}

	def compose(self):
		with VerticalScroll():
			yield Header(show_clock=True)
			yield Footer()

			yield Label("Enter input file name:", shrink=True)
			yield Input(placeholder="File name with extension...")

			yield Label("Enter output file name:", shrink=True)
			yield Input(id="output_input", placeholder="File name with extension...")

			with Horizontal():
				with Container():
					yield Label("Bitrate:", shrink=True)
					yield Input(id="bitrate_input", placeholder="Number only (0 - 1000000)...")

				with Container():
					yield Label("Debug Mode:", shrink=True)
					yield Checkbox("Off", id="my-checkbox", value=False)

			with Horizontal():
				with Container():
					yield Label("Codec:", shrink=True)

					with RadioSet(id="codec_set"):
						yield Label("Write your output file name with extension first...", shrink=True)

			with Container(id="button_container"):
				yield Button("Submit", variant="primary")

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
				ext = ext[::-1].lower()

			self.update_codec_set(ext)

		elif event.input.id == "bitrate_input":
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
		codec_set.remove_children()

		if ext in self.CODECS:
			codecs = self.CODECS[ext]
			if not codecs:
				codec_set.mount(Label("No codecs available.", shrink=True))
				return
		else:
			codec_set.mount(Label("No codecs available.", shrink=True))
			return

		first = True
		for codec in codecs:
			codec_set.mount(RadioButton(codec, value=first))
			first = False


if __name__ == "__main__":
	app = SimpleMP()
	app.run()
