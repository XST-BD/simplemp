from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Footer, Header, Input, Label


class InputWithLabel(Widget):
	DEFAULT_CSS = """
    InputWithLabel {
        layout: vertical;
        height: auto;
    }
    InputWithLabel Label {
        padding-top: 1;
        text-align: right;
    }
    InputWithLabel Input {
        width: 1fr;
        max-width: 50;
        height: 1;
    }
    """

	def __init__(self, input_label: str) -> None:
		self.input_label = input_label
		super().__init__()

	def compose(self) -> ComposeResult:
		yield Label(self.input_label)
		yield Input()


class SimpleMP(App):
	def compose(self):
		yield Header(show_clock=True)
		yield Footer()
		yield InputWithLabel("Enter input file name:")
		yield InputWithLabel("Enter output file name:")


if __name__ == "__main__":
	app = SimpleMP()
	app.run()
