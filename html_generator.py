Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def generate_concept_HTML(concept_title, concept_description):
	text1 = """
	<div class="concept">
		<div class="concept_title>""" + concept_title
	text2 = """
		</div>
		<div class="concept_descritption">""" + concept_description
	text3 = """
		</div>
	</div>"""
	HTML_text = text1 + text2 + text3
	return HTML_text

>>> def create_HTML(concept):
	concept_title = concept[0]
	concept_description = concept[1]
	return generate_concept_HTML(concept_title, concept_description)

>>> def create_composite_HTML(list_of_concepts):
	HTML = ""
	for concept in list_of_concepts:
		HTML_concept = create_HTML(concept)
		HTML = HTML + HTML_concept
	return HTML

>>> TEST_LIST_OF_CONCEPTS = [ ['''Computers''', '''Computers can be programmed to carry out a set of instructions.
   				A computer program, is an exact sequence of instructions, written to perform a 
				specified task with a computer. Some examples of computer programs are web browsers 
				and simple print statements.'''], ['''Programming Language''', '''Programming is the
				core of Computer Science. A programming language is a formal constructed language 
				designed to communicate instructions to a computer. Examples of programming language 
				are Python, C++, Java and SQL.'''], ['''Compiler''', '''Compiler - a program that 
				producers another program. It transforms source code written in a programming language 
				(the source language) into another computer language (the target language).'''],
			     ['''String''', '''A string is a sequence of characters surrounding by quotes. A string 
				can be surrouded by single quotes (') or double quotes (").The only requirement is if 
				it starts with a sigle or double quote it needs to end with a single or double quote 
				respectively. Python does not allow you to concatenate a string and an interger. 
				However, strings can be multiplied. The following code: print '!' * 3  
                                Will display: !!!'''] ]
>>> print create_composite_HTML(TEST_LIST_OF_CONCEPTS)

	<div class="concept">
		<div class="concept_title>Computers
		</div>
		<div class="concept_descritption">Computers can be programmed to carry out a set of instructions.
   				A computer program, is an exact sequence of instructions, written to perform a 
				specified task with a computer. Some examples of computer programs are web browsers 
				and simple print statements.
		</div>
	</div>
	<div class="concept">
		<div class="concept_title>Programming Language
		</div>
		<div class="concept_descritption">Programming is the
				core of Computer Science. A programming language is a formal constructed language 
				designed to communicate instructions to a computer. Examples of programming language 
				are Python, C++, Java and SQL.
		</div>
	</div>
	<div class="concept">
		<div class="concept_title>Compiler
		</div>
		<div class="concept_descritption">Compiler - a program that 
				producers another program. It transforms source code written in a programming language 
				(the source language) into another computer language (the target language).
		</div>
	</div>
	<div class="concept">
		<div class="concept_title>String
		</div>
		<div class="concept_descritption">A string is a sequence of characters surrounding by quotes. A string 
				can be surrouded by single quotes (') or double quotes (").The only requirement is if 
				it starts with a sigle or double quote it needs to end with a single or double quote 
				respectively. Python does not allow you to concatenate a string and an interger. 
				However, strings can be multiplied. The following code: print '!' * 3  
                                Will display: !!!
		</div>
	</div>
>>> 
