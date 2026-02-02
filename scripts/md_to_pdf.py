import pypandoc
import os

def md_to_pdf(md_file, pdf_file):
    """Convert MD to PDF (ASCII focus, no mermaid-filter)."""
    extra_args = [
        '--pdf-engine=xelatex',
        '--syntax-highlighting=pygments',
        '-V', 'geometry:margin=1in',
        '-V', 'fontsize=11pt'
    ]
    pypandoc.convert_file(md_file, 'pdf', outputfile=pdf_file, extra_args=extra_args)
    print(f"✅ Generated: {pdf_file}")

if __name__ == "__main__":
    # Create output folder "pdf" if it doesn't exist
    output_dir = os.path.join(os.getcwd(), "pdf")
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all .md files in current directory
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".md"):
            md_file = os.path.join(os.getcwd(), filename)
            pdf_file = os.path.join(output_dir, filename.replace(".md", ".pdf"))
            md_to_pdf(md_file, pdf_file)
