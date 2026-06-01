from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_dummy_pdf(
        filename="dummy.pdf",
        pages=20
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    dummy_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
    ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
    dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident,
    sunt in culpa qui officia deserunt mollit anim id est laborum.
    """

    for page in range(1, pages + 1):

        content.append(
            Paragraph(
                f"Page {page}",
                styles["Title"]
            )
        )

        for _ in range(20):

            content.append(
                Paragraph(
                    dummy_text,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 10)
            )

        content.append(
            PageBreak()
        )

    doc.build(content)

    print(
        f"{filename} generated successfully"
    )


if __name__ == "__main__":
    generate_dummy_pdf(
        filename="large_dummy.pdf",
        pages=1000
    )