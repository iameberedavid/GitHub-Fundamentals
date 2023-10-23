import markdown 
def test_section_author(): 
	md_fp = "README.md" 
	with open(md_fp,) as f: 
		markdown_string = f.read() 
	html_string = markdown.markdown(markdown_string,).lower() 
	assert "author" in html_string[-300:]
