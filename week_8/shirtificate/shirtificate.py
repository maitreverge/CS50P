from fpdf import FPDF


class Shirtificate:
    def __init__(self, name):
        self.name = name
        self.generate()

    @classmethod
    def get(cls):
        name = input("What is your name ? ")
        return cls(name)

    def generate(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        # For the title
        pdf.set_font("Helvetica", "B", 50)
        pdf.cell(0, 50, txt="CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", x=5, y=80, w=200)

        # For the name
        f_text = f"{self.name} took CS50"
        text_width = pdf.get_string_width(f_text) / 2
        pdf.set_font("Helvetica", "B", size=30)
        pdf.set_text_color(255, 255, 255)

        x = (210 - text_width) / 2
        y = 180
        pdf.text(x, y, f_text)

        # Export the pdf
        pdf.output("shirtificate.pdf")


def main():
    Shirtificate.get()


if __name__ == "__main__":
    main()
